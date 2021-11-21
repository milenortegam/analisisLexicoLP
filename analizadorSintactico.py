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
sentenciaIf
sentenciaFOR
sentenciaWHILE
sentenciaCASE
unless
'''

'''Reglas definidas por Hayleen Carrillo
sentenciaBegin
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
                    | sentenciaCASE
                    | unless

                    | sentenciaBegin
                    | sentenciaFuncion
                    | pop
                    | push
                    | clear

                    | puts
                    | comentarios

    '''



sentenciaBegin
sentenciaFuncion
pop
push
clear
def p_pop(p):


# Error rule for syntax errors
=======
'''Inicio Gabriela Pazmiño'''

def p_sentenciaFuncion(p):
    ''' sentenciaFuncion : FUNCION  variables codigo  END
    '''

def p_sentenciaAnd(p):
    ''' sentenciaAND : comparacion AND comparacion
    '''

def p_sentenciaOr(p):
    ''' sentenciaOR : comparacion OR comparacion
    '''

def p_sentenciaBegin(p):
    '''sentenciaBegin : BEGIN codigo END'''

def p_sentenciaIf(p):
    ''' sentenciaIf : IF comparaciones codigo finalIf
    '''

def p_finalIf(p):
    ''' finalIf : END
                | sentenciaBREAK END
    '''

def p_sentenciaFor(p):
    ''' sentenciaFOR : FOR variables IN range DO codigo END
    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion DO codigo END
    '''

def p_sentenciaCase(p):
    ''' sentenciaCASE : CASE variables sentenciaWhens ELSE codigo END
    '''

def p_unless(p):
    ''' unless : UNLESS comparacion codigo END
    '''

#errores

def p_error(p):
     print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
