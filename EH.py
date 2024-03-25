import sympy as sp

def ecuacion_homogenea():
    print("*** ECUACION HOMOGENEAS ***")
    print("")

    print("Las ecuaciones hogemenas se pueden expresar como:")
    print("dy/dx = f(y/x)")
    print("dy/dx = f(x/y)")
    print("dy/dx = f(y/x, x/y)")
    
    print("Ejemplo de ecuación homogénea:")
    print("dy/dx = (2x + y) / (x + y)")
    ecuacion = input("Ingrese la ecuación: ")
    llevacondicionante=input("LLeva condicional inicial S/ N: ")
    
    if llevacondicionante.lower() in ["s", "si"]:
      x0 = float(input("Ingrese el valor inicial de x: "))
      y0 = float(input("Ingrese el valor inicial de y: "))
    else:
        x0 = y0 = None
    
    
    # Definimos las variables y símbolos
    x, y, u, c = sp.symbols('x y u c')
    dx, dy, du = sp.symbols('dx dy du')
    ln = sp.symbols('ln')
    
    
    
    # Parseamos la ecuación ingresada
    partes = ecuacion.split("=")
    
    puraformula = partes[1].strip()
    
    if '/' in puraformula:
        divisionPartes = puraformula.split("/")
        lado_izquierdo = divisionPartes[0].strip()
        lado_derecho = divisionPartes[1].strip()
    else:
        lado_izquierdo = puraformula
        lado_derecho = "x"
    
    # Imprimimos la ecuación en la forma deseada
    print("La ecuación ingresada es:")
    print("Lo que hicimos fue separar la ecuación en dos partes")
    print("")
    print("")
    print("dy =", lado_izquierdo)
    print("_____")
    print("dx =", lado_derecho)
    print("")
    
    print("Lo siguiente es multiplicar ambos lados por dx y dy respectivamente")
    print("Segundo paso :")
    print("")
    print(lado_derecho + " dy = " + lado_izquierdo + " dx")
    print("")
    lado_derecho = lado_derecho + "*dy"
    lado_izquierdo = lado_izquierdo + "*dx"
    
    # Verificamos si en el tercer paso 'x' o 'y' es la variable dependiente
    tercer_paso_x = False
    if len(lado_izquierdo) < len(lado_derecho):
        print("Tercer paso:")
        print("")
        print("x = uy")
        print("dx = u dy + y du")
        print("")
        lado_izquierdo = lado_izquierdo.replace('dx', '(u*dy + y*du)')
        # Realizamos la sustitución correcta
        lado_derecho = lado_derecho.replace('x', '(u*y)')
        lado_izquierdo = lado_izquierdo.replace('x', '(u*y)')
        tercer_paso_x = True
    else:
        print("Tercer paso:")
        print("")
        print("y = ux")
        print("dy = u dx + x du")
        print("")
        
        # Realizamos la sustitución correcta
        lado_derecho = lado_derecho.replace('dy', '(u*dx + x*du)')
        lado_derecho = lado_derecho.replace('y', '(u*x)')
        lado_izquierdo = lado_izquierdo.replace('y', '(u*x)')
        
    print("Cuarto paso:")
    print("")
    print(lado_derecho + " = " + lado_izquierdo)
    print("")
    
    print("Quinto paso")
    print("")
    
    # Convertir las expresiones a SymPy
    lado_derecho = sp.sympify(lado_derecho)
    
    
    lado_izquierdo = sp.sympify(lado_izquierdo)
    
    # Expandir términos
    lado_derecho_exp = lado_derecho.expand()
    
    lado_izquierdo_exp = lado_izquierdo.expand()
    print(lado_derecho)
    
    # Imprimir resultados
    print("Lado derecho después de la multiplicación:")
    print(lado_derecho_exp)
    print("\nLado izquierdo después de la multiplicación:")
    print(lado_izquierdo_exp)
    print("")
    
    print("haci se ve  completa ")
    print(str(lado_derecho_exp) + " = " +str(lado_izquierdo_exp))
    
    print("")
    print("Sexto paso")
    
    dy_terms = []
    du_terms = []
    
    dx_terms = []
    if tercer_paso_x != False:
     
     
     for term in lado_derecho_exp.as_ordered_terms():
        if dy in term.free_symbols:
            dy_terms.append(term)
        else:
            du_terms.append(term)
     for term in lado_izquierdo_exp.as_ordered_terms():
        if dy in term.free_symbols:
            dy_terms.append(-term)  # Cambiar el signo al moverlos al otro lado
        else:
            du_terms.append(term)
    else:
        
        for term in lado_derecho_exp.as_ordered_terms():
         if dx in term.free_symbols:
            dx_terms.append(term)
         else:
            du_terms.append(term)
        for term in lado_izquierdo_exp.as_ordered_terms():
         if dx in term.free_symbols:
            dx_terms.append(-term)  # Cambiar el signo al moverlos al otro lado
         else:
            du_terms.append(term)
        
    if tercer_paso_x!=False:
    
    # Construir nuevas expresiones para cada lado
     lado_derecho_dy = sum(dy_terms)
     lado_izquierdo_du = sum(du_terms)
     print(lado_derecho_dy)
     print(lado_izquierdo_du)
     print("")
     print("Séptimo paso")
       # Factorización de términos
     lado_derecho_factors = sp.factor(lado_derecho_dy)
     lado_izquierdo_factors = sp.factor(lado_izquierdo_du)
     
    else:
         # Construir nuevas expresiones para cada lado
      lado_derecho_dx = sum(dx_terms)
      lado_izquierdo_du = sum(du_terms)
      print(lado_derecho_dx)
      print(lado_izquierdo_du)
      print("")
      print("Séptimo paso")
       # Factorización de términos
      lado_derecho_factors = sp.factor(lado_derecho_dx)
      lado_izquierdo_factors = sp.factor(lado_izquierdo_du)
     
  
    
    print("Lado derecho con términos factorizados:")
    print(lado_derecho_factors)
    print("\nLado izquierdo con términos factorizados:")
    print(lado_izquierdo_factors)
    print("")
    print("Haci se ve completo ")
    print(str(lado_derecho_factors)+"="+str(lado_izquierdo_factors))
    
    print("")
    print("Octavo paso")

    # Obtener los factores de la expresión del lado derecho
    lado_derecho_factors = list(lado_derecho_factors.as_ordered_factors())
    

    # Inicializar listas para almacenar los términos con 'y' y 'u' en el lado derecho
    terminos_con_y_derecho = []
    terminos_con_u_derecho = []
    terminos_con_x_derecho = []
    # Separar la expresión en términos y factor 'du'
    lado_izquierdo_str = str(lado_izquierdo_factors)
    termino_du, termino_sin_du = lado_izquierdo_str.split("du*")

