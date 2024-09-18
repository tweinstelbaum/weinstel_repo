# Lista de productos como lista de diccionarios
productos = [
    {'id': 'P001', 'nombre': 'Televisor', 'precio': 30000, 'cantidad': 10},
    {'id': 'P002', 'nombre': 'Refrigerador', 'precio': 50000, 'cantidad': 5},
]

crear_producto = lambda producto: productos.append(producto)
leer_productos = lambda: productos
actualizar_producto = lambda id_producto, nuevos_datos: [prod.update(nuevos_datos) for prod in productos if prod['id'] == id_producto]
eliminar_producto = lambda id_producto: productos[:] = [prod for prod in productos if prod['id'] != id_producto]

crear_producto({'id': 'P003', 'nombre': 'Laptop', 'precio': 40000, 'cantidad': 7})
print("Productos después de agregar:", leer_productos())
actualizar_producto('P001', {'precio': 35000, 'cantidad': 12})
print("Productos después de actualizar:", leer_productos())
eliminar_producto('P002')
print("Productos después de eliminar:", leer_productos())

# Lista de productos como lista de listas
productos_matriz = [
    ['P001', 'Televisor', 30000, 10],
    ['P002', 'Refrigerador', 50000, 5],
]

def crear_producto_matriz(producto):
    productos_matriz.append(producto)

def leer_productos_matriz():
    return productos_matriz

def actualizar_producto_matriz(id_producto, nuevos_datos):
    for i in range(len(productos_matriz)):
        if productos_matriz[i][0] == id_producto:
            productos_matriz[i] = nuevos_datos
            return

def eliminar_producto_matriz(id_producto):
    productos_matriz[:] = [prod for prod in productos_matriz if prod[0] != id_producto]

crear_producto_matriz(['P003', 'Laptop', 40000, 7])
print("Productos (matriz) después de agregar:", leer_productos_matriz())
actualizar_producto_matriz('P001', ['P001', 'Televisor', 35000, 12])
print("Productos (matriz) después de actualizar:", leer_productos_matriz())
eliminar_producto_matriz('P002')
print("Productos (matriz) después de eliminar:", leer_productos_matriz())