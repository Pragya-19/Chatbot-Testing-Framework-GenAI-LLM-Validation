import csv
from chatbot.bot import SimpleChatbot
from utils.response_validator import validate_keyword, calculate_response_score


def load_test_data():
    test_cases = []

    with open("test_data/chatbot_test_data.csv", mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            test_cases.append(row)

    return test_cases


def test_chatbot_using_csv_data():
    bot = SimpleChatbot()
    test_cases = load_test_data()

    for test_case in test_cases:
        response = bot.get_response(test_case["user_prompt"])
        expected_keyword = test_case["expected_keyword"]

        assert validate_keyword(response, expected_keyword)

        score = calculate_response_score(response, expected_keyword)
        assert score == 100
