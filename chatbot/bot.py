class SimpleChatbot:
    def __init__(self):
        self.user_name = None

    def get_response(self, message):
        message = message.lower()

        if "my name is" in message:
            self.user_name = message.split("my name is")[-1].strip().title()
            return f"Nice to meet you, {self.user_name}!"

        if "what is my name" in message:
            if self.user_name:
                return f"Your name is {self.user_name}."
            return "I don't know your name yet."

        if "book a flight" in message:
            return "Sure, I can help you with flight booking."

        if "refund" in message:
            return "I can help you with refund-related queries."

        if "capital of india" in message:
            return "The capital of India is New Delhi."

        if "who is ceo of mars in 2050" in message:
            return "I don't have enough verified information to answer that."

        return "Sorry, I did not understand your request."
