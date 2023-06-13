class almacenar_datos:
    def __init__(self):
        self.datos= {}
    
    def pedir_almacenar_datos(self):
        print("\n#### Registro de datos ####")
        print("INGRESA lo que se te pida...\n")

        nombre= input("Nombre: ").capitalize()
        edad= int(input("Edad: "))

        if 1 < edad < 100:
            self.datos[nombre]= edad
        else:
            print(f"La edad {edad} no es admitida!")
    
    def mostrar_datos_almacenados(self):
        return self.datos

#Definiendo el objeto
almacenador= almacenar_datos()