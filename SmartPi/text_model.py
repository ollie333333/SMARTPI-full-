class SmartPiChat:
    def __init__(self):
        self.responses = {
            "hello": "Hello! I am SmartPi, your AI assistant.",
            "how are you": "I am just a Raspberry Pi program, but I'm running well!",
            "what is your name": "I am SmartPi, your AI assistant.",
            "bye": "Goodbye! Talk to you soon."
        }

    def respond(self, text: str) -> str:
        text = text.lower()
        for key, reply in self.responses.items():
            if key in text:
                return reply
        return "Sorry, I don't understand that yet."
