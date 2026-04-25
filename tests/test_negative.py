from chatbot.bot import SimpleChatbot


def test_unknown_message_fallback():
    bot = SimpleChatbot()

    response = bot.get_response("xyz random unknown input")

    assert "did not understand" in response.lower()
