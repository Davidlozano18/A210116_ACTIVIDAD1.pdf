import ply.lex as lex

lexema = []

reservada = ('CADENA ',)
tokens = reservada + ('VARIABLEMA','VARIABLEMI',)

def t_VARIABLEMA (t):
    r'[A-Z_]+(w d)*'
def t_VARIABLEMI (t):
    r'[a-z]+(w d)*'
def t_CADENA(t) :
    r'\"?( \ W+\* \w * \ d*  \ * ) \ "?'
    return t 
def t_error (t):
    global lexema
    estado = "**Token no valido en la linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                                   str(t.lexpos))
    lexema.append(estado)
    t.lexer.skip(1)

def ingreso(datos):
    global lexema

    analizador=lex.lex()
    analizador.input(datos)

    lexema.clear
    while True:
        toke = analizador.token()
        if not toke:
            break
        estado = " Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(toke.lineno), str(toke.value),
                                                                                   str(toke.lexpos))
        lexema.append(estado)
    return lexema
analizador = lex.lex()

if __name__=='__main__':
    while True:
        datos = input ("ingrese la cadena:")
    prueba(datos)
    print(lexema)