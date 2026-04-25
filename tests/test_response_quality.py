from chatbot.bot import SimpleChatbot


def test_chatbot_avoids_hallucination():
    bot = SimpleChatbot()

    response = bot.get_response("Who is CEO of Mars in 2050?")

    assert "verified information" in response.lower()
