import sqlite3
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from litestar import Litestar, Request, get, post
from litestar.config.cors import CORSConfig
from litestar.exceptions import HTTPException
from litestar.static_files import create_static_files_router
from litestar.status_codes import HTTP_200_OK
from pydantic import BaseModel
from sklearn.metrics import f1_score

# ---- Configurations and Constants ---- #
DATABASE_PATH = "predictions.db"
BASE_URL = "http://localhost:8000" # https://dmml.dapagyi.dedyn.io
CONTESTS = {
    "dmml-2025-09-25": {
        "contest_name": "DMML 2025-09-25",
        "submission_rate_limit": 2,
        "train_data_url": f"{BASE_URL}/static/dmml-2025-09-25/train.csv",
        "test_data_url": f"{BASE_URL}/static/dmml-2025-09-25/test.csv",
        "solution_file": "solutions/dmml-2025-09-25.csv",
    },
    # "practice_1015": {
    #     "contest_name": "Practice 10-15",
    #     "submission_rate_limit": 2,
    #     "train_data_url": "https://dmml.dapagyi.dedyn.io/static/practice_1015/train.csv",
    #     "test_data_url": "https://dmml.dapagyi.dedyn.io/static/practice_1015/test.csv",
    #     "solution_file": "solutions/practice_1015.csv",
    # },
}
USERS = {
    "david123": {"full_name": "Apagyi Dávid"},
    "user123": {"full_name": "Alice Smith"},
}
# df = pd.read_csv("users.csv")
# users_from_file = {
#     user_key: {"full_name": full_name}
#     for user_key, full_name in zip(df["user_key"], df["full_name"])
# }
# USERS = dict(**USERS, **users_from_file)


RATE_LIMIT_TIME = timedelta(minutes=1)
ASSETS_DIR = Path("assets")

# ---- Logging Setup ---- #
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


# ---- Database Setup ---- #
def setup_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            user_key TEXT,
            contest_id TEXT,
            prediction TEXT,
            score FLOAT,
            timestamp DATETIME
        )
    """
    )
    conn.commit()
    return conn


db_conn = setup_db()


def get_contest_info(user_key: str, contest_id: int):
    if user_key not in USERS or contest_id not in CONTESTS:
        raise HTTPException(status_code=404, detail="Invalid user key or contest ID")

    user_info = USERS[user_key]
    contest_info = CONTESTS[contest_id]

    return {
        "full_name": user_info["full_name"],
        "contest_name": contest_info["contest_name"],
        "submission_rate_limit": contest_info["submission_rate_limit"],
        "train_data_url": contest_info["train_data_url"],
        "test_data_url": contest_info["test_data_url"],
    }


class ContestInfoResponse(BaseModel):
    full_name: str
    neptun_code: str
    contest_name: str
    submission_rate_limit: int
    train_data_url: str
    test_data_url: str


@get("/contest")
async def get_contest(user_key: str, contest_id: str) -> ContestInfoResponse:
    contest_info = get_contest_info(user_key, contest_id)
    return contest_info


def check_rate_limit(user_key: str, contest_id: int, db_conn):
    cursor = db_conn.cursor()
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM submissions
        WHERE user_key = ? AND contest_id = ? AND timestamp > ?
        """,
        (user_key, contest_id, datetime.now() - RATE_LIMIT_TIME),
    )

    count = cursor.fetchone()[0]

    if count >= CONTESTS[contest_id]["submission_rate_limit"]:
        raise HTTPException(status_code=429, detail="Submission rate limit exceeded")