# Reconstruir la expresión reorganizada
    expresion_reorganizada = f"({termino_du}{termino_sin_du})"
    
    #expresion_reorganizada = f"du*(({termino_du})({termino_sin_du}))"
    expresion_reorganizada = sp.simplify(expresion_reorganizada)
    #print(expresion_reorganizada)
    
# Imprimir la expresión reorganizada
    #print("-"*10)
    
    if tercer_paso_x!=False:

    # Separar los términos según los factores en el lado derecho
     for factor in lado_derecho_factors:
        if 'y' in str(factor) and 'dy' not in str(factor):
            terminos_con_y_derecho.append(factor)
        elif 'u' in str(factor) and 'du' not in str(factor):
            terminos_con_u_derecho.append(factor)

    # Imprimir los términos con 'y' y 'u' en el lado derecho
     print("Términos con 'y' en el lado derecho:", terminos_con_y_derecho)
     print("Términos con 'u' en el lado derecho:", terminos_con_u_derecho)
    else:
        for factor in lado_derecho_factors:
         if 'x' in str(factor) and 'dx' not in str(factor):
          terminos_con_x_derecho.append(factor)
         elif 'u' in str(factor) and 'du' not in str(factor):
          terminos_con_u_derecho.append(factor)

# Imprimir los términos con 'y' y 'u' en el lado derecho
        print("Términos con 'x' en el lado derecho:", terminos_con_x_derecho)
        print("Términos con 'u' en el lado derecho:", terminos_con_u_derecho)
        
    

    # Obtener los factores de la expresión del lado izquierdo
    lado_izquierdo_factors = list(expresion_reorganizada.as_ordered_factors())

    # Inicializar listas para almacenar los términos con 'y' y 'u' en el lado izquierdo
    terminos_con_y_izquierdo = []
    terminos_con_u_izquierdo = []
    terminos_con_x_izquierdo = []
    if tercer_paso_x!=False:
    # Separar los términos según los factores en el lado izquierdo
     for factor in lado_izquierdo_factors:
        if 'y' in str(factor) and 'dy' not in str(factor):
            terminos_con_y_izquierdo.append(factor)
        elif 'u' in str(factor) and 'du' not in str(factor):
            terminos_con_u_izquierdo.append(factor)

    # Imprimir los términos con 'y' y 'u' en el lado izquierdo
     print("Términos con 'y' en el lado izquierdo:", terminos_con_y_izquierdo) 
     print("Términos con 'u' en el lado izquierdo:", terminos_con_u_izquierdo)
     
    else:
       for factor in lado_izquierdo_factors:
        if 'x' in str(factor) and 'dx' not in str(factor):
            terminos_con_x_izquierdo.append(factor)
        elif 'u' in str(factor) and 'du' not in str(factor):
            terminos_con_u_izquierdo.append(factor)

    # Imprimir los términos con 'y' y 'u' en el lado izquierdo
       print("Términos con 'x' en el lado izquierdo:", terminos_con_x_izquierdo) 
       print("Términos con 'u' en el lado izquierdo:", terminos_con_u_izquierdo)
       # Asumiendo que du, dx, dy, u, x, y son símbolos definidos previamente

