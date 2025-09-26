import unittest
import sys
import os

# Añade el directorio src al path para poder importar los módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from medider import ValidadorBase, ValidadorDatosPersonales, ValidadorDatosContacto

class TestValidadorBase(unittest.TestCase):
    
    def setUp(self):
        self.validador = ValidadorBase()
    
    def test_validar_solo_numeros(self):
        self.assertTrue(self.validador.validar_solo_numeros("12345"))
        self.assertTrue(self.validador.validar_solo_numeros("0"))
        self.assertFalse(self.validador.validar_solo_numeros("123a45"))
        self.assertFalse(self.validador.validar_solo_numeros("12.34"))
        self.assertFalse(self.validador.validar_solo_numeros(""))
    
    def test_validar_solo_letras(self):
        self.assertTrue(self.validador.validar_solo_letras("Juan Pérez"))
        self.assertTrue(self.validador.validar_solo_letras("María José"))
        self.assertTrue(self.validador.validar_solo_letras("Ángel Martínez"))
        self.assertFalse(self.validador.validar_solo_letras("Juan123"))
        self.assertFalse(self.validador.validar_solo_letras(""))
    
    def test_validar_alfanumerico(self):
        self.assertTrue(self.validador.validar_alfanumerico("abc123"))
        self.assertTrue(self.validador.validar_alfanumerico("123abc"))
        self.assertTrue(self.validador.validar_alfanumerico("abc 123"))
        self.assertFalse(self.validador.validar_alfanumerico("abc@123"))
        self.assertFalse(self.validador.validar_alfanumerico(""))


class TestValidadorDatosPersonales(unittest.TestCase):
    
    def setUp(self):
        self.validador = ValidadorDatosPersonales()
    
    def test_validar_edad(self):
        self.assertTrue(self.validador.validar_edad("25"))
        self.assertTrue(self.validador.validar_edad("0"))
        self.assertTrue(self.validador.validar_edad("120"))
        self.assertFalse(self.validador.validar_edad("121"))
        self.assertFalse(self.validador.validar_edad("-5"))
        self.assertFalse(self.validador.validar_edad("25a"))
        self.assertFalse(self.validador.validar_edad(""))
    
    def test_validar_nombre(self):
        self.assertTrue(self.validador.validar_nombre("Juan Pérez García"))
        self.assertTrue(self.validador.validar_nombre("María José López"))
        self.assertFalse(self.validador.validar_nombre("Juan123"))
        self.assertFalse(self.validador.validar_nombre(""))
    
    def test_validar_documento_identidad(self):
        self.assertTrue(self.validador.validar_documento_identidad("12345678A"))
        self.assertTrue(self.validador.validar_documento_identidad("123-456-789"))
        self.assertTrue(self.validador.validar_documento_identidad("AB123456"))
        self.assertFalse(self.validador.validar_documento_identidad("123"))
        self.assertFalse(self.validador.validar_documento_identidad(""))
        self.assertFalse(self.validador.validar_documento_identidad("123@456"))


class TestValidadorDatosContacto(unittest.TestCase):
    
    def setUp(self):
        self.validador = ValidadorDatosContacto()
    
    def test_validar_email(self):
        self.assertTrue(self.validador.validar_email("usuario@example.com"))
        self.assertTrue(self.validador.validar_email("nombre.apellido@empresa.co.uk"))
        self.assertFalse(self.validador.validar_email("usuario@"))
        self.assertFalse(self.validador.validar_email("@example.com"))
        self.assertFalse(self.validador.validar_email("usuario.example.com"))
        self.assertFalse(self.validador.validar_email(""))
    
    def test_validar_celular(self):
        self.assertTrue(self.validador.validar_celular("612345678"))
        self.assertTrue(self.validador.validar_celular("+34612345678"))
        self.assertTrue(self.validador.validar_celular("+34 612 345 678"))
        self.assertFalse(self.validador.validar_celular("123"))
        self.assertFalse(self.validador.validar_celular("6123456789012345"))
        self.assertFalse(self.validador.validar_celular(""))
    
    def test_validar_direccion(self):
        self.assertTrue(self.validador.validar_direccion("Calle Principal 123"))
        self.assertTrue(self.validador.validar_direccion("Av. Siempre Viva 742, Springfield"))
        self.assertFalse(self.validador.validar_direccion("Calle Sin Número"))
        self.assertFalse(self.validador.validar_direccion("123"))
        self.assertFalse(self.validador.validar_direccion(""))


if __name__ == '__main__':
    unittest.main()