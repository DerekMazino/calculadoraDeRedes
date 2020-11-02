
def decbin(numeroDec):
    numeroDec = int(numeroDec)
    numeroBin = ''
    while numeroDec > 0:
        if numeroDec % 2 == 0:
            numeroBin += '0'
        else:
            numeroBin += '1'
        numeroDec = int(numeroDec/2)
    return agregarCeros(numeroBin[::-1])

def agregarCeros(numeroBin):
    cantidad = 8-len(numeroBin)
    nuevoBinario = ''
    for i in range(cantidad):
        nuevoBinario += '0'
    return nuevoBinario+numeroBin

def bindec(numeroBin):
    pot = 0
    numero = 0
    for i in numeroBin[::-1]:
        numero +=int(i)*2**pot
        pot += 1
    return str(numero)