# Verificar si tercer_paso_x es False o no
    if tercer_paso_x != False:
     factorizacionderecha = None
     izq = None

    # Verificar si hay términos con 'y' en el lado derecho e izquierdo
     if len(terminos_con_y_derecho) > 0 and len(terminos_con_y_izquierdo) > 0:
        factorizacionderecha = (terminos_con_y_derecho[0] / terminos_con_y_izquierdo[0]) * dy
     elif len(terminos_con_y_derecho) > 0:
        factorizacionderecha = dy / terminos_con_y_izquierdo[0]

    # Verificar si hay términos con 'u' en el lado derecho e izquierdo
     if len(terminos_con_u_derecho) > 0 and len(terminos_con_u_izquierdo) > 0:
        izq = (terminos_con_u_derecho[0] / terminos_con_u_izquierdo[0]) * du
     elif len(terminos_con_u_derecho) >= 0:
        izq = du / terminos_con_u_derecho[0] if len(terminos_con_u_derecho) > 0 else du / terminos_con_u_izquierdo[0]

    else:
       factorizacionderecha = None
       izq = None

    # Verificar si hay términos con 'x' en el lado derecho e izquierdo
       if len(terminos_con_x_derecho) > 0 and len(terminos_con_x_izquierdo) > 0:
        factorizacionderecha = (terminos_con_x_derecho[0] / terminos_con_x_izquierdo[0]) * dx
       elif len(terminos_con_x_derecho) > 0:
        factorizacionderecha = dx / terminos_con_x_izquierdo[0]

    # Verificar si hay términos con 'u' en el lado derecho e izquierdo
       if len(terminos_con_u_derecho) > 0 and len(terminos_con_u_izquierdo) > 0:
        izq = (terminos_con_u_derecho[0] / terminos_con_u_izquierdo[0]) * du
       elif len(terminos_con_u_derecho) >= 0:
        izq = du / terminos_con_u_derecho[0] if len(terminos_con_u_derecho) > 0 else du / terminos_con_u_izquierdo[0]

# Imprimir los resultados
    print()
    print("Noveno paso: Mandar las x o y o u a sus lados respectivos y dividirlos")
    print()
    print("Factorización derecha:", factorizacionderecha)
    print()
    print("Izquierda:", izq)

    
    
    print()
    print("Decimo paso Ln ")
    print("")
    
    

    if tercer_paso_x!=False:
    # Imprimir la expresión final en términos de logaritmos naturales
     print("\nExpresión final:")
     print("ln"+ "(" +str(terminos_con_y_derecho[0])+")"+"="+"ln"+ "(" +str(terminos_con_u_derecho[0])+")" + " + ln"+str(c))
    else:
        # Imprimir la expresión final en términos de logaritmos naturales
     print("\nExpresión final:")
     print("ln"+ "(" +str(terminos_con_x_derecho[0])+")"+"="+"ln"+ "(" +str(terminos_con_u_derecho[0])+")" + " + ln"+str(c))
    
    # Combinar los logaritmos en base natural
    print("")
    print("11° paso")
    
    if tercer_paso_x!=False:
        
       ladoderechodeln=sp.ln(terminos_con_y_derecho[0])
       ladoizquierdoln= sp.ln(terminos_con_u_derecho[0])  + sp.ln(c)
        
    else:    
     ladoderechodeln=sp.ln(terminos_con_x_derecho[0])+ sp.ln(c)
     ladoizquierdoln= sp.ln(terminos_con_u_derecho[0]) 
    
    # Expandir la expresión para aplicar la regla de los logaritmos
    expresion_expandida = sp.expand_log(ladoizquierdoln)
    
    ladorecho = sp.simplify(ladoderechodeln)
    ladoizquierdo = sp.simplify(expresion_expandida)
    print()
    print("eliminar ln con e  ")
    
    print()
    
    
    print(str( sp.exp(ladoizquierdo))+" = "+str(sp.exp(ladorecho)))

    print()
    print("12 Paso ")
    
    
    print()
    cambiaruPorxy=ladoizquierdo.subs('u',(x/y))
    print()
    
    
    
    #print(str(sp.exp(ladorecho))+" = "+str(sp.exp(cambiaruPorxy)))
    
    #cambiaruPorxy=sp.exp(ladorecho) = sp.exp(cambiaruPorxy)
    
    
    
    
    ecuacion_c=sp.Eq(sp.exp(ladorecho),sp.exp(cambiaruPorxy))
    #print(ecuacion_c)
    slucion_de_c=sp.solve(ecuacion_c,c)
    
    #print(slucion_de_c)
    
    #print(slucion_de_c)
    if tercer_paso_x!=False:
        
      ecuacion_c = sp.Eq(ladorecho, cambiaruPorxy)

