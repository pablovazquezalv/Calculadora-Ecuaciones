import sympy as sp

#UNA ECUACIÓN DIFERENCIAL ORDINARIA DE PRIMER ORDEN SE PUEDE EXPRESAR COMO:
#dy/dx = f(x)*g(x)
#dy/dx = f(x)/g(y)
#dy/dx = g(y)/f(x)

#definir la variable dependiente
y = sp.Function('y')
x = sp.symbols('x')

#definir la función dependiente
func_dependiente = 3*x**2






#print(f"La función dependiente es: {func_dependiente}")

# #resolver con sympy
# solucion = sp.integrate(func_dependiente, x)
# print(f"La solución de la integral es: {solucion}")

#definir la funcion independiente
func_independiente = 8*y

#print(f"{func_dependiente} = {func_independiente}")
print(f"{sp.pretty(func_dependiente)} = {func_independiente} = 0")
#resolver con sympy
# solucion = sp.integrate(func_independiente, y)
# print(f"La solución de la integral es: {solucion}")

#separar variables
#definir la ecuación diferencial
