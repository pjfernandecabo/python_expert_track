class GreeterPlugin:
    name = "Greeter"

    def process(self, text: str) -> str:
        return f"Hola! 👋 {text}"

plugin = GreeterPlugin()
