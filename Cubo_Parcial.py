"""
Representación: tupla de 6 caras x 9 stickers (fila por fila)
Caras: 0=U(W), 1=D(Y), 2=F(R), 3=B(O), 4=L(G), 5=R(B)
Celdas por cara:  0 1 2
                  3 4 5
                  6 7 8
"""

from collections import deque
"""Estructura de datos. ES una cola de doble extremo,
la usamos como cola FIFO porque su operacion popleft() es O(1),
mucho mas eficiente que list.pop(0)"""
import random, time
"""Para generar mezclas aleatorias y medir tiempos de búsqueda"""


RESUELTO = (
    ('W','W','W','W','W','W','W','W','W'),  # 0 Up
    ('Y','Y','Y','Y','Y','Y','Y','Y','Y'),  # 1 Down
    ('R','R','R','R','R','R','R','R','R'),  # 2 Front
    ('O','O','O','O','O','O','O','O','O'),  # 3 Back
    ('G','G','G','G','G','G','G','G','G'),  # 4 Left
    ('B','B','B','B','B','B','B','B','B'),  # 5 Right
)  # Estado resuelto el cubo

# ---Funciones auxiliares de rotacion---
def rot_h(c): return (c[6],c[3],c[0],c[7],c[4],c[1],c[8],c[5],c[2])# rotacion 90grados a derecha
def rot_a(c): return (c[2],c[5],c[8],c[1],c[4],c[7],c[0],c[3],c[6])# rotacion 90grados a izquierda
# ---Funciones conversoras---
def s(e): return [list(c) for c in e]# de tupla a lista 
def t(e): return tuple(tuple(c) for c in e)# de lista a tupla

# ---Funciones de movimiento---
#Funciones de los 18 posibles movimientos del
def X3L(e):
    m=s(e); m[0]=list(rot_h(e[0])) # rotacion (up) y funcion auxiliar
    f,r,b,l = e[2][0:3], e[5][0:3], e[3][0:3], e[4][0:3]#rotamos las caras que tmb se afectan
    m[4][0:3]=f; m[2][0:3]=r; m[5][0:3]=b; m[3][0:3]=l; return t(m)# reasignamos los valores, y volvemos a tupla

def X3R(e):
    m=s(e); m[0]=list(rot_a(e[0])) # rotacion (up) y funcion auxiliar
    f,r,b,l = e[2][0:3], e[5][0:3], e[3][0:3], e[4][0:3]
    m[5][0:3]=f; m[3][0:3]=r; m[4][0:3]=b; m[2][0:3]=l; return t(m)

def X1R(e):
    m=s(e); m[1]=list(rot_h(e[1])) # rotacion (down) y funcion auxiliar
    f,r,b,l = e[2][6:9], e[5][6:9], e[3][6:9], e[4][6:9]
    m[4][6:9]=f; m[2][6:9]=r; m[5][6:9]=b; m[3][6:9]=l; return t(m)

def X1L(e):
    m=s(e); m[1]=list(rot_a(e[1])) # rotacion (down) y funcion auxiliar
    f,r,b,l = e[2][6:9], e[5][6:9], e[3][6:9], e[4][6:9]
    m[5][6:9]=f; m[3][6:9]=r; m[4][6:9]=b; m[2][6:9]=l; return t(m)

def X2R(e):
    m=s(e)# rotacion (front) y funcion auxiliar (no afecta otras caras)
    f,r,b,l = e[2][3:6], e[5][3:6], e[3][3:6], e[4][3:6]
    m[5][3:6]=f; m[3][3:6]=r; m[4][3:6]=b; m[2][3:6]=l; return t(m)

def X2L(e):
    m=s(e) # rotacion (front) y funcion auxiliar (no afecta otras caras)
    f,r,b,l = e[2][3:6], e[5][3:6], e[3][3:6], e[4][3:6]
    m[4][3:6]=f; m[2][3:6]=r; m[5][3:6]=b; m[3][3:6]=l; return t(m)

