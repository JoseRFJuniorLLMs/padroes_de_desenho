"""
Propósito: Asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.
"""
class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.config = {}
        self._initialized = True

# Uso
config1 = ConfigurationManager()
config2 = ConfigurationManager()
print(config1 is config2)  # Imprime: True
