import sympy as sp
import re

class EcuacionNoHomogeneaM:

    def __init__(self):
        pass

    def validar_formato_Y(self, valor):
        # Expresión regular para validar el formato
        patron = r'^-?\d+\*x\*\*\d+$'
        if re.match(patron, valor):
            return True
        else:
            return False

    def metodo(self):
        print("*** Ecuaciones diferenciales no homogéneas ***")
        print("")
        # Mostrar la fórmula de la ecuación no homogénea
        print("La ecuación no homogénea tiene la forma: y' + P(x)y = Q(x)")
        print("\n")
        # Explicar el proceso al usuario
        print("Por favor ingrese las funciones en el formato 'ax^n'")
        print("\n")

        # Validar la función Y(x)
        while True:
            self.Y = input("Ingrese la función Y(x):")
            if self.validar_formato_Y(self.Y):
                break
            else:
                print("El formato de la función Y(x) es incorrecto, debe ser de la forma: ax^n")

        # Validar la función P(x)
        while True:
            self.P = input("Ingrese la función P(x):")
            #P(x) = 2*x**2
            if self.validar_formato_Y(self.P):
                break
            else:
                print("El formato de la función P(x) es incorrecto, debe ser de la forma: ax^n")

        # Validar la función Q(x)
        while True:
            self.Q = input("Ingrese la función Q(x):")
            if self.validar_formato_Y(self.Q):
                break
            else:
                print("El formato de la función Q(x) es incorrecto, debe ser de la forma: ax^n")

        # Mostrar las funciones ingresadas por el usuario
        print("\n")
        print("Los valores de las funciones son:")
        print(f"Y(x) = {self.Y}")
        print(f"P(x) = {self.P}")
        print(f"Q(x) = {self.Q}")
        print("\n")

        # Mostrar la ecuación no homogénea
        print("La ecuación no homogénea es:")
        print(f"y' + {self.P} = {self.Q}")
        print("-" * 20)
        print(f"   + {self.Y}  {self.Y}")
        print("\n")

        # Simplificar P(x) y Q(x) dividiendo por Y(x)
        P_simplificado = sp.sympify(self.P) / sp.sympify(self.Y)
        Q_simplificado = sp.sympify(self.Q) / sp.sympify(self.Y)
        P_simplificado = P_simplificado.subs('y', 1)

        print("Después de simplificar la ecuación, se obtiene:")
        print("\n")
        print(f"y' + {P_simplificado} = {Q_simplificado}")
        print("\n")

        # Integrar P(x) con respecto a x
        print("Después de integrar la ecuación, se obtiene:")
        x = sp.symbols('x')
        M = sp.symbols('M')
        M = sp.exp(sp.integrate(P_simplificado, x))
        print(f"M es igual a: {M}")

        # MY = ∫M*Q(x)dx
        print(f"{M}Y = ∫{M}*{Q_simplificado}dx")
        print("\n")
        # Multiplicar M por Q(x)
        MQ = M * Q_simplificado
        print(f"{M} y = {MQ} dx")

        # Integrar MY
        print("\n")
        print(f"Y = ∫{MQ}dx")
        print("\n")

        Y = sp.integrate(MQ, x)
        print(f"Y = {Y} + C")

        #preguntar si desea continuar o regresar al menú principal
        print("\n")
        print("Desea continuar con otra ecuación no homogénea?")
        print("1. Sí")
        print("2. No")
        opcion = input("Seleccione una opción:")    
        if opcion == "1":
            self.metodo()
        else:
            return
        


if __name__ == "__main__":
    ecuacion = EcuacionNoHomogeneaM()
    ecuacion.metodo()