def Y3U(e):
    m=s(e); m[5]=list(rot_h(e[5]))# rotacion (r) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (2,5,8)], [e[2][i] for i in (2,5,8)], \
              [e[1][i] for i in (2,5,8)], [e[3][i] for i in (0,3,6)]# tomamos partes afectadas de las caras
    m[0][2],m[0][5],m[0][8] = f[0],f[1],f[2]
    m[3][0],m[3][3],m[3][6] = u[2],u[1],u[0]
    m[1][2],m[1][5],m[1][8] = b[2],b[1],b[0]# asignamos los valores a las partes afectadas de las caras
    m[2][2],m[2][5],m[2][8] = d[0],d[1],d[2]; return t(m)#volvemos a tupla

def Y3D(e):
    m=s(e); m[5]=list(rot_a(e[5]))# rotacion (r) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (2,5,8)], [e[2][i] for i in (2,5,8)], \
              [e[1][i] for i in (2,5,8)], [e[3][i] for i in (0,3,6)]
    m[2][2],m[2][5],m[2][8] = u[0],u[1],u[2]
    m[1][2],m[1][5],m[1][8] = f[0],f[1],f[2]
    m[3][0],m[3][3],m[3][6] = d[2],d[1],d[0]
    m[0][2],m[0][5],m[0][8] = b[2],b[1],b[0]; return t(m)

def Y1D(e):
    m=s(e); m[4]=list(rot_h(e[4]))# rotacion (l) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (0,3,6)], [e[2][i] for i in (0,3,6)], \
              [e[1][i] for i in (0,3,6)], [e[3][i] for i in (2,5,8)]
    m[2][0],m[2][3],m[2][6] = u[0],u[1],u[2]
    m[1][0],m[1][3],m[1][6] = f[0],f[1],f[2]
    m[3][2],m[3][5],m[3][8] = d[2],d[1],d[0]
    m[0][0],m[0][3],m[0][6] = b[2],b[1],b[0]; return t(m)

def Y1U(e):
    m=s(e); m[4]=list(rot_a(e[4]))# rotacion (l) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (0,3,6)], [e[2][i] for i in (0,3,6)], \
              [e[1][i] for i in (0,3,6)], [e[3][i] for i in (2,5,8)]
    m[0][0],m[0][3],m[0][6] = f[0],f[1],f[2]
    m[3][2],m[3][5],m[3][8] = u[2],u[1],u[0]
    m[1][0],m[1][3],m[1][6] = b[2],b[1],b[0]
    m[2][0],m[2][3],m[2][6] = d[0],d[1],d[2]; return t(m)

def Y2U(e):
    m=s(e) # rotacion (middle) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (1,4,7)], [e[2][i] for i in (1,4,7)], \
              [e[1][i] for i in (1,4,7)], [e[3][i] for i in (1,4,7)]
    m[0][1],m[0][4],m[0][7] = f[0],f[1],f[2]
    m[3][1],m[3][4],m[3][7] = u[2],u[1],u[0]
    m[1][1],m[1][4],m[1][7] = b[2],b[1],b[0]
    m[2][1],m[2][4],m[2][7] = d[0],d[1],d[2]; return t(m)

def Y2D(e):
    m=s(e)# rotacion (middle) y funcion auxiliar
    u,f,d,b = [e[0][i] for i in (1,4,7)], [e[2][i] for i in (1,4,7)], \
              [e[1][i] for i in (1,4,7)], [e[3][i] for i in (1,4,7)]
    m[2][1],m[2][4],m[2][7] = u[0],u[1],u[2]
    m[1][1],m[1][4],m[1][7] = f[0],f[1],f[2]
    m[3][1],m[3][4],m[3][7] = d[2],d[1],d[0]
    m[0][1],m[0][4],m[0][7] = b[2],b[1],b[0]; return t(m)

