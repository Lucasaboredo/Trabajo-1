mochila = ["llaves", "cartuchera", "pala", "caramelos", "sable de luz"]
#Desarrollo
def fuerza (mochila, posicion=0,  objetos=0):
    if posicion >= len(mochila):
        return False, posicion   
    
    objetos += 1
    if mochila[posicion] == "sable de luz":
        return True, posicion

    return fuerza(mochila, posicion + 1, objetos)

encontrado, objetos = fuerza(mochila)

if encontrado:
    print("¡Luke encontró el sable de luz!")
    print(f"Número de objetos sacados: {objetos}")
else:
    print("No se encontró un sable de luz en la mochila.")
    print(f"Se sacaron {objetos} objetos de la mochila.")
    