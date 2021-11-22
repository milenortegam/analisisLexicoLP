import ply.yacc as yacc


'''
LO QUE FALTA
Operaciones matematicas
Creacion de listas (uso de corchetes), tuplas (uso de llaves?)
Retorno en funciones!!!

PARTE DE MILEN

'''
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
sentFor
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
    ''' sentencias :

                    | sentIf
                    | sentFor
                    | sentWhile
                    | unless

                    | sentenciaBloque
                    | sentenciaFuncion
                    | pop
                    | push
                    | clear

    '''

'''Inicio Milen Ortega'''


'''Fin Milen Ortega'''



'''Inicio Gabriela Pazmiño'''

def p_variables(p):
    '''variables : VGLOBALES
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
                    | IZQPAREN expresion DERPAREN operadorComparador IZQPAREN expresion DERPAREN
    '''

def p_operadorComparador (p):
    '''operadorComparador : IGUAL_COMP
            | DIFERENTE
            | MENOR
            | MAYOR
    '''
def p_sentAnd(p):
    ''' sentAnd : comparacion AND comparacion
    '''

def p_sentOr(p):
    ''' sentOr : comparacion OR comparacion
    '''

def p_comparaciones(p):
    ''' comparaciones : comparacion
                      | sentAnd
                      | sentOr
    '''

def p_rango(p):
    ''' rango : NUMERO RANGO NUMERO
    '''


def p_sentBreak(p):
    ''' sentBREAK : BREAK
            | BREAK variables
    '''

def p_sentIf(p):
    ''' sentIf : IF comparaciones base finalIf
    '''

def p_finalIf(p):
    ''' finalIf : END
                | sentBREAK END
    '''

def p_sentFor(p):
    ''' sentFor : FOR variables IN rango DO base END
    '''

def p_sentWhile(p):
    '''sentWhile : WHILE  comparacion DO base END
    '''


def p_unless(p):
    ''' unless : UNLESS comparacion base END
    '''

def p_listas(p):
    ''' listas: IZQ_CORCH expresion COMA expresion DER_CORCH
    '''

def p_mapas(p):
    ''' mapa: IZQ_LLAVE expresion COMA expresion DER_LLAVE
    '''

'''Fin Gabriela Pazmiño'''



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
    ''' pop : variables PUNTO POP  IZQPAREN valor DERPAREN
            | variables PUNTO POP IZQPAREN DERPAREN
    '''

def p_push(p):
    ''' push : variables PUNTO PUSH  IZQPAREN valor DERPAREN
    '''


def p_clear(p):
    ''' clear : variables PUNTO PUSH IZQPAREN DERPAREN
    '''

'''Fin Hayleen Carrillo'''


#errores
def p_error(p):
     print("Syntax error in input!")

     # Build the parser


parser = yacc.yacc()

