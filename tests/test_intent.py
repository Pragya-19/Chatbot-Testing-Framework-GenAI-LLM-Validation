from chatbot.bot import SimpleChatbot


def test_flight_booking_intent():
    bot = SimpleChatbot()

    response = bot.get_response("I want to book a flight to Delhi")

    assert "flight booking" in response.lower()


def test_refund_intent():
    bot = SimpleChatbot()

    response = bot.get_response("I need refund for my ticket")

    assert "refund" in response.lower()
