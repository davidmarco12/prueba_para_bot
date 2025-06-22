# Código con duplicados intencionalmente para demostrar el bot
# Agrega este archivo a tu repositorio para una demo completa

def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo"""
    resultado = ancho * alto
    return resultado

def obtener_area_rectangulo(width, height):
    """Obtiene el área de un rectángulo - DUPLICADO SEMÁNTICO"""
    area = width * height
    return area

def calcular_superficie_rectangulo(w, h):
    """Calcula superficie de rectángulo - OTRO DUPLICADO"""
    return w * h

def sumar_dos_numeros(a, b):
    """Suma dos números"""
    total = a + b
    return total

def agregar_numeros(x, y):
    """Agrega dos números - DUPLICADO SEMÁNTICO"""
    resultado = x + y
    return resultado

def procesar_lista_elementos(items):
    """Procesa una lista duplicando cada elemento"""
    resultado = []
    for item in items:
        resultado.append(item * 2)
    return resultado

def transformar_lista_elementos(elementos):
    """Transforma lista duplicando elementos - DUPLICADO ESTRUCTURAL"""
    nueva_lista = []
    for elemento in elementos:
        nueva_lista.append(elemento * 2)
    return nueva_lista

def multiplicar_por_dos(lista):
    """Multiplica por 2 cada elemento - OTRO DUPLICADO"""
    output = []
    for elem in lista:
        output.append(elem * 2)
    return output

def validar_email_simple(email):
    """Valida email de forma simple"""
    return "@" in email and "." in email

def verificar_email_basico(correo):
    """Verifica email básicamente - DUPLICADO SEMÁNTICO"""
    return "@" in correo and "." in correo

# Función exactamente duplicada
def calcular_descuento(precio, porcentaje):
    """Calcula descuento"""
    return precio * (porcentaje / 100)

# Función EXACTAMENTE igual
def calcular_descuento_copia(precio, porcentaje):
    """Calcula descuento"""
    return precio * (porcentaje / 100)