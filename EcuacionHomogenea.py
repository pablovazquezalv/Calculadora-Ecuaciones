import sympy as sp

def resolver_ecuacion(ecuacion_input):
    print("*** Ecuaciones diferenciales homogéneas ***") 
    print("Para resolver ecuaciones diferenciales homogéneas de primer orden, sigue estos pasos:")
    print("\n1. Escribe la ecuación diferencial en la forma estándar:")
    print("La forma estándar es: dy/dx = f(x, y)")

    print("\n2. Identifica la función f(x, y):")
    print("   Esta función, f(x, y), es la del lado derecho de la ecuación.")
    print("   En ecuaciones homogéneas, f(x, y) debe cumplir la propiedad:")
    print("   f(tx, ty) = t^n * f(x, y), donde t es un factor constante.")
    print("   Si esta propiedad se cumple, la ecuación es homogénea.")

    print("\n3. Encuentra la solución general:")
    print("   Para resolver la ecuación, intenta encontrar una función y(x) que la satisfaga.")
    print("   Se pueden utilizar métodos como separación de variables, sustituciones o variables auxiliares.")
    print("   Aplica el método adecuado según la forma de f(x, y).")

    print("\n4. Verifica la solución:")
    print("   Una vez que encuentres una solución, verifica que cumpla la ecuación diferencial original.")
    print("   Sustituye la solución en la ecuación y comprueba que se cumpla para todos los valores de x.")

    print("\n5. Ejemplo de ecuación homogénea:")
    print("   dy/dx = (2x + y) / (x + y)")
    print("   Esta ecuación es homogénea porque f(tx, ty) = t * f(x, y) se cumple.")
    print("   Puedes resolverla utilizando métodos de variables separables o sustituciones adecuadas.")
    # Definir la variable simbólica y la función
    x = sp.Symbol('x') 
    y = sp.Function('y')(x)
    
    # Convertir la ecuación a un objeto SymPy
    ecuacion = sp.sympify(ecuacion_input)
    
    # Reescribir la ecuación como una ecuación diferencial
    ecuacion_diferencial = sp.Eq(sp.Derivative(y, x), ecuacion)
    
    # Mostrar la ecuación ingresada
    print("Ecuación ingresada:")
    print(sp.pretty(ecuacion_diferencial))
    
    # Resolviendo la ecuación
    solucion = sp.dsolve(ecuacion_diferencial, y)
    
    # Mostrar la solución
    print("Lo que se hizo fue resolver la ecuación diferencial homogénea de primer orden: dy/dx = f(x, y)")
    print("haciendo que las derivadas de y sean iguales a la ecuación diferencial ingresada")
    
    print("\nSolución:")
    print(solucion)

# Solicitar la ecuación al usuario
ecuacion_input = input("Ingrese la ecuación en términos de x e y(x): ")

# Llamar a la función para resolver la ecuación ingresada por el usuario
resolver_ecuacion(ecuacion_input)
