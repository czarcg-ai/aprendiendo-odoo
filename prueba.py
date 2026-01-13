class personaje:
    
    # 1. Constructor: Corregimos 'Nombre' a 'nombre' (minúsculas)
    def __init__(self, nombre, vida):
        self.nombre = nombre 
        self.vida = vida

    # 2. Función del golpe
    def Coñazo(self):
        self.vida = self.vida - 10
        # El print debe estar indentado (metido) aquí adentro
        print(f"{self.nombre} recibió un golpe. Vida restante: {self.vida}")

# --- ZONA DE EJECUCIÓN ---

# Creamos al primer personaje usando el molde 'personaje'
mi_personaje = personaje("Maduro cds", 1000)

# Creamos al SEGUNDO personaje usando EL MISMO molde 'personaje'
# (Solo cambiamos el nombre de la variable a la izquierda)
mi_personaje2 = personaje("Diosdi hp", 1000)

# Golpeamos al segundo personaje
mi_personaje.Coñazo()
