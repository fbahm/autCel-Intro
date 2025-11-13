### Bienvenida
print(f"Hola, bienvenido. Por favor eliga una regla del 0-255.") ### 0 al 255 -> 1 al 256

### Regla en binario
numRegla = int(input("Regla: "))
stringBinario = bin(numRegla)[2:].zfill(8)
print(stringBinario)