def Z1R(e):
    m=s(e); m[2]=list(rot_h(e[2]))# rotacion (front) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (6,7,8)], [e[5][i] for i in (0,3,6)], \
              [e[1][i] for i in (0,1,2)], [e[4][i] for i in (2,5,8)]# tomamos partes afectadas de las caras
    m[5][0],m[5][3],m[5][6] = u[0],u[1],u[2]
    m[1][0],m[1][1],m[1][2] = r[2],r[1],r[0]
    m[4][2],m[4][5],m[4][8] = d[0],d[1],d[2]# asignamos los valores a las partes afectadas de las caras
    m[0][6],m[0][7],m[0][8] = l[2],l[1],l[0]; return t(m)

def Z1L(e):
    m=s(e); m[2]=list(rot_a(e[2]))# rotacion (front) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (6,7,8)], [e[5][i] for i in (0,3,6)], \
              [e[1][i] for i in (0,1,2)], [e[4][i] for i in (2,5,8)]
    m[0][6],m[0][7],m[0][8] = r[0],r[1],r[2]
    m[4][2],m[4][5],m[4][8] = u[2],u[1],u[0]
    m[1][0],m[1][1],m[1][2] = l[0],l[1],l[2]
    m[5][0],m[5][3],m[5][6] = d[2],d[1],d[0]; return t(m)

def Z3L(e):
    m=s(e); m[3]=list(rot_h(e[3]))# rotacion (back) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (0,1,2)], [e[5][i] for i in (2,5,8)], \
              [e[1][i] for i in (6,7,8)], [e[4][i] for i in (0,3,6)]
    m[0][0],m[0][1],m[0][2] = l[0],l[1],l[2]
    m[4][0],m[4][3],m[4][6] = d[2],d[1],d[0]
    m[1][6],m[1][7],m[1][8] = r[0],r[1],r[2]
    m[5][2],m[5][5],m[5][8] = u[2],u[1],u[0]; return t(m)

def Z3R(e):
    m=s(e); m[3]=list(rot_a(e[3])) # rotacion (back) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (0,1,2)], [e[5][i] for i in (2,5,8)], \
              [e[1][i] for i in (6,7,8)], [e[4][i] for i in (0,3,6)]
    m[4][0],m[4][3],m[4][6] = u[0],u[1],u[2]
    m[1][6],m[1][7],m[1][8] = l[2],l[1],l[0]
    m[5][2],m[5][5],m[5][8] = d[0],d[1],d[2]
    m[0][0],m[0][1],m[0][2] = r[2],r[1],r[0]; return t(m)

def Z2R(e):
    m=s(e)# rotacion (middle) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (3,4,5)], [e[5][i] for i in (1,4,7)], \
              [e[1][i] for i in (3,4,5)], [e[4][i] for i in (1,4,7)]
    m[5][1],m[5][4],m[5][7] = u[0],u[1],u[2]
    m[1][3],m[1][4],m[1][5] = r[2],r[1],r[0]
    m[4][1],m[4][4],m[4][7] = d[0],d[1],d[2]
    m[0][3],m[0][4],m[0][5] = l[2],l[1],l[0]; return t(m)

def Z2L(e):
    m=s(e)# rotacion (middle) y funcion auxiliar
    u,r,d,l = [e[0][i] for i in (3,4,5)], [e[5][i] for i in (1,4,7)], \
              [e[1][i] for i in (3,4,5)], [e[4][i] for i in (1,4,7)]
    m[0][3],m[0][4],m[0][5] = r[0],r[1],r[2]
    m[4][1],m[4][4],m[4][7] = u[2],u[1],u[0]
    m[1][3],m[1][4],m[1][5] = l[0],l[1],l[2]
    m[5][1],m[5][4],m[5][7] = d[2],d[1],d[0]; return t(m)

# diccionario de movimientos para acceso por nombre
MOVS = {
    'X1R':X1R,'X1L':X1L,'X2R':X2R,'X2L':X2L,'X3R':X3R,'X3L':X3L,
    'Y1U':Y1U,'Y1D':Y1D,'Y2U':Y2U,'Y2D':Y2D,'Y3U':Y3U,'Y3D':Y3D,
    'Z1R':Z1R,'Z1L':Z1L,'Z2R':Z2R,'Z2L':Z2L,'Z3R':Z3R,'Z3L':Z3L,
}

