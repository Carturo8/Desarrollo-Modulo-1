"""
Un sistema de seguridad para el hogar necesita monitorear posibles intrusiones bajo estas condiciones:

    Se detecta movimiento en el interior de la propiedad (activado por sensores).

    Además, debe cumplirse al menos una de estas situaciones:

        Alguna ventana está abierta o

        Es horario nocturno (entre las 10 PM y 6 AM)

Cuando ambas condiciones principales se cumplen, se activa la alarma; en cualquier otro caso, el sistema permanece en estado seguro.
"""

# Variables
movimiento = True
ventana_abierta = True
hora_noche = False

# Operadores lógicos
if movimiento == True and (ventana_abierta == True or hora_noche == True):
    print("¡ALARMA! 🚨")
else:
    print("Todo seguro 🔒")