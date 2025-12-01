class UppercaserPlugin:
    name = "Uppercaser"

    def process(self, text: str) -> str:
        return text.upper()

plugin = UppercaserPlugin()