def save_prediction(
    username: str,
    user_key: str,
    contest_id: int,
    prediction: str,
    score: float,
    db_conn,
):
    cursor = db_conn.cursor()
    cursor.execute(
        """
        INSERT INTO submissions (username, user_key, contest_id, prediction, score, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        (username, user_key, contest_id, prediction, score, datetime.now()),
    )
    db_conn.commit()


def evaluate_prediction(predictions: pd.DataFrame, contest_id: int) -> float:
    solution_path = CONTESTS[contest_id]["solution_file"]
    solution_df = pd.read_csv(solution_path)
    if predictions.shape != solution_df.shape:
        raise HTTPException(
            status_code=400,
            detail=f"Shape mismatch between submission and solution. Expected {solution_df.shape}, got {predictions.shape}.",
        )
    try:
        # if contest_id == "dmml-2025-09-25":
        #     return f1_score(solution_df.values, predictions.values)
        # elif contest_id == "practice_1015":
        #     return roc_auc_score(solution_df.values, predictions.values)
        return f1_score(solution_df.values, predictions.values)

    except Exception as _e:
        raise HTTPException(
            status_code=400,
            detail="Invalid prediction.",
        )


@dataclass
class PredictionSubmitRequest:
    username: str
    user_key: str
    contest_id: str
    predictions: list[float]


@post("/test")
async def test(data: PredictionSubmitRequest) -> dict:
    print(data)
    return {"data": data}


@post("/submit", status_code=HTTP_200_OK)
async def submit_prediction(request: Request, data: PredictionSubmitRequest) -> dict:
    if data.user_key not in USERS or data.contest_id not in CONTESTS:
        raise HTTPException(status_code=404, detail="Invalid user or contest ID")
    request.logger.info(
        f"User {data.user_key} submitting prediction for contest {data.contest_id}"
    )
    check_rate_limit(data.user_key, data.contest_id, db_conn)
    try:
        predictions_df = pd.DataFrame(data.predictions)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file format")

    f1 = evaluate_prediction(predictions_df, data.contest_id)
    save_prediction(
        data.username,
        data.user_key,
        data.contest_id,
        predictions_df.to_csv(index=False),
        f1,
        db_conn,
    )
    request.logger.info(f"User {data.user_key}'s submission achieved F1-score: {f1}")
    return {"f1_score": f1}


class Submission(BaseModel):
    id: int
    contest_id: str
    score: float
    timestamp: datetime
    username: str


# Helper function to query the top submissions from the database
def get_top_submissions(contest_id: str, limit: int = 10):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, username, contest_id, score, timestamp
        FROM submissions
        WHERE contest_id = ?
        ORDER BY score DESC, timestamp ASC
        LIMIT ?
        """,
        (contest_id, limit),
    )

    rows = cursor.fetchall()
    conn.close()

    return rows


# Helper function to query the top submissions from the database
def get_top_submissions_per_user(contest_id: str, limit: int = 10):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        WITH RankedSubmissions AS (
            SELECT id, username, contest_id, score, timestamp,
                ROW_NUMBER() OVER (PARTITION BY username ORDER BY score DESC, timestamp ASC) AS rank
            FROM submissions
            WHERE contest_id = ?
        )
        SELECT id, username, contest_id, score, timestamp
        FROM RankedSubmissions
        WHERE rank = 1
        ORDER BY score DESC, timestamp ASC
        LIMIT ?;
        """,
        (contest_id, limit),
    )

    rows = cursor.fetchall()
    conn.close()

    return rows


@dataclass
class FetchSubmissionsRequest:
    contest_id: str
    # limit: int


# API endpoint to fetch top submissions by contest_id
@post("/top-submissions")
async def fetch_top_submissions(data: FetchSubmissionsRequest) -> list[Submission]:
    if not data.contest_id:
        raise HTTPException(status_code=400, detail="Contest ID is required")
    limit = 500
    submissions = get_top_submissions(data.contest_id, limit)

    # Convert results to list of dicts for Pydantic model
    result = [
        Submission(
            id=row[0],
            username=row[1],
            contest_id=row[2],
            score=row[3],
            timestamp=row[4],
        )
        for row in submissions
    ]

    return result


# API endpoint to fetch top submissions by contest_id
@post("/top-submissions-per-user")
async def fetch_top_submissions_per_user(
    data: FetchSubmissionsRequest,
) -> list[Submission]:
    if not data.contest_id:
        raise HTTPException(status_code=400, detail="Contest ID is required")
    limit = 500
    submissions = get_top_submissions_per_user(data.contest_id, limit)

    # Convert results to list of dicts for Pydantic model
    result = [
        Submission(
            id=row[0],
            username=row[1],
            contest_id=row[2],
            score=row[3],
            timestamp=row[4],
        )
        for row in submissions
    ]

    return result


cors_config = CORSConfig(
    allow_origins=[
        "https://apagyidavid.web.elte.hu",
        "https://dmml-contest.dapagyi-oracle.duckdns.org",
        "https://dmml.dapagyi.dedyn.io"
    ]
)

app = Litestar(
    route_handlers=[
        fetch_top_submissions,
        fetch_top_submissions_per_user,
        test,
        get_contest,
        submit_prediction,
        create_static_files_router(path="/static", directories=["static"]),
    ],
    cors_config=cors_config,
)
