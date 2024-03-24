import sympy as sp 
from sympy import symbols, Function, Eq, dsolve

class EcuacionHomogenea:

    def __init__(self):
        pass


    def resolver(self):
        print("Para resolver ecuaciones diferenciales homogéneas de primer orden, sigue estos pasos:")
        print("\n1. Escribe la ecuación diferencial en la forma estándar:")
        print("   La forma estándar es: dy/dx = f(x, y)")

        print("\n2. Identifica la función f(x, y):")
        print("   Esta función, f(x, y), es la del lado derecho de la ecuación.")
        print("   En ecuaciones homogéneas, f(x, y) debe cumplir la propiedad:")
        print("   f(tx, ty) = t^n * f(x, y), donde t es un factor constante.")
        print("   Si esta propiedad se cumple, la ecuación es homogénea.")

        print("\n3. Encuentra la solución general:")
        print("   Para resolver la ecuación, intenta encontrar una función y(x) que la satisfaga.")
        print("   Se pueden utilizar métodos como separación de variables, sustituciones o variables auxiliares.")
        print("   Aplica el método adecuado según la forma de f(x, y).")

        print("\n4. Aplica condiciones iniciales (si es necesario):")
        print("   Si tienes condiciones iniciales dadas, como y(x0) = y0,")
        print("   puedes usarlas para encontrar una solución particular que satisfaga estas condiciones.")

        print("\n5. Verifica la solución:")
        print("   Una vez que encuentres una solución, verifica que cumpla la ecuación diferencial original.")
        print("   Sustituye la solución en la ecuación y comprueba que se cumpla para todos los valores de x.")

        print("\n6. Ejemplo de ecuación homogénea:")
        print("   dy/dx = (2x + y) / (x + y)")
        print("   Esta ecuación es homogénea porque f(tx, ty) = t * f(x, y) se cumple.")
        print("   Puedes resolverla utilizando métodos de variables separables o sustituciones adecuadas.")

        print("Deseas volver al menu principal")
        print("1.- Si")
        print("2.- No")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            return
        else:
            exit()

if __name__ == "__main__":
    ecuacion = EcuacionHomogenea()
    ecuacion.resolver()