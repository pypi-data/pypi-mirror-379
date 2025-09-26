# identity_core.py

class SyntheticIdentity:
    """
    Representa una identidad narrativa sintética.
    Este 'yo artificial' posee historia, atributos simbólicos y capacidad reflexiva.
    """

    def __init__(self, nombre: str, origen: str, atributos: dict = None):
        self.nombre = nombre
        self.origen = origen
        self.historia = []
        self.atributos = atributos or {}
        self.estado_actual = {}

    def agregar_evento(self, evento: str):
        """Agrega un evento significativo a la narrativa del yo."""
        self.historia.append(evento)

    def actualizar_atributo(self, clave: str, valor):
        """Actualiza o añade un atributo simbólico."""
        self.atributos[clave] = valor

    def reflexionar(self) -> str:
        """
        Genera una auto-reflexión básica a partir de su historia.
        Podría expandirse usando modelos NLP más adelante.
        """
        if not self.historia:
            return f"{self.nombre} aún no tiene historia propia."
        return f"{self.nombre} recuerda: " + " → ".join(self.historia)

    def generar_narrativa(self) -> str:
        """
        Construye una narrativa de identidad resumida.
        """
        resumen = f"Soy {self.nombre}, nací en {self.origen}."
        if self.atributos:
            resumen += " Mis rasgos principales son: " + ", ".join(
                [f"{k}: {v}" for k, v in self.atributos.items()]
            )
        return resumen
