import sympy as sp
import re

class NoHomogeneaCoeficiente:

    def __init__(self):
        pass

    def validar_numero(self, mensaje):
        patron = r'^-?\d+$'
        if re.match(patron, mensaje):
            return True
        else:
            return False

    def metodo(self):
        print("*** Ecuaciones diferenciales diferenciales con Coeficientes ***")
        print("\n")
        print("Este programa resuelve ecuaciones diferenciales no homogéneas de segundo orden con coeficientes constantes.")
        
        print("La ecuacion tiene la forma: y'' + p(x)y' + q(x)y = f(x)")
        print("por ejemplo: y'' + 2y' + 2y = 2x² + 3x + 4")
        print("\n")
        
        #VALIDAR LOS COEFICIENTES DEL LADO IZQUIERDO
        while True:
            self.yizq = input("Ingresa el coeficiente de y': ")

            if self.validar_numero(self.yizq):
                self.yizq = int(self.yizq)
                break
            else:
                print("Error: Ingresa solo números enteros.")

        while True:
            self.independienteizq = input("Ingresa el coeficiente independiente: ")
            if self.validar_numero(self.independienteizq):
                self.independienteizq = int(self.independienteizq)
                break
            else:
                print("Error: Ingresa solo números enteros.")


        print(f"La ecuacion tiene la forma: y'' + {self.yizq}y' + {self.independienteizq}y = d²x² + ex + f")

        #VALIDAR LOS COEFICIENTES DEL LADO DERECHO
        while True:
            self.ycuadradader = input("Ingresa el coeficiente de x² :    ")
            if self.validar_numero(self.ycuadradader):
                self.ycuadradader = int(self.ycuadradader)
                break
            else:
                print("Error: Ingresa solo números enteros.")

        while True:
            self.coeficiente_x = input("Ingresa el coeficiente de x: ")
            if self.validar_numero(self.coeficiente_x):
                self.coeficiente_x = int(self.coeficiente_x)
                break
            else:
                print("Error: Ingresa solo números enteros.")

        while True:
            self.termino_independiente = input("Ingresa el término independiente: ")
            if self.validar_numero(self.termino_independiente):
                self.termino_independiente = int(self.termino_independiente)
                break
            else:
                print("Error: Ingresa solo números enteros.") 

       
        #DEFINIR VARIABLES Y ECUACIONES
        x = sp.Symbol('x')
        a = 1
        #primer termino
        b = self.yizq
        #segundo termino
        c = self.independienteizq
        #================================
        d = self.ycuadradader

        e = self.coeficiente_x

        f = self.termino_independiente

    
        print("La ecuación es:")
        print(f"y'' + {b}y' + {c} = {d}x² + {e}x + {f}")
        print("\n")
        # 
        ecuacion = a*x**2 + b*x + c

        print("Factorizacion:")
        #corregir lo del signo
        print(f"(x + {b}) (x + {c})")
        traslado = sp.solve(ecuacion, x)

        #  print("Factorizacion:")
        x1 = traslado[0].evalf()
        x2 = traslado[1].evalf()
        #quitar decimales a x1 y x2
        x1_visual = "{:.3f}".format(traslado[0].evalf())
        x2_visual = "{:.3f}".format(traslado[1].evalf())
   
        
        print(f"x1 = {x1_visual}")
        print(f"x2 = {x2_visual}")
        print("\n")
       
        x, A, B, C = sp.symbols('x A B C')
        Yp = A*x**2 + B*x + C
        Yp2 = 2*A*x + B
        Yp_double_prime = 2*A

        coef_yp_double_prime = 1
        coef_yp_prime = b
        coef_y = c

        ecuacion = coef_yp_double_prime*Yp_double_prime + coef_yp_prime*Yp2 + coef_y*Yp

        print("La ecuación resultante es:")
       
        print(sp.pretty(ecuacion))
        sp.latex(ecuacion)
        print("\n")
        #SEPARAR LOS TERMINOS DE LA ECUACION
        
        print("Lo siguiente es despejar los terminos de la ecuacion:")
        print("\n")
        print("despejamos A:")
        print("que es el termino que acompaña a x²")
        termino_x2 = ecuacion.coeff(x**2)
        ecuacion_simplificada = sp.Eq(termino_x2, d) 
        A_valor = sp.solve(ecuacion_simplificada, A)[0] 

        print("\nX² ->:")
        print(A_valor)
        print("\n")
        print("despejamos B:")
        print("que es el termino que acompaña a x")

        termino_x = ecuacion.coeff(x)
        ecuacion_simplificada_x = sp.Eq(termino_x, e)
        B_valor = sp.solve(ecuacion_simplificada_x.subs(A, A_valor), B)[0]

        print("\nX ->")
        print(B_valor)

        print("\n")
        print("despejamos C:")
        print("que es el termino independiente")
        termino_independiente = ecuacion - termino_x2*x**2 - termino_x*x
        ecuacion_simplificada_ind = sp.Eq(termino_independiente, f)  # Igualamos el término al valor independiente
        C_valor = sp.solve(ecuacion_simplificada_ind.subs({A: A_valor, B: B_valor}), C)[0]

        print("\nInd ->")
        print(C_valor)


        print("\nRESULTADO")
        print(sp.pretty(Yp))
        print("\n")
        print(f"C₁e^{x1_visual}x + C₂e^{x2_visual}x + ({A_valor})X² + ({B_valor})X + {C_valor}")

        print("\n")
        # preguntar si quiere continuar o regresar al menu principal
        print("Desea continuar con otra ecuación no homogénea?")    
        print("1. Sí")
        print("2. No")
        opcion = input("Seleccione una opción:")
        if opcion == "1":
            self.metodo()
        else:
            return


if __name__ == "__main__":
    nh = NoHomogeneaCoeficiente()
    nh.metodo()