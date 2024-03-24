class Menu:
    def __init__(self):
        pass

    @staticmethod
    def mostrar_menu():
        print("***** Menú de Métodos de Ecuaciones Diferenciales 8 A *****")
        print("1. Método de Variables Separables")
        print("2. Método de Ecuaciones Diferenciales Homogéneas")
        print("3. Método de Ecuaciones Diferenciales No Homogéneas con Coeficientes Constantes")
        print("4. Método de Ecuaciones Diferenciales Metodo Miaw")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion

    