"""
Medider - Librería de validación de datos
"""

from .validador import ValidadorBase, ValidadorDatosPersonales, ValidadorDatosContacto

__version__ = "1.0.0"
__all__ = ["ValidadorBase", "ValidadorDatosPersonales", "ValidadorDatosContacto"]