# ── BFS con reporte visual del proceso 
def bfs(inicio, limite=7):
    if inicio == RESUELTO: return []# si el cubo esta resuleto vuleve lista vacia
    cola, visitados = deque([(inicio, [])]), {inicio}# crea la cola BFS con el estado inicial(estado, camino), y cera conjunto de estados 
    nivel_actual = -1#guardamos en que lvl del algoritmo estamos

    # Bucle principal
    while cola:# corre mientras haya estados pendientes por revisar 
        estado, camino = cola.popleft()# Saca el estado mas antiguo de la cola
        if len(camino) >= limite: continue# si el camino llega al limite, cambia de camino

        # Cada vez que pasamos a un nivel más profundo, lo anunciamos
        if len(camino) != nivel_actual:# detecta cuando el algoritmo cambia de nivel
            nivel_actual = len(camino)# actualiza el ultimo lvl al nuevo
            print(f"\n  {'·'*48}")#separador visual
            print(f"  Revisando estados que necesitan {nivel_actual + 1} movimiento(s)...")#suma uno al nivel
            print(f"  Estados en lista de espera : {len(cola) + 1}")# muestra la cantidad de estados en la cola, suma uno porque el estado actual ya fue sacado de la cola
            print(f"  Estados ya descartados     : {len(visitados)}")# muestra estados descartados

        for nombre, fn in MOVS.items():#recorre cada movimiento posible
            nuevo = fn(estado)# aplica el movimiento al estado actual para obtener un nuevo estado
            if nuevo in visitados: continue#si el estado ya fue explorado lo ignora.
            nuevo_camino = camino + [nombre]#crea historial del camino
            if nuevo == RESUELTO:# compara el actual con el resuelto
                return nuevo_camino# devuelve camino que se llevo para llegar a la solucion
            visitados.add(nuevo)# marca estado nuevo como visto
            cola.append((nuevo, nuevo_camino))# # agrega el nuevo estado al final de la cola junto al historial
    return None# si se vacia la cola sin encontrar solucion, devuelve None

#Utilidades para mezclar, aplicar movimientos e imprimir el estado del cubo
def aplicar(estado, movs):#recibe estado del cubo y una lista de movimientos a aplicar
    for m in movs: estado = MOVS[m](estado)# recorre cada mov, aplica la funcion correspondiente
    return estado

def mezclar(n=5, semilla=None):
    if semilla: random.seed(semilla)#generador de movs
    inv = {'X1R':'X1L','X1L':'X1R','X2R':'X2L','X2L':'X2R','X3R':'X3L','X3L':'X3R',
           'Y1U':'Y1D','Y1D':'Y1U','Y2U':'Y2D','Y2D':'Y2U','Y3U':'Y3D','Y3D':'Y3U',
           'Z1R':'Z1L','Z1L':'Z1R','Z2R':'Z2L','Z2L':'Z2R','Z3R':'Z3L','Z3L':'Z3R'}
    nombres, estado, ultimo, usados = list(MOVS), RESUELTO, None, []#convertimos claves del diccionario MOVS en una lista de 18 nombres de movimiento disponibles
    for _ in range(n):#repite n veces para n movs
        m = random.choice([x for x in nombres if x != inv.get(ultimo)])# evitamos el movimiento contrario
        estado = MOVS[m](estado); usados.append(m); ultimo = m# guardamos el moviento aplicado
    return estado, usados#devuelve cubo mezclado

