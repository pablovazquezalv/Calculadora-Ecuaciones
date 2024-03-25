from Menu import Menu
from NoHomogeneasM import EcuacionNoHomogeneaM
from NoHomogeneasCoeficientes import NoHomogeneaCoeficiente
from VariableSeparables import VariableSeparables
from EcuacionHomogenea import EcuacionHomogenea


#PABLO VAZQUEZ ALVARADO 8A
#UNIVERSIDAD TECONOLOGICA DE TORREON
#INGENIERIA EN DESARROLLO Y GESTION DE SOFTWARE
#MATERIA: MATEMATICAS PARA INGENIERIA
#PROFESOR: DANIEL ROSALES MIRON



if __name__ == "__main__":
    menu = Menu()
    opcion = ""
    while opcion != "5":
        opcion = menu.mostrar_menu()
        if opcion == "1":
            print("Seleccionó el método de Variables Separables")
            vs = VariableSeparables()
            vs.resolverVariablesSeparables()
        elif opcion == "2":
            print("Seleccionó el método de Ecuaciones Diferenciales Homogéneas")
            ecuacion = EcuacionHomogenea()
            ecuacion.resolver_ecuacion()
        elif opcion == "3":
            print("Seleccionó el método de Ecuaciones Diferenciales No Homogéneas con Coeficientes Constantes")
            noHomogeneasC = NoHomogeneaCoeficiente()
            noHomogeneasC.metodo()
        elif opcion == "4":
            print("Seleccionó el método de Ecuaciones Diferenciales Metodo Miaw")
            noHomogeneasM = EcuacionNoHomogeneaM()
            noHomogeneasM.metodo()
