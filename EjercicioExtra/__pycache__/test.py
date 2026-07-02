proyecto_dict = {
    "presupuesto" : 1000000,
    "impacto_esperado" : 20,
    "duracion_estimada" : 3,
    "miembros" : ["mariano", "agustin", "taiel"],
    "roles" : ["admin", "empleado"],
    "ROI" : 50
}

def evaluar_por_presupuesto(proyecto: dict, limite: int) -> bool:
    aprobado = False
    if proyecto["presupuesto"] < limite:
        aprobado = True
    return aprobado

def evaluar_por_impacto(proyecto: dict, minimo: int) -> bool:
    aprobado = False
    if proyecto["impacto"] < minimo:
        aprobado = True
    return aprobado

def evaluar_por_duracion(proyecto: dict, meses: int) -> bool:
    aprobado = False
    if proyecto["duracion_estimada"] < meses:
        aprobado = True
    return aprobado

# ASIGNAR FUNCIONES A VARIABLES (O LISTA DE FUNCIONES)
# PASAR FUNCIONES COMO PARAMETRO A OTRAS FUNCIONES


def evaluar_proyecto(proyecto: dict, criterio: callable[[dict, int], bool], parametro: int) -> bool:
    
    funciones = [evaluar_por_duracion, evaluar_por_impacto, evaluar_por_presupuesto] 
    for i in range(3):
        ingreso = int(input("Ingrese el valor: "))


    
  

