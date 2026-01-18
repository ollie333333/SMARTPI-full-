class SmartPiChat:
    """
    Simple offline chatbot logic.
    """
    def __init__(self):
        self.responses = {
            "hello": "Hello! I am SmartPi, your AI assistant.",
            "how are you": "I'm just a program, but I'm doing well!",
            "what is your name": "I am SmartPi.",
            "bye": "Goodbye! Talk soon."
        }

    def respond(self, text: str) -> str:
        text = text.lower()
        for key, reply in self.responses.items():
            if key in text:
                return reply
        return "Sorry, I don't understand that yet."
