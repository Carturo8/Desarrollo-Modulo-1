servidor = "www.riwi.com/BD"
puerto = "3080"
n_bd = "Prueba1"
nombre_usuario = "Admin"
contraseña = "Ingreso20*"

url_correcta = servidor + ":" + puerto + "/" + n_bd + "/" + "Nombre_Usuario:" + nombre_usuario + "&" + "Contraseña:" + contraseña
print("URL correcta: " + url_correcta)

pedir_servidor = str(input("Ingrese el servidor: "))
pedir_puerto = str(input("Ingrese el puerto: "))
pedir_bd = str(input("Ingrese el nombre de la base de datos: "))
pedir_usuario = str(input("Ingrese el nombre de usuario: "))
pedir_contraseña = str(input("Ingrese la contraseña: "))
url_ingresada = pedir_servidor + ":" + pedir_puerto + "/" + pedir_bd + "/" + "Nombre_Usuario:" + pedir_usuario + "&" + "Contraseña:" + pedir_contraseña
print("URL ingresada: " + url_ingresada)

if url_correcta == url_ingresada:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    print("La URL solicitada no coincide con la URL correcta.")
    print("Por favor, verifique los datos ingresados.")