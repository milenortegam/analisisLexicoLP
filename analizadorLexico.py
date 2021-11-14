import ply.lex as lex

#Milen Ortega Mautong

reservadas = {
    'alias': 'alias',
    'begin': 'begin',
    'class': 'class',
    'do': 'do',
    'end': 'END',
    'false': 'false',
    'module': 'module',
    'not': 'not',
    'rescue': 'rescue',
    'self': 'self',
    'true': 'true',
    'until': 'until',
    'yield': 'yield',
    'and': 'and',
    'break': 'break',
    'def': 'def',
    'else': 'else',
    'end': 'end',
    'for': 'for',
    'next': 'next',
    'or': 'or',
    'retry': 'retry',
    'super': 'super',
    'undef': 'undef',
    'when': 'when',
    'begin': 'BEGIN',
    'case': 'case',
    'elsif': 'elsif',
    'ensure': 'ensure',
    'if': 'if',
    'nil': 'nil',
    'redo': 'redo',
    'return': 'return',
    'unles': 'unles',
    'while': 'while',
}


tokens = (
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'IZQPAREN',
    'DERPAREN',
    'FLOTANTE',
    'VGLOBALES',
    'VLOCALES',
    'VCLASE',
    'VINSTANCIA',
    'CONSTANTES',
#Gabriela Pazmiño Guerrero
    'NUMERO',
    'IMAGINARIO',
    'BOOLEANOV',
    'BOOLEANOF',
    'CADENAS',
    'ARREGLOS',
    'MAPAS',
    'SIMBOLOS'
) + tuple(reservadas.values())


t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IZQPAREN = r'\('
t_DERPAREN = r'\)'

#Gabriela Pazmiño Guerrero
t_NUMERO = r'\d+'
t_IMAGINARIO = r'\d+\+\d'
t_BOOLEANOV = r'\true'
t_BOOLEANOF = r'\false'
t_CADENAS = r'\[a-z]+'

#t_VGLOBALES = r'^\$[a-z]+[_a-zA-Z0-9]*'
#t_VLOCALES = r'^[a-z]+[_a-zA-Z0-9]*'
#t_VCLASE = r'^@@[a-z]+[_a-zA-Z0-9]*'
#t_VINSTANCIA = r'^@[a-z]+[_a-zA-Z0-9]*'
#t_CONSTANTES = r'^[A-Z]+[_a-zA-Z0-9]*'

def t_VGLOBALES(t):
    r'[\$][a-z]+[_a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'VGLOBALES')
    return t

def t_VLOCALES(t):
    r'[a-z]+[_a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'VLOCALES')
    return t

def t_VCLASE(t):
    r'[@][@][a-z]+[_a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'VCLASE')
    return t

def t_VINSTANCIA(t):
    r'[@][a-z]+[_a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'VINSTANCIA')
    return t

def t_CONSTANTES(t):
    r'[A-Z]+[_a-zA-Z0-9]*'
    t.type = reservadas.get(t.value, 'CONSTANTES')
    return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore  = ' \t'


lexer = lex.lex()

 # Test it out
data = '''
    3 + 4 * 10
    + -20 *2
    $var_global 
    @@var_clase
    @var_insta
    CONSTANTE2
    var_local
    if
'''
 
 # Give the lexer some input
lexer.input(data)
 
 # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)