def imprimir(e):#recibe estado del cubo
    c = e
    print(f"\n      ┌───────┐")
    print(f"      │ {c[0][0]} {c[0][1]} {c[0][2]} │")
    print(f"      │ {c[0][3]} {c[0][4]} {c[0][5]} │  U(W)")
    print(f"      │ {c[0][6]} {c[0][7]} {c[0][8]} │")
    print(f"┌─────┼───────┼─────┬─────┐")
    print(f"│{c[4][0]} {c[4][1]} {c[4][2]}│ {c[2][0]} {c[2][1]} {c[2][2]} │{c[5][0]} {c[5][1]} {c[5][2]}│{c[3][0]} {c[3][1]} {c[3][2]}│")
    print(f"│{c[4][3]} {c[4][4]} {c[4][5]}│ {c[2][3]} {c[2][4]} {c[2][5]} │{c[5][3]} {c[5][4]} {c[5][5]}│{c[3][3]} {c[3][4]} {c[3][5]}│")
    print(f"│{c[4][6]} {c[4][7]} {c[4][8]}│ {c[2][6]} {c[2][7]} {c[2][8]} │{c[5][6]} {c[5][7]} {c[5][8]}│{c[3][6]} {c[3][7]} {c[3][8]}│")
    print(f"└─────┼───────┼─────┴─────┘")
    print(f"      │ {c[1][0]} {c[1][1]} {c[1][2]} │")
    print(f"      │ {c[1][3]} {c[1][4]} {c[1][5]} │  D(Y)")
    print(f"      │ {c[1][6]} {c[1][7]} {c[1][8]} │")
    print(f"      └───────┘")
    print(f" L(G)    F(R)   R(B)  B(O)")
# MAIN
if __name__ == '__main__':

    #Ejemplo 1: mezcla manual de 3 movimientos 
    print("=" * 52)#separador visual
    print("  EJEMPLO 1: mezcla de 3 movimientos")
    print("=" * 52)

    mezcla = ['Z1R', 'Y3U', 'X3L']
    mezclado = aplicar(RESUELTO, mezcla)#parte del resulto y aplica los 3 movs

    print(f"\nMovimientos aplicados para mezclar: {mezcla}")
    print("Así quedó el cubo:")
    imprimir(mezclado)

    print("\n--- Iniciando búsqueda BFS ---")
    t0 = time.time()#guarda el tiempo de inicio
    sol = bfs(mezclado, limite=len(mezcla)+1)# llamamos algortimo BFS
    t1 = time.time()#guarda el tiempo de finalizacion

    print(f"\n{'='*52}")
    print(f"  SOLUCION ENCONTRADA: {sol}")
    print(f"  Movimientos necesarios : {len(sol)}")
    print(f"  Tiempo de búsqueda     : {t1-t0:.3f} segundos")
    print(f"{'='*52}")

    print("\nAplicando la solución paso a paso:")
    estado_paso = mezclado# copia del estado mezclado para ir aplicando los movimientos de la solucion paso a paso
    for i, mov in enumerate(sol):#recorre cada movimiento de la solucion encontrada
        estado_paso = MOVS[mov](estado_paso)# aplica mov y actualiza el estado
        print(f"\n  Paso {i+1}: {mov}")# imprimimos paso actual 
        imprimir(estado_paso)

    print(f"\nVerificación final: {'✅ Cubo resuelto' if aplicar(mezclado, sol)==RESUELTO else '❌ Error'}")

    # ── Ejemplo 2: mezcla aleatoria de 4 movimientos ─────────────────────────
    print("\n\n" + "=" * 52)
    print("  EJEMPLO 2: mezcla aleatoria de 4 movimientos")
    print("=" * 52)

    estado, movs = mezclar(4, semilla=42)
    print(f"\nMovimientos aplicados para mezclar: {movs}")
    print("Así quedó el cubo:")
    imprimir(estado)

    print("\n--- Iniciando búsqueda BFS ---")
    t0 = time.time()
    sol2 = bfs(estado, limite=6)
    t1 = time.time()

    print(f"\n{'='*52}")
    print(f"  SOLUCION ENCONTRADA: {sol2}")
    print(f"  Movimientos necesarios : {len(sol2)}")
    print(f"  Tiempo de búsqueda     : {t1-t0:.3f} segundos")
    print(f"{'='*52}")
    print(f"\nVerificación final: {'✅ Cubo resuelto' if sol2 and aplicar(estado,sol2)==RESUELTO else '❌ Error'}")