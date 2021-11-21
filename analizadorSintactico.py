import ply.yacc as yacc

from analizadorLexico import tokens

'''Reglas definidas por Milen Ortega
asignacion
append
split
slicing
puts
comentarios
'''

'''Reglas definidas por Gabriela Pazmiño
sentIf
sentFOR
sentWHILE
unless
'''

'''Reglas definidas por Hayleen Carrillo
sentenciaBloque
sentenciaFuncion
pop
push
clear
'''

def p_base(p):
    '''base : sentencias
                | sentencias base
    '''

def p_sentencias(p):
    ''' sentencias : asignacion
                    | append
                    | split
                    | slicing

                    | sentenciaIf
                    | sentenciaFOR
                    | sentenciaWHILE
                    | unless

                    | sentenciaBegin
                    | sentenciaFuncion
                    | pop
                    | push
                    | clear

                    | puts
                    | comentarios

    '''


# Error rule for syntax errors

'''Inicio Gabriela Pazmiño'''

def p_variables(p):
    '''variables : VARIABLE_LOCAL
                | VGLOBALES
                | VLOCALES
                | VCLASE
                | VINSTANCIA
                | CONSTANTES
    '''

def p_valor(p):
    '''valor : NUMERO
            | FLOTANTES
            | CADENAS
            | ARREGLOS
            | MAPAS
            | variables
    '''

def p_expresion(p):
    ''' expresion : valor
    '''

def p_comparacion(p):
    '''comparacion : expresion operadorComparador expresion
        | IZQPAREN expresion DERPAREN operadorComparador expresion
        | IZQPAREN expresion operadorComp operadorComparador DERPAREN
    '''

def p_sentAnd(p):
    ''' sentAND : comparacion AND comparacion
    '''

def p_sentOr(p):
    ''' sentOR : comparacion OR comparacion
    '''

def p_comparaciones(p):
    ''' comparaciones : comparacion
                      | sentAND
                      | sentOR
    '''

def p_rango(p):
    ''' rango : NUMERO RANGO NUMERO
    '''

def p_sentDef(p):
    ''' p_sentDef : DEF  variables base  END
    '''

def p_sentBreak(p):
    ''' sentBREAK : BREAK
            | BREAK variables
    '''

def p_sentBegin(p):
    '''sentBegin : BEGIN base END'''

def p_sentIf(p):
    ''' sentIf : IF comparaciones base finalIf
    '''

def p_finalIf(p):
    ''' finalIf : END
                | sentBREAK END
    '''

def p_sentFor(p):
    ''' sentFOR : FOR variables IN rango DO base END
    '''

def p_sentWhile(p):
    '''sentWHILE : WHILE  comparacion DO base END
    '''


def p_unless(p):
    ''' unless : UNLESS comparacion base END
    '''

'''Fin'''



'''Inicio Hayleen Carrillo'''

def p_sentenciaBloque(p):
    ''' sentenciaBloque : BEGIN base END
    '''

def p_sentenciaFuncion(p):
    '''sentenciaFuncion : DEF variables base END
                        | DEF variables parametrosF base END
    '''

def p_parametrosF(p):
    ''' parametrosF : IZQPAREN parametros DERPAREN
    '''

def p_parametros(p): #analizar variables
    ''' parametros : variables COMA variables
                    | variables
                    | parametros COMA parametros
    '''

def p_pop(p):
    ''' pop: variables PUNTO POP
    '''

def p_push(p):
    ''' push: variables PUNTO PUSH
    '''


def p_clear(p):
    ''' clear: variables PUNTO PUSH
    '''


#errores
def p_error(p):
     print("Syntax error in input!")

     # Build the parser


parser = yacc.yacc()

while True:
    try:
        s = print('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)