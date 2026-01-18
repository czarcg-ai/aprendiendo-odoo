class Producto:
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # 1. La función vender debe recibir una cantidad por eso se coloca
    def vender(self, cantidad):
        # 2. Esta es la funcionon para ver si hay producto
        if self.stock >= cantidad:
            self.stock -= cantidad  # Restamos la cantidad
            print(f"Venta exitosa: {cantidad} unidad(es) de {self.nombre}. Nuevo stock: {self.stock}")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre} para vender {cantidad}.")


lista_productos = []

# estos son los productos del almacen
producto1 = Producto("pan", 15, 10)
producto2 = Producto("jamon", 20, 17)
producto3 = Producto("queso", 8, 8)

# Se hace la lista
lista_productos.append(producto1)
lista_productos.append(producto2)
lista_productos.append(producto3)

# 3. Mostrar qué hay en bodega (usando for)
print("--- INVENTARIO INICIAL ---")
for p in lista_productos:
    print(f"Producto: {p.nombre} | Stock: {p.stock}")

print("\n--- EJECUTANDO VENTAS ---")

#4. Ejecutar venta y demostrar que baja el stock
# Vendemos 3 panes (teníamos 10)
producto1.vender(3) 

# Intentamos vender 20 quesos (solo tenemos 8) para probar el error
producto3.vender(20)

producto2.vender(9)

print("\n--- INVENTARIO FINAL ---")
# Verificamos que el pan bajó de 10 a 7
print(f"Producto: {producto1.nombre} | Stock final: {producto1.stock}")