from chatbot.bot import SimpleChatbot


def test_same_intent_with_different_prompts():
    bot = SimpleChatbot()

    prompts = [
        "I want to book a flight",
        "Can you help me book a flight?",
        "Book a flight to Delhi"
    ]

    for prompt in prompts:
        response = bot.get_response(prompt)
        assert "flight booking" in response.lower()
