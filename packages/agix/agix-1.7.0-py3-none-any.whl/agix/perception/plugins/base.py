class SensorPlugin:
    """Clase base para plugins de sensores."""

    def process(self, raw_input):
        """Convierte la entrada cruda a un formato manejable."""
        raise NotImplementedError("process debe implementarse en subclases")
