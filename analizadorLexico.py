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
    'NUMERO',
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
) + tuple(reservadas.values())


t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IZQPAREN = r'\('
t_DERPAREN = r'\)'
t_FLOTANTE = r'\d+\.\d+'
t_NUMERO = r'\d+'
t_VGLOBALES = r'^\$[a-z]+[_a-zA-Z0-9]*'
t_VLOCALES = r'^[a-z]+[_a-zA-Z0-9]*'
t_VCLASE = r'^@@[a-z]+[_a-zA-Z0-9]*'
t_VINSTANCIA = r'^@[a-z]+[_a-zA-Z0-9]*'
t_CONSTANTES = r'^[A-Z]+[_a-zA-Z0-9]*'



def t_NUMBERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
