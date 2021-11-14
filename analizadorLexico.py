import ply.lex as lex

# Milen Ortega Mautong

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
    # Inicio Tokens Milen Ortega
             'VGLOBALES',
             'VLOCALES',
             'VCLASE',
             'VINSTANCIA',
             'CONSTANTES',

    # Inicio Tokens Gabriela Pazmiño Guerrero
             'NUMERO',
             'FLOTANTES',
             'CADENAS',
             'ARREGLOS',
             'MAPAS',
             'PUNTO',
             'COMA',
             'INTERROGACION',
             'ADMIRACION',
             'COMENTARIO',

        # Inicio Tokens Hayleen Carrillo
             'MAS',
             'MENOS',
             'MULTIPLICACION',
             'DIVISION',
             'IZQPAREN',
             'DERPAREN',
             'EXPONENCIAL',
            'MODULO',

         ) + tuple(reservadas.values())


# Milen Ortega Mautong
# t_VGLOBALES = r'^\$[a-z]+[_a-zA-Z0-9]*'
# t_VLOCALES = r'^[a-z]+[_a-zA-Z0-9]*'
# t_VCLASE = r'^@@[a-z]+[_a-zA-Z0-9]*'
# t_VINSTANCIA = r'^@[a-z]+[_a-zA-Z0-9]*'
# t_CONSTANTES = r'^[A-Z]+[_a-zA-Z0-9]*'

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


# Gabriela Pazmiño Guerrero
# t_FLOTANTES = r'\d+\.\d+'
# t_NUMERO = r'\d+'
# t_CADENAS = r'"[a-zA-Z0-9\s,]*"'
# t_ARREGLOS = r"\[(('([a-zA-z\s])*'|[0-9]+|[0-9]+,?[0-9]*),?)+\]"
# t_MAPAS = r"\{((\"|')?[a-zA-Z_][a-zA-Z0-9_\s]*(\"|')?(\:|\=>)([0-9]|[1-9][0-9]*|(\"|')[\w\s]+(\"|')),?)+\}"
t_PUNTO = r'\.'
t_COMA = r'\,'
t_INTERROGACION = r'\?'
t_ADMIRACION = r'\!'
t_COMENTARIO = r"\#.*"


def t_FLOTANTES(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ARREGLOS(t):
    r"\[(('([a-zA-z\s])*'|[0-9]+|[0-9]+,?[0-9]*),?)+\]"
    t.value = int(t.value)
    return t


def t_MAPAS(t):
    r"\{((\"|')?[a-zA-Z_][a-zA-Z0-9_\s]*(\"|')?(\:|\=>)([0-9]|[1-9][0-9]*|(\"|')[\w\s]+(\"|')),?)+\}"
    t.value = int(t.value)
    return t


# Inicio Hayleen Carrillo

t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IZQPAREN = r'\('
t_DERPAREN = r'\)'
t_EXPONENCIAL = r'\*\*'
t_MODULO = r'%'


# General
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()

# Test it out
data = '''
    3 + 4.4 * 10
    + -20 *2
    $var_global 
    @@var_clase
    @var_insta
    CONSTANTE2
    var_local
    if
    5%3
    4852**233
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)