from almacenador_de_datos import almacenador
from actualizador_de_datos import actualizador

class cuerpo_programa:
    def __init__(self):
        self.datos= almacenador.mostrar_datos_almacenados()
        self.opcion_uno= "Almacenar datos"
        self.opcion_dos= "Actualizar datos"
        self.opcion_tres= "Ver datos"
        self.opcion_cuatro= "Salir"

    def menu(self):
        print(f"1 - {self.opcion_uno}")
        print(f"2 - {self.opcion_dos}")
        print(f"3 - {self.opcion_tres}")
        print(f"4 - {self.opcion_cuatro}")

#Definiendo el objeto
programa= cuerpo_programa()

'''Main'''

while True:

    print("\n##### Pequeño Gestor de Datos #####")
    print("INGRESA lo que se te pida...\n")

    programa.menu()
    opcion_menu= int(input("Numero de opcion: "))
    if opcion_menu == 1:
        almacenador.pedir_almacenar_datos()
    elif opcion_menu == 2:
        actualizador.pedir_actualizar_edad()
    elif opcion_menu == 3:

        print("\n#### Vista de los datos ####\n")
        for nombre, edad in almacenador.mostrar_datos_almacenados().items():
                print(f"Nombre: {nombre}, Edad: {edad}")
                
    elif opcion_menu == 4:
        break
    else:
        print("\n***Opcion no valida!***\n")
