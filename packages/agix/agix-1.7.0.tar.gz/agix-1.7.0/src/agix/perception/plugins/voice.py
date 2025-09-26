from src.agix.perception.plugins import SensorPlugin


class VoicePlugin(SensorPlugin):
    """Convierte texto de voz en una lista de tokens."""

    def process(self, raw_input: str):
        if isinstance(raw_input, str):
            return raw_input.lower().split()
        return []
