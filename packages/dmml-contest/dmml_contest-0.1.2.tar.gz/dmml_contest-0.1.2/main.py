import numpy as np

from dmml_contest.contest import Contest


def main():
    contest = Contest(
        display_name="dapagyi_test",  # This can be anything in case you don't want to use your real name on the leaderboard.
        contest_id="dmml-2025-09-25",
        user_key="user123",
        contest_api_url="http://localhost:8000",
    )
    train_data = contest.fetch_train_data()
    test_data = contest.fetch_test_data()
    print(train_data.shape)
    # print(test_data.info())

    sample_submission = np.ones(len(test_data))
    response = contest.submit_prediction(sample_submission)
    print("Submission response:", response)


if __name__ == "__main__":
    main()
