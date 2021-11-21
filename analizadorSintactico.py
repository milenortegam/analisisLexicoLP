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
def p_error(p):
     print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
