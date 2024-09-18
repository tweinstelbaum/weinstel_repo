import re
emails = [
    "usuario1@gmail.com",
    "usuario2@gmail.com",
    "usuario3@gmail.com"
]

# Lista de teléfonos
telefonos = [
    "123-456-7890",
    "234-567-8901",
    "345-678-9012"
]

# Lista de códigos postales
codigos_postales = [
    "10001",
    "10002",
    "10003"
]


# Lista de fechas
fechas = [
    "01/01/2023",
    "12/12/2022",
    "05/07/2021"
]


mail = input("Ingrese su mail: ")
tel = input("Ingrese su teléfono: ")
pos = input("Ingrese su código postal: ")
fecha = input("Ingrese una fecha en formato dd/mm/yyyy: ")

def validacion():
    
    patron_mail = "[a-zA-Z0-9._%+-]+@[gmail]+\.[com]{3}"  
    busqueda_mail = re.match(patron_mail, mail)
    
    if busqueda_mail and mail in emails:
        print("Mail autorizado")
    else:
        print("Mail no autorizado o inválido")

    
    patron_tel = "\d{3}-\d{3}-\d{4}"  
    busqueda_tel = re.match(patron_tel, tel)
    
    if busqueda_tel and tel in telefonos:
        print("Teléfono autorizado")
    else:
        print("Teléfono no autorizado o inválido")
    
    
    patron_pos = "\d{5}"  
    busqueda_pos = re.match(patron_pos, pos)
    
    if busqueda_pos and pos in codigos_postales:
        print("Código postal autorizado")
    else:
        print("Código postal no autorizado o inválido")
    
    
    patron_fecha = "\d{2}/\d{2}/\d{4}"  
    busqueda_fecha = re.match(patron_fecha, fecha)
    
    if busqueda_fecha and fecha in fechas:
        print("Fecha autorizada")
    else:
        print("Fecha no autorizada o inválida")


validacion()

