usuarios = []

crear_usuario = lambda usuario: usuarios.append(usuario)
leer_usuarios = lambda: usuarios

actualizar_usuario = lambda indice, nuevo_usuario: usuarios[indice].update(nuevo_usuario)

eliminar_usuario = lambda indice: usuarios.pop(indice)

crear_usuario({"nombre": "Juan", "edad": 30})
crear_usuario({"nombre": "Ana", "edad": 25})

print("Usuarios:", leer_usuarios())

actualizar_usuario(0, {"nombre": "Juan", "edad": 31})

print("Usuarios después de actualizar:", leer_usuarios())
eliminar_usuario(1)

print("Usuarios después de eliminar:", leer_usuarios())