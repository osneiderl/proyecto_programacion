from datetime import datetime 
import os
print("::::::::::::::::::::::::::BIENVENIDOS AL SITIO OFICIAL DE BOLETERIAS:::::::::::::::::::::")
compras_realizadas = []
apuestas_realizadas = []
usuarios_registrados = []
cantidad_boletas_vendidas=[]
partidos = {
    "Partido 1": {
        "fecha": "15/04/2023",
        "equipo_local": "Barcelona",
        "equipo_visitante": "Real Madrid",
        "estadio": "camp nou",
        "precio_boleta": 350000
    },
    "Partido 2": {
        "fecha": "22/04/2023",
        "equipo_local": "Real Madrid",
        "equipo_visitante": "Valencia",
        "estadio": "Santiago Bernabéu",
        "precio_boleta": 200000
    },
    "Partido 3": {
        "fecha": "29/04/2023",
        "equipo_local": "Barcelona",
        "equipo_visitante": "Atletico Madrid",
        "estadio": "camp nou",
        "precio_boleta": 230000
    }
}


while True:
    print("::::::::::::::::::::::::::MENU::::::::::::::::::::::::::::")
    print("| 1. Comprar boletas                                     |")
    print("| 2. Hacer apuestas                                      |")
    print("| 3. ver compras                                         |")
    print("| 4. ver apuestas                                        |")
    print("| 5. cantidad de boletas vendidas                        |")
    print("| 6. mostrar usuarios registrados                        |")
    print("| 7. Salir                                               |")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    opcion = input("Ingrese la opción que desea escoger: ")
    os.system("cls")
    if opcion == "1":
        print("CALENDARIOS DE LOS PARTIDOS:")
        for partido, detalles in partidos.items():
          print(f"{partido}: {detalles['fecha']} - {detalles['equipo_local']} vs {detalles['equipo_visitante']}")
        try:
         partido_seleccionado = int(input("Seleccione un partido: "))
         if partido_seleccionado not in [1, 2, 3]:
           print("No existe esa opcion")
           continue
         print(f"¡Usted ha seleccionado ir a ver el partido {partido_seleccionado}!")
        except ValueError:
          print("Debe ingresar un número válido para seleccionar el partido.")
          continue
        if partido_seleccionado not in [1, 2, 3]:
            print("No hay partidos disponibles.")
            continue
        print("Para comprar la boleta primero necesita ingresar sus datos.")
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <18:
                print("No cumples con la edad requerida.")
                continue
            cedula = float(input("Ingrese su número de cédula: "))
            nombre = input("Ingrese su nombre completo: ")
            telefono = int(input("Ingrese su número de teléfono: "))
            correo_electronico = input("Ingrese su correo electrónico: ")
            cantidad_boletas = int(input("Ingrese la cantidad de boletas que desea comprar: "))
            if cantidad_boletas <= 0:
              print("Debe comprar al menos una boleta.")
              continue
        except ValueError:
            print("datos como se solicitan")
            continue
        confirmacion = input("¿Desea confirmar la compra? (1/2): ")
        if confirmacion == "1":
           usuario = {
            "cedula": cedula,
            "nombre": nombre,
            "telefono": telefono,
            "correo_electronico": correo_electronico,
            "partido": partido_seleccionado,
            "cantidad_boletas": cantidad_boletas,
            "fecha_compra": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           }
           compras_realizadas.append(usuario)
           usuarios_registrados.append(usuario)
           detalles_partido = partidos[f"Partido {partido_seleccionado}"]
           print(f"\nDetalle del partido {partido_seleccionado}:")
           print(f"Fecha: {detalles_partido['fecha']}")
           print(f"Equipo local: {detalles_partido['equipo_local']}")
           print(f"Equipo visitante: {detalles_partido['equipo_visitante']}")
           print(f"Estadio: {detalles_partido['estadio']}")
           print(f"Precio de la boleta: ${detalles_partido['precio_boleta']}")
           print(f"{detalles_partido['equipo_local']} vs {detalles_partido['equipo_visitante']}")
           precio_boleta = detalles_partido['precio_boleta']
           sector = input("¿En qué sector del estadio desea estar? ( 1. lado oeste/ 2. norte / 3.noroeste /4 sur): ")
           if sector=="1":
               asiento="sector 10, fila 15, asiento 3"
               print("Usted ha elegido el sector lado oeste.")
               print(asiento)
           elif sector=="2":
              asiento="sector 12, fila 5, asiento 13"
              print("Usted ha elegido el sector norte.")
              print(asiento)
           elif sector=="3":
              asiento="sector 65, fila 24, asiento 120"
              print("Usted ha elegido el sector noroeste.")
              print(asiento)
           elif sector=="4":
               asiento="sector 25, Fila 12, Asiento 8"
               print("Usted ha elegido el sector sur.")
               print(asiento)
           else:
              print("opcion no existe ")
              continue
           total_a_pagar = precio_boleta * cantidad_boletas
           usuario={"total_a_pagar": total_a_pagar,}
           print(f"El total a pagar es de ${total_a_pagar}")
        elif confirmacion=="2":
            print("gracias por visitarnos. vuelva pronto")
            continue  
        else:
            print("no existe esa opcion")
            continue
        while True: 
                print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                print("::::::::::::::::::::::::: BOLETA :::::::::::::::::::::::")
                print("Fecha de compra :" , datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                print("Partido         : " , detalles_partido["equipo_local"], "vs", detalles_partido["equipo_visitante"])
                print("Estadio         :",detalles_partido["estadio"])
                print("Fecha  partido  :",detalles_partido["fecha"])
                print("Asiento         :" ,asiento)
                print("Precio boleta   :", precio_boleta, "pesos")
                print("Nombre          :", nombre,   "::" "Cédula:", cedula)
                print("Teléfono        :", telefono     , "::""correo electronico:",correo_electronico)
                print("cantidad_boletas:",cantidad_boletas, "::""total_a_pagar:", total_a_pagar)
                print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 
                break
        print("compra correctamente exitosa")
        
    elif opcion=="2":
        os.system("cls")
        print("CALENDARIOS DE LOS PARTIDOS EN QUE SE YO:")
        for partido, detalles in partidos.items():
           print(f"{partido}: {detalles['fecha']} - {detalles['equipo_local']} vs {detalles['equipo_visitante']}")
        try:
           partido_seleccionado = int(input("Seleccione un partido: "))
           if partido_seleccionado not in [1, 2, 3]:
             print("No existe esa opcion")
             continue
           print(f"¡Usted ha seleccionado apostar por el partido {partido_seleccionado}!")
        except ValueError:
          print("Debe ingresar un número válido para seleccionar el partido.")
          continue
        if partido_seleccionado not in [1, 2, 3]:
           print("No hay partidos disponibles.")
           continue
        print("Para hacer la apuesta primero necesita ingresar sus datos.")
        try:
           edad = int(input("Ingrese su edad: "))
           if edad <18:
             print("No cumples con la edad requerida.")
             continue
        
           cedula = float(input("Ingrese su número de cédula: "))
           nombre = input("Ingrese su nombre completo: ")
           telefono = int(input("Ingrese su número de teléfono: "))
           correo_electronico = input("Ingrese su correo electrónico: ")
           cantidad_apuesta = float(input("Ingrese la cantidad de dinero que desea apostar: "))
           if cantidad_apuesta <= 0:
             print("Debe apostar al menos un peso.")
             continue
        except ValueError:
           print("Datos como se solicitan")
           continue
        confirmacion = input("¿Desea confirmar la apuesta? (1/2): ")
        if confirmacion.lower()== "1":
           usuario = {
              "cedula": cedula,
              "nombre": nombre,
              "telefono": telefono,
              "correo_electronico": correo_electronico,
              "partido": partido_seleccionado,
              "cantidad_apuesta": cantidad_apuesta,
              "fecha_apuesta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
           apuestas_realizadas.append(usuario)
           usuarios_registrados.append(usuario)
           detalles_partido = partidos[f"Partido {partido_seleccionado}"]
           print(f"\nDetalle del partido {partido_seleccionado}:")
           print(f"Fecha: {detalles_partido['fecha']}")
           print(f"Equipo local: {detalles_partido['equipo_local']}")
           print(f"Equipo visitante: {detalles_partido['equipo_visitante']}")
           print(f"Estadio: {detalles_partido['estadio']}")
           print(f"Precio de la boleta: ${detalles_partido['precio_boleta']}")
           print(f"{detalles_partido['equipo_local']} vs {detalles_partido['equipo_visitante']}")
           print(f"Usted ha apostado ${cantidad_apuesta} por el equipo {detalles_partido['equipo_local']}. ¡Mucha suerte!") 
        if confirmacion.lower()=="2":
           print("gracias por entrar a nuestro sitio")
        else:
           print("gracias.vuelve pronto")
           continue
    elif opcion == "3":
        os.system("cls")
        print("Compras realizadas:")
        if len(compras_realizadas) == 0:
            print("No se han realizado apuestas todavía.")
        for compra in compras_realizadas:
            print(f"\nCedula: {compra['cedula']}")
            print(f"Nombre: {compra['nombre']}")
            print(f"Telefono: {compra['telefono']}")
            print(f"Correo electrónico: {compra['correo_electronico']}")
            print(f"Partido: {compra['partido']}")
            print(f"Cantidad de boletas: {compra['cantidad_boletas']}")
            print(f"Fecha de compra: {compra['fecha_compra']}")
            print(f"------------------------------------------------------------")
    elif opcion=="4":
        print("APUESTAS REALIZADAS:")
        if len(apuestas_realizadas) == 0:
            print("No se han realizado apuestas todavía.")
        else:
            for apuesta in apuestas_realizadas:
                print(f"Apuesta realizada por {apuesta['nombre']} con cédula {apuesta['cedula']}:")
                detalles_partido = partidos[f"Partido {apuesta['partido']}"]
                print(f" Partido: {detalles_partido['equipo_local']} vs {detalles_partido['equipo_visitante']}")
                print(f"Fecha: {detalles_partido['fecha']}")
                print(f"Cantidad apostada: ${apuesta['cantidad_apuesta']}")
                print(f"Fecha de apuesta: {apuesta['fecha_apuesta']}")
                print(f"-------------------------------------------------------------------------------------")
                continue
    elif opcion=="5":
           total_boletas_vendidas = sum([compra["cantidad_boletas"] for compra in compras_realizadas])
           print(f"Se han vendido un total de {total_boletas_vendidas} boletas.")
    elif opcion=="6":
        os.system("cls")
        print("Usuarios registrados:")
        if len(usuarios_registrados) == 0:
            print("No se han realizado apuestas todavía.")
        for usuario in usuarios_registrados:
            print(f"Cédula: {usuario['cedula']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Teléfono: {usuario['telefono']}")
            print(f"Correo electrónico: {usuario['correo_electronico']}")
            print("---------------------------------------------------")
            continue
    elif opcion=="7":
        print("has elegido salir del programa. hasta pronto")
        exit()
    else:
        print("esa opcion no se encuentra")  
        continue
    