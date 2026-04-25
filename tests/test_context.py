from chatbot.bot import SimpleChatbot


def test_chatbot_remembers_user_name():
    bot = SimpleChatbot()

    bot.get_response("My name is Pragya")
    response = bot.get_response("What is my name?")

    assert "Pragya" in response
