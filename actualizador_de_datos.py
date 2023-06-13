from almacenador_de_datos import almacenador

class actualizar_datos:
    def __init__(self):
        pass
    
    def pedir_actualizar_edad(self):
        print("\n#### Actualizador de datos ####")
        print("INGRESA lo que se te pida...\n")

        datos= almacenador.mostrar_datos_almacenados()
        print("Tus datos son:")
        print(datos, "\n")

        print("¿Ah quien se le actualizara?")
        nombre_buscado= input("Nombre de la persona: ").capitalize()
        anios= int(input("¿Cuantos años?: "))
        if nombre_buscado in datos:
            datos[nombre_buscado] += anios
            print(f"\n*** Actualizacion: Nombre: {nombre_buscado}, Edad: {datos[nombre_buscado]} ***")
        else:
            print(f"\n***El nombre '{nombre_buscado}' no esta en esta lista.***")

#Definiendo el objeto
actualizador= actualizar_datos()