import ply.lex as lex

#Milen Ortega Mautong

reservadas = {
    'alias': 'ALIAS',
    'begin': 'BEGIN',
    'class': 'CLASS',
    'do': 'DO',
    'end': 'END',
    'false': 'FALSE',
    'module': 'MODULE',
    'not': 'NOT',
    'rescue': 'RESCUE',
    'self': 'SELF',
    'true': 'TRUE',
    'until': 'UNTIL',
    'yield': 'YIELD',
    'and': 'AND',
    'break': 'BREAK',
    'def': 'DEF',
    'else': 'ELSE',
    'for': 'FOR',
    'next': 'NEXT',
    'or': 'OR',
    'retry': 'RETRY',
    'super': 'SUPER',
    'undef': 'UNDEF',
    'when': 'WHEN',
    'file': 'FILE',
    'case': 'CASE',
    'defined': 'DEFINED',
    'elsif': 'ELSIF',
    'ensure': 'ENSURE',
    'if': 'IF',
    'nil': 'NIL',
    'redo': 'REDO',
    'return': 'RETURN',
    'unles': 'UNLES',
    'while': 'WHILE',
    'line': 'LINE',
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
) + tuple(reservadas.values())


t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IZQPAREN = r'\('
t_DERPAREN = r'\)'
t_FLOTANTE = r'\d+\.\d+'
t_NUMERO = r'\d+'



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
