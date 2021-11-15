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
             'COMILLASIMPLE',
             'COMILLADOBLE',

    # Inicio Tokens Gabriela Pazmiño Guerrero
             'NUMERO',
             'FLOTANTES',
             'CADENAS',
             'ARREGLOS',
             'MAPAS',
             'PUNTO',
             'COMA',
             'INTERROGACION',
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
             'IGUAL',
            'ASIGNACIONSUMA',
            'ASIGNACIONRESTA',
            "ASIGNACIONMULT",
            'ASIGNACIONDIV',
            'ASIGNACIONMOD',
            'ASIGNACIONEXP',
            'IGUAL_COMP',
            'DIFERENTE',
            'MENOR',
            'MAYOR',
            'AND',
            'OR',
            'IZQ_CORCH',
            'DER_CORCH',
            'IZQ_LLAVE',
            'DER_LLAVE',

         ) + tuple(reservadas.values())


# Inicio Milen Ortega Mautong


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

# Fin Milen Ortega Mautong


# Inicio Gabriela Pazmiño Guerrero
t_CADENAS = r'"[a-zA-Z0-9\s,]*"'
t_ARREGLOS = r"\[(('([a-zA-z\s])*'|[0-9]+|[0-9]+,?[0-9]*),?)+\]"
t_MAPAS = r"\{((\"|')?[a-zA-Z_][a-zA-Z0-9_\s]*(\"|')?(\:|\=>)([0-9]|[1-9][0-9]*|(\"|')[\w\s]+(\"|')),?)+\}"
t_PUNTO = r'\.'
t_COMA = r'\,'
t_INTERROGACION = r'\?'
t_COMENTARIO = r"\#.*"

def t_FLOTANTES(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


#Fin Gabriela Pazmiño Guerrero

# Inicio Hayleen Carrillo

t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IZQPAREN = r'\('
t_DERPAREN = r'\)'
t_EXPONENCIAL = r'\*\*'
t_MODULO = r'%'
t_IGUAL = r'='
t_ASIGNACIONSUMA = r'\+='
t_ASIGNACIONRESTA = r'-='
t_ASIGNACIONMULT = r'\*='
t_ASIGNACIONDIV = r'/='
t_ASIGNACIONMOD = r'%='
t_ASIGNACIONEXP = r'\*\*='
t_IGUAL_COMP=r"=="
t_DIFERENTE=r"!="
t_MENOR=r"<"
t_MAYOR=r">"
t_AND=r"&&"
t_OR=r"\|\|"
t_IZQ_CORCH = r"\["
t_DER_CORCH = r"\]"
t_IZQ_LLAVE = r"\{"
t_DER_LLAVE = r"\}"
t_COMILLASIMPLE  = r"\'"
t_COMILLADOBLE  = r"\""
#Fin Inicio Hayleen Carrillo


# General
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'


lexer = lex.lex()

# Pruebas
data = '''
    3 + 4.4 * 10
    + -20 *2 /5
    $var_global 
    @@var_clase
    @var_insta
    CONSTANTE2
    var_local
    if
    5%3
    4852**233
    a*=5
    a==5
    3!=85
    (3==3) && (8!=90)
    654>78
    [aaa]
    {bbb}
    '"

'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)