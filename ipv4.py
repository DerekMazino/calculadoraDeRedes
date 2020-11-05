def calculandoMascara(prefijo):
    mascara = ''
    prefijo = int(prefijo)
    for i in range(32):
        if i % 8 == 0 and i!=0:
            mascara += '.'
        if i>=prefijo:
            mascara += '0'
        else:
            mascara += '1'
    return str(mascara)

def obtenerDirRed(dir, mascara):
    dirRed = ''
    iteraciones = len(dir)
    for i in range(iteraciones):
        if dir[i] == '1' and mascara[i] == '1':
            dirRed += '1'
        elif dir[i]=='.' and mascara[i]=='.':
            dirRed += '.'
        else:
            dirRed += '0'
    return str(dirRed)

def obtenerPrimerRed(direccion):
    return direccion[:-1] + '1'

def obtenerUltimaRed(direccion):
    return direccion[:-1] + '0'

def obtenerBroadcast(direccion, prefijo):
    prueba = direccion[::-1]
    sufijo = 32 - prefijo
    broadcast = ''
    for i in range(sufijo):
        if i % 8 == 0 and i!=0:
            broadcast += '.'
        if i<sufijo:
            broadcast += '1'
    if prefijo == 24:
        broadcast += '.'
    return (str(broadcast)+prueba[sufijo+1:])[::-1]