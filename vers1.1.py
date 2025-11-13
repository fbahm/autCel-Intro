

def regla_wolfram(numero_regla):
    # Convertimos el numero de regla a binario de 8 bits. 
    binario = f"{numero_regla:08b}"  
    # Todas las combinaciones de 3 celdas . 
    patrones = [
        (1, 1, 1),
        (1, 1, 0),
        (1, 0, 1),
        (1, 0, 0),
        (0, 1, 1),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0)
    ]
    # Creamos diccionario que asocia cada resultado . 
    return {patrones[i]: int(binario[i]) for i in range(8)}


# A partir de una fila de celdas , genera la sigueinte aplicando la regla de evolucion . 
def evolucionar(fila, regla):     # Creeamos una nueva lista del mismo tamaño , y la iniciamos vacia . 
    # Devuelve la siguiente fila a partir de la actual según la regla.
    nueva = [0] * len(fila)
    for i in range(1, len(fila) - 1):      # Recorremos las celdas sin contar los extremos . 
        vecindad = (fila[i-1], fila[i], fila[i+1])
        nueva[i] = regla[vecindad]     # Aplicamos regla . 
    return nueva    # devolver la nueva fila resultante .


def mostrar(historia):
    # Recorremos cada celda y convertimos 1 en bloque y 0 en vacio . 
        print("".join("█" if c == 1 else " " for c in fila))


# Codigo principal de ejecucion 

print(" Simulacion de automatas celulares ")
print("Ejemplos de reglas principales : 30 (caótica), 90 (simétrica), 110 (compleja), 184 (tráfico)")
print()


# Entradas del usuario
# Solicitamos parametros al usuario . 
try:
    regla_num = int(input("Ingresa el número de la regla (0–255): "))    
    num_celdas = int(input("Número de celdas (recomendado 50–100): "))
    num_pasos = int(input("Número de pasos de evolución: "))

# Validamos que los valores esten dentro de los parametros 
except ValueError:
    print("El valor no es valido.")
    exit()

if not (0 <= regla_num <= 255):
    print("El valor debe ser entre 0 y 255.")
    exit()



fila = [0] * num_celdas      # Creamos fila con todas las celdas vacias . 
fila[num_celdas // 2] = 1     # Activamos la celda central . 
regla = regla_wolfram(regla_num)

# codigo para la evolucion de los automatas  .
historia = [fila[:]]    
for _ in range(num_pasos):
    fila = evolucionar(fila, regla)
    historia.append(fila[:])

# Mostrar resultado
mostrar(historia)

print("\nFin de la simulacion")
