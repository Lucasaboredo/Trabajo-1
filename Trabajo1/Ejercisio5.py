def romanodecimal(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return romanos[romano]

    if romanos[romano[0]] < romanos[romano[1]]:
        return - romanos[romano[0]] + romanodecimal(romano[1:])
    else:
        return romanos[romano[0]] + romanodecimal(romano[1:])

# Ejemplo de uso
numeroromano = "XVI"
numerodecimal = romanodecimal(numeroromano)
print(f"El número romano {numeroromano} es igual a {numerodecimal} en decimal.")
