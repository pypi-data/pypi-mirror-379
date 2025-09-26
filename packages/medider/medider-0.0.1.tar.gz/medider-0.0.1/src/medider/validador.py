import re

class ValidadorBase:
    """
    Clase base que contiene métodos de validación generales
    """
    
    def validar_solo_numeros(self, texto: str) -> bool:
        """
        Valida que el texto contenga solo números
        
        Args:
            texto (str): Texto a validar
            
        Returns:
            bool: True si contiene solo números, False en caso contrario
        """
        if not texto:
            return False
        return texto.isdigit()
    
    def validar_solo_letras(self, texto: str) -> bool:
        """
        Valida que el texto contenga solo letras y espacios
        
        Args:
            texto (str): Texto a validar
            
        Returns:
            bool: True si contiene solo letras y espacios, False en caso contrario
        """
        if not texto:
            return False
        # Permite letras, espacios y caracteres especiales del español
        return all(c.isalpha() or c.isspace() or c in 'áéíóúÁÉÍÓÚñÑ' for c in texto)
    
    def validar_alfanumerico(self, texto: str) -> bool:
        """
        Valida que el texto contenga solo caracteres alfanuméricos
        
        Args:
            texto (str): Texto a validar
            
        Returns:
            bool: True si es alfanumérico, False en caso contrario
        """
        if not texto:
            return False
        return texto.replace(' ', '').isalnum()


class ValidadorDatosPersonales(ValidadorBase):
    """
    Clase especializada en validación de datos personales
    que utiliza internamente métodos de ValidadorBase
    """
    
    def validar_edad(self, edad: str) -> bool:
        """
        Valida que la edad sea un número entre 0 y 120
        Utiliza validar_solo_numeros de ValidadorBase
        
        Args:
            edad (str): Edad a validar
            
        Returns:
            bool: True si la edad es válida, False en caso contrario
        """
        # Usa el método de la clase base para validar que sean solo números
        if not self.validar_solo_numeros(edad):
            return False
        
        try:
            edad_num = int(edad)
            return 0 <= edad_num <= 120
        except ValueError:
            return False
    
    def validar_nombre(self, nombre: str) -> bool:
        """
        Valida que el nombre contenga solo letras y espacios
        Utiliza validar_solo_letras de ValidadorBase
        
        Args:
            nombre (str): Nombre a validar
            
        Returns:
            bool: True si el nombre es válido, False en caso contrario
        """
        if not nombre or len(nombre.strip()) < 2:
            return False
        
        # Usa el método de la clase base para validar que sean solo letras
        return self.validar_solo_letras(nombre)
    
    def validar_documento_identidad(self, documento: str) -> bool:
        """
        Valida el formato del documento de identidad
        Utiliza validar_alfanumerico de ValidadorBase
        
        Args:
            documento (str): Documento a validar
            
        Returns:
            bool: True si el documento es válido, False en caso contrario
        """
        if not documento or len(documento) < 5:
            return False
        
        # Limpia el documento eliminando espacios y guiones
        documento_limpio = documento.replace(' ', '').replace('-', '')
        
        # Usa el método de la clase base para validar que sea alfanumérico
        return self.validar_alfanumerico(documento_limpio) and len(documento_limpio) >= 5


class ValidadorDatosContacto(ValidadorBase):
    """
    Clase especializada en validación de datos de contacto
    que utiliza internamente métodos de ValidadorBase
    """
    
    def validar_email(self, email: str) -> bool:
        """
        Valida el formato de un email
        Utiliza métodos de validación de la clase base
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si el email es válido, False en caso contrario
        """
        if not email:
            return False
        
        email = email.strip()
        
        # Patrón básico para validar email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, email))
    
    def validar_celular(self, celular: str) -> bool:
        """
        Valida el formato de un número de celular
        Utiliza validar_solo_numeros de ValidadorBase
        
        Args:
            celular (str): Número de celular a validar
            
        Returns:
            bool: True si el celular es válido, False en caso contrario
        """
        if not celular:
            return False
        
        # Limpia el número (elimina espacios, guiones, paréntesis, etc.)
        celular_limpio = re.sub(r'[\s\-\(\)\+]', '', celular)
        
        # Usa el método de la clase base para validar que sean solo números
        return (self.validar_solo_numeros(celular_limpio) and 
                8 <= len(celular_limpio) <= 15)
    
    def validar_direccion(self, direccion: str) -> bool:
        """
        Valida el formato de una dirección
        Utiliza métodos de validación de la clase base
        
        Args:
            direccion (str): Dirección a validar
            
        Returns:
            bool: True si la dirección es válida, False en caso contrario
        """
        if not direccion or len(direccion.strip()) < 10:
            return False
        
        direccion_limpia = direccion.strip()
        
        # Una dirección válida debe contener al menos números y letras
        # Usa lógica de la clase base para validar caracteres
        tiene_numeros = any(c.isdigit() for c in direccion_limpia)
        tiene_letras = any(c.isalpha() for c in direccion_limpia)
        
        return tiene_numeros and tiene_letras and len(direccion_limpia) >= 10