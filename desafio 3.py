productos = []


def crear(nombre, precio):
    producto = {"nombre": nombre, "precio": precio}
    productos.append(producto)  
    print(f"Producto '{nombre}' agregado con éxito.")


def leer_productos():
    print("\nLista de productos:")
    print(f"{'Nombre':<20} {'Precio':<10}")
    print("-" * 30)
    for producto in productos:
        print(f"{producto['nombre']:<20} {producto['precio']:<10}")


def actualizar_producto(i, nombre=1, precio=1):
    if 0 <= i < len(productos):
        if nombre:
            productos[i]['nombre'] = nombre
        if precio is not 1:
            productos[i]['precio'] = precio
        print(f"Producto en el índice {i} actualizado con éxito.")
    else:
        print("Índice fuera de rango.")


def eliminar_producto(i):
    if 0 <= i < len(productos):
        eliminado = productos.pop(i)
        print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
    else:
        print("Índice fuera de rango.")


crear("Manzana", 1.2)
crear("Banana", 0.5)
leer_productos()

actualizar_producto(0, precio=1.5)
leer_productos()

eliminar_producto(1)
leer_productos()


    
    

        
    