# Resolver la ecuación resultante
      soluciones_de_c = sp.solve(ecuacion_c, c)

# Imprimir las soluciones para c
      if llevacondicionante == "n" :
       print("Soluciones para c   :")
       for solucion in soluciones_de_c:
        print(solucion)
      else:
       print("Soluciones para c:")
       solucion=resolver_ecuacion_para_c_con_condicional(ecuacion_c,x0,y0)
       print(solucion)

# Resolver la ecuación resultante
      soluciones = sp.solve(ecuacion_c, y)  # Resolvemos respecto a y

# Imprimir las soluciones
      print("Soluciones para y:")
      for solucion in soluciones:
        print()
        print(solucion)
      
    else:
       
       
        
      ecuacion_c = sp.Eq(ladorecho, cambiaruPorxy)

# Resolver la ecuación resultante
      soluciones_de_c = sp.solve(ecuacion_c, c)

# Imprimir las soluciones para c
      if llevacondicionante == "n" :
       print("Soluciones para c   :")
       for solucion in soluciones_de_c:
        print(solucion)
      else:
       print("Soluciones para c:")
       solucion=resolver_ecuacion_para_c_con_condicional(ecuacion_c,x0,y0)
       print(solucion)

# Resolver la ecuación resultante
      soluciones = sp.solve(ecuacion_c, x)  # Resolvemos respecto a y

# Imprimir las soluciones
      print("Soluciones para x:")
      for solucion in soluciones:
        print()
        print(solucion)
     
     
     
     
def resolver_ecuacion_para_c(ecuacion):
    """
    Resuelve el paso 12 para obtener el valor de la constante 'c' de una ecuación diferencial homogénea de primer orden.
    """
    
    # Definimos las variables y símbolos
    x, y, u, c = sp.symbols('x y u c')
    dx, dy, du = sp.symbols('dx dy du')
    
    # Parseamos la ecuación ingresada
    partes = ecuacion.split("=")
    
    puraformula = partes[1].strip()
    
    if '/' in puraformula:
        divisionPartes = puraformula.split("/")
        lado_izquierdo = divisionPartes[0].strip()
        lado_derecho = divisionPartes[1].strip()
    else:
        lado_izquierdo = puraformula
        lado_derecho = "1"  # Si no hay división, el lado derecho se considera 1 para formar una ecuación homogénea
    
    # Determinamos si 'x' o 'y' es la variable dependiente
    tercer_paso_x = len(lado_izquierdo) < len(lado_derecho)
    
    # Convertimos las cadenas de lado izquierdo y derecho a expresiones de sympy
    lado_izquierdo_expr = sp.sympify(lado_izquierdo, locals={'x': x, 'y': y, 'dx': dx, 'dy': dy})
    lado_derecho_expr = sp.sympify(lado_derecho, locals={'x': x, 'y': y, 'dx': dx, 'dy': dy})
    
    # Realizamos las sustituciones necesarias
    if tercer_paso_x:
        sustitucion = {x: u*y, dx: u*dy + y*du}
    else:
        sustitucion = {y: u*x, dy: u*dx + x*du}
    
    lado_izquierdo_sust = lado_izquierdo_expr.subs(sustitucion)
    lado_derecho_sust = lado_derecho_expr.subs(sustitucion)
    
    # Separación de variables
    ecuacion_separada = sp.Eq(lado_derecho_sust, lado_izquierdo_sust)
    variables_separadas = sp.separatevars(ecuacion_separada, symbols=[dy, du], force=True)
    
    # Integración
    solucion_integrada = sp.integrate(variables_separadas.rhs - variables_separadas.lhs, u)
    
    # Solución para 'c'
    ecuacion_para_c = sp.Eq(solucion_integrada, c)
    solucion_para_c = sp.solve(ecuacion_para_c, c)
    
    return solucion_para_c
    

    



def resolver_ecuacion_para_c_con_condicional(ecuacion, x0, y0):
    x, y, c = sp.symbols('x y c')
    
    # Sustituir condiciones iniciales en la ecuación
    ecuacion = ecuacion.subs({x: x0, y: y0})
    
    # Resolver la ecuación para la constante 'c'
    solucion_para_c = sp.solve(ecuacion, c)
    
    return solucion_para_c

    
    


ecuacion_homogenea()