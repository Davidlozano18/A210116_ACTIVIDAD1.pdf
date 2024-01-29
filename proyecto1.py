import ply.lex as lex

rlexema = []

reserved = {
    'CADENA': 'CADENA'
}

tokens = ['VARIABLEMA', 'VARIABLEMI'] + list(reserved.values())

def t_VARIABLEMA(t):
    r'[A-Z_]+(\w*\d*)*'
    return t

def t_VARIABLEMI(t):
    r'[a-z_]+(\w*\d*)*'
    return t

def t_CADENA(t):
    r'\"(\w+\ \w\d*\ *)\"?'
    return t

def t_error(t):
    global rlexema
    estado = "** Token no válido en la línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), str(t.value), str(t.lexpos))
    rlexema.append(estado)
    t.lexer.skip(1)

def ingreso(datos):
    global rlexema
    analizador = lex.lex()
    analizador.input(datos)
    rlexema.clear()
    while True:
        token = analizador.token()
        if not token:
            break
        estado = "** Línea {:4} Tipo {:16} Valor {:16} Posición {:4}".format(str(token.lineno), str(token.type), str(token.value), str(token.lexpos))
        rlexema.append(estado)
    return rlexema

if _name_ == '_main_':
    while True:
        datos = input("Ingrese la cadena: ")
        ingreso(datos)
        print(rlexema)
