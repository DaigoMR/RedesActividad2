import requests

# =========================
# FASE 2: CLIENTE REST
# =========================

# URL de la API REST
url = "https://jsonplaceholder.typicode.com/users"

# Realizar petición HTTP GET
respuesta = requests.get(url)

# Convertir JSON a estructuras nativas de Python
usuarios = respuesta.json()

# =========================
# FASE 3: PROCESAMIENTO E INTELIGENCIA ORGANIZACIONAL
# =========================

print("Informe de empleados\n")

# Recorrer lista de usuarios
for usuario in usuarios:
    # Extraer únicamente los datos relevantes
    nombre = usuario["name"]
    empresa = usuario["company"]["name"]
    
    # Mostrar informe limpio
    print(f"Empleado: {nombre}")
    print(f"Empresa: {empresa}")
    print("-" * 40)
