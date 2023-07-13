# pylint: disable=too-few-public-methods
"""
Este módulo contiene la definición de la clase BaseService, 
la cual es una clase abstracta que otros servicios deberían heredar.
"""
class BaseService:
    """
    Clase base para los servicios. Define una interfaz común para todos los servicios.
    """
    def perform(self):
        """
        Método que cada servicio debe implementar.
        """
        raise NotImplementedError("Subclasses must implement this method.")
