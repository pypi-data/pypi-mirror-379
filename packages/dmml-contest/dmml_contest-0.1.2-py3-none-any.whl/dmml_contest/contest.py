import numpy as np
import pandas as pd
import requests


class Contest:
    def __init__(self, display_name: str, contest_id: str, user_key: str, contest_api_url: str) -> None:
        self.display_name = display_name
        self.contest_id = contest_id
        self.user_key = user_key
        self.contest_api_url = contest_api_url

        # self.request_timeout = 1

        self._fetch_contest_info()

        print(f"Hello, {self.full_name} ({self.display_name})!")
        print(f"Welcome to the following contest: {self.contest_name}")

    def _fetch_contest_info(self) -> None:
        response = requests.post(  # noqa: S113
            f"{self.contest_api_url}/contest",
            json={"contest_id": self.contest_id, "user_key": self.user_key},
            headers={"user_key": self.user_key},
            # timeout=self.request_timeout,
        )

        if response.status_code == 200:
            data: dict = response.json()
            self.full_name: str = data.get("full_name")  # pyright: ignore[reportAttributeAccessIssue]
            contest_info: dict = data.get("contest_info")  # pyright: ignore[reportAssignmentType]
            self.contest_name: str = contest_info.get("contest_name")  # pyright: ignore[reportAttributeAccessIssue]
            self._train_data_url: str = contest_info.get("train_data_url")  # pyright: ignore[reportAttributeAccessIssue]
            self._test_data_url: str = contest_info.get("test_data_url")  # pyright: ignore[reportAttributeAccessIssue]

        elif response.status_code == 404:
            data = response.json()
            raise Exception("API returned not found error: " + data.get("detail", ""))

        else:
            raise Exception(f"Failed to fetch contest data. Status code: {response.status_code}")

    def fetch_train_data(self) -> pd.DataFrame:
        """Fetches the training data from the contest server."""
        return pd.read_csv(self._train_data_url)

    def fetch_test_data(self) -> pd.DataFrame:
        """Fetches the test data from the contest server."""
        return pd.read_csv(self._test_data_url)

    def submit_prediction(self, prediction_array: np.ndarray | list) -> dict:
        """Submits the predictions to the contest server."""

        if isinstance(prediction_array, np.ndarray):
            prediction_array = prediction_array.tolist()

        submit_url = f"{self.contest_api_url}/submit"

        payload = {
            "user_key": self.user_key,
            "contest_id": self.contest_id,
            "predictions": prediction_array,
            "display_name": self.display_name,
        }

        response = requests.post(  # noqa: S113
            submit_url,
            json=payload,
            # timeout=self.request_timeout
        )

        if response.status_code == 200:
            data = response.json()
            return data

        elif response.status_code == 429:
            raise Exception("Rate limit exceeded. Please try again later.")

        else:
            raise Exception(f"Failed to submit predictions. Status code: {response.status_code}")
