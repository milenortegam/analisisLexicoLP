import ply.lex as lex

#Milen Ortega Mautong


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
    'file': '_ _FILE_ _',
    'begin': 'BEGIN',
    'case': 'case',
    'defined': 'defined?',
    'elsif': 'elsif',
    'ensure': 'ensure',
    'if': 'if',
    'nil': 'nil',
    'redo': 'redo',
    'return': 'return',
    'unles': 'unles',
    'while': 'while',
    'line': '_ _LINE_ _',
}





def t_NUMBERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


lexer = lex.lex()
