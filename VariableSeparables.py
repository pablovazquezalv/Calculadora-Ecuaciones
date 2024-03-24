from sympy import symbols, Function, Eq, dsolve, Derivative, simplify, sympify, pretty
from sympy.abc import x
import sympy as sp
import re

class VariableSeparables:

    def __init__(self):
        pass
        
    def validarLadoIzquierdo(self, valor):
        if valor == "dy/dx":
            return True
        else:
            return False  
        
    def validarLadoDerecho(self, valor):
        patron = r'^-?\d+\*x\*\*\d+$'
        if re.match(patron, valor):
            return True
        else:
            return False
    
    def validarVariableDependiente(self, valor):
        #un patron que acepte solo letras y que sea solo una letra
        patron = r'^[a-zA-Z]$'
        if re.match(patron, valor):
            return True
        else:
            return False
        
    def validarFloat(self, valor):
        if valor.isnumeric():
            return True
        else:
            return False
        
    def resolverVariablesSeparables(self):
        print("*** METODO DE VARIABLES SEPARABLES ***")
        print("")
        print("La ecuación diferencial ordinaria de primer orden se puede expresar como:")
        print("dy/dx = f(x)*g(x)")
        print("dy/dx = f(x)/g(y)")
        print("dy/dx = g(y)/f(x)")
        print("")
        print("Para resolver la ecuación diferencial, se debe separar las variables y luego integrar ambos lados.")

        # Pedir al usuario que ingrese los lados de la ecuación diferencial
        #Derivative(y(x), x) = -x/y(x) es igual a dy/dx 
        #explicar el formato de la ecuación diferencial
        print("Por favor, ingresa la ecuación diferencial ordinaria de primer orden en la forma:")
        print("Lado izquierdo = Lado derecho")


        #si escribe dy/dx = -x/y(x) es Derivative(y(x), x) 
        lhs_str = input("Ingresa el lado izquierdo de la ecuacion (ejemplo, 'dy/dx'): ")

        while True:
            if self.validarLadoIzquierdo(lhs_str):
                break
            else:
                print("El formato del lado izquierdo es incorrecto, debe ser de la forma: dy/dx")
                lhs_str = input("Ingresa el lado izquierdo de la EDO (ejemplo, 'dy/dx'): ")

        if lhs_str == "dy/dx":
            lhs_str = "Derivative(y(x), x)"

        rhs_str = input("Ingresa el lado derecho de la ecuacion (ejemplo, '-x/y(x) o 3*x**2'): ")


        while True:
            if self.validarLadoDerecho(rhs_str):
                break
            else:
                print("El formato del lado derecho es incorrecto, debe ser de la forma: -x/y(x) o 3*x**2")
                rhs_str = input("Ingresa el lado derecho de la ecuacion (ejemplo, '-x/y(x) o 3*x**2'): ")
        # Pedir al usuario que ingrese la variable dependiente 
                       
        print("")
        print("Listo, se ha ingresado la ecuación diferencial: ")
        print(f"La ecuación diferencial es: dy/dx = {rhs_str}")
        print("")
        print("Por favor, ingresa la variable dependiente de la ecuación diferencial.")
        print("Por ejemplo, si la ecuación es dy/dx = y*x, la variable dependiente es 'y'.")
        print("Si la ecuación es dy/dx = -x/y, la variable dependiente es 'y'.")
        #explicar cual por que es la variable dependiente
        print("La variable dependiente es la función que deseas encontrar. Por favor, ingrésala.")
        print("Por ejemplo, si la ecuación es dy/dx = y*x, la variable dependiente es 'y'.")
        print("porque queremos encontrar la función y(x).")
        print("")
       
        while True:
            dependiente = input("Ingresa la variable dependiente de la ecuación diferencial: ")
          
            
            if dependiente.isalpha():
                break
            else:
                print("La variable dependiente debe ser una letra, por ejemplo 'y'.")
                print("Por favor, ingrésala nuevamente.")

        try:
            y = Function(dependiente)
            lhs = sympify(lhs_str, locals={'y': y, 'x': x, 'Derivative': Derivative})
            rhs = sympify(rhs_str, locals={'y': y, 'x': x})
            edo = Eq(lhs, rhs)
        except Exception as e:
            print(f"Error interpretando la ecuación: {e}. Asegúrate de usar el formato correcto.")
            return

        print("¿Deseas aplicar condiciones iniciales? (s/n): ")
        aplicar_condiciones = input().lower() == 's'
        condiciones = {}

        if aplicar_condiciones:
                condicionx = input("Ingresa el valor de condicion inicial en x (x,y): ")
                while True:
                    if self.validarFloat(condicionx):
                        break
                    else:
                        print("El valor de la condición inicial en x debe ser un número.")
                        condicionx = input("Ingresa el valor de la condición inicial en x (x,y): ")
                
                while True:
                    condiciony = input("Ingresa el valor de la condición inicial en y (x,y)")
                    if self.validarFloat(condiciony):
                        break
                    else:
                        print("El valor de la condición inicial en y debe ser un número.")

              
                # Convertir los valores de las condiciones iniciales a números
                condicionx_num = float(condicionx)
                condiciony_num = float(condiciony)
                condiciones = {y(x).subs(x, condicionx_num): condiciony_num}
            
        #Resolver la ecuación diferencial
        try:
            solucion = dsolve(edo, y(x), ics=condiciones)
            print("Para resolver la ecuación diferencial, se debe separar las variables y luego integrar ambos lados.")
            print("\n")
            print("en tu caso lo que se hizo fue:")
            print("1. Separar las variables")
            print("2. Integrar ambos lados")
            print("3. Simplificar la solución")
            print("\n")
            print("Solución:")
            print(pretty(solucion))

            print("\n")
            print("Desea resolver otra ecuación diferencial? (s/n): ")
            resolver_otra = input().lower() == 's'
            if resolver_otra:
                self.resolverVariablesSeparables()
            else:
                return

        except Exception as e:
            print(f"No se pudo resolver la EDO: {e}")


if __name__ == "__main__":
    vs = VariableSeparables()
    vs.resolverVariablesSeparables()