import random

### Bienvenida
print(f"Hola, bienvenido. Por favor eliga una regla del 0-255.") ### 0 al 255 -> 1 al 256
regla = int(input("Regla: "))

### Regla en binario
    # Acá se crea una función que pasa la regla puesta por el usuario a binario.

def binRegla(numRegla):
    numRegla = int(numRegla)
    stringBinario = bin(numRegla)[2:].zfill(8)
    patrones = [(1,1,1),(1,1,0),(1,0,1),(1,0,0),(0,1,1),(0,1,0),(0,0,1),(0,0,0)]
    reglaDic = {}
    for i, patron in enumerate(patrones):
        reglaDic[patron] = int(stringBinario[i])
    return reglaDic, stringBinario
reglaDic, stringBinario = binRegla(regla)



### Fila inicial
largoInicial = int(input("Que tan larga va a ser la primera fila?: "))
fila1 = []

    # Genera una primera fila con el largo que le da el usuario (llena de 0)
for i in range(0,largoInicial):
    fila1.append(0)

    # Elige al azar la cantidad de 1s que van a poblar, tal como donde.
for i in range(0,random.randrange(largoInicial)):
    valor1 = int(random.randrange(largoInicial))
    fila1[valor1] = 1
print(f"Así se ve tu primera generación: \n{fila1}")

### Esto va a ver cuantas generaciones se quieren visualizar.
    # P.D. Acá no se recortan los extremos, por lo cual no toma forma piramidal.
numGeneraciones = int(input("Cuantas generaciones van a ser?: "))

### Esta función define el comportamiento de la siguiente generación.
def siguienteFila(fila_actual, reglaDic):
    nueva_fila = []
    n = len(fila_actual)
    
    for i in range(n):
        # Manejar bordes (primera y última celda) NO se recortan.
        izquierda = fila_actual[i-1] if i > 0 else 0
        centro = fila_actual[i]
        derecha = fila_actual[i+1] if i < n-1 else 0
        
        # Analiza el comportamiento y lo contrasta con el diccionario.
        patron = (izquierda, centro, derecha)
        nuevo_valor = reglaDic[patron]
        nueva_fila.append(nuevo_valor)
    return nueva_fila

### Lo visualizamos de forma más ordenada (sin , y sin [])
def visualizarFila(fila):
    visual = ""
    for celda in fila:
        if celda == 1:
            visual += "1"
        else:
            visual += "0"
    return visual

### SIMULACIÓN
print("\nEvolución:")
    # Empezamos en la fila 1 siempre
fila_actual = fila1

for gen in range(numGeneraciones):
    # Visualizar la fila actual
    print(visualizarFila(fila_actual))
    
    # Generar siguiente fila
    fila_actual = siguienteFila(fila_actual, reglaDic)