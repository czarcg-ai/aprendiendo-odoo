import time
class personaje:
    
    # 1. Constructor: Corregimos 'Nombre' a 'nombre' (minúsculas)
    def __init__(self, nombre, vida):
        self.nombre = nombre 
        self.vida = vida

    # 2. Función del golpe
    def Coñazo(self):
        self.vida = self.vida - 10
        # El print debe estar indentado (metido) aquí adentro
        print(f"{self.nombre} recibió un misilazo. Vida restante: {self.vida}")

# --- ZONA DE EJECUCIÓN ---
# Creamos al primer personaje usando el molde 'personaje'
hp1 = personaje("Maduro cds", 100)
# Creamos al SEGUNDO personaje usando EL MISMO molde 'personaje'
# (Solo cambiamos el nombre de la variable a la izquierda)
hp2 = personaje("Diosdi hp", 100)
hp1.Coñazo()
print(f"¡misilazos pa miraflores {hp1.nombre}!")
while hp1.vida > 0:
    hp1.Coñazo()  
    time.sleep(1)
print("cayeron manooo")