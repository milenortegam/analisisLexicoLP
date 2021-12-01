import ply.yacc as yacc
from analizadorLexico import *

'''Reglas definidas por Milen Ortega
asignacion-
append-
split-
slicing-
puts-
comentarios-
'''

'''Reglas definidas por Gabriela Pazmiño
sentIf
sentFor
sentWHILE
unless
listas
mapas
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
                    | puts
                    | comentarios
                    | sentIf
                    | sentFor
                    | sentWhile
                    | unless
                    | sentenciaBloque
                    | sentenciaFuncion
                    | pop
                    | push
                    | clear
                    | operacionMat
                    | slice
                    | print
                    | listas
                    | mapas
                    | booleanos
                    | reglaSemanticaCondiciones

    '''
    p[0] = p[1]

#Inicio Milen Ortega
def p_asignacion(p):
    '''asignacion : variables IGUAL expresion
    '''

def p_split(p):
    '''split : variables PUNTO SPLIT IZQPAREN DERPAREN
                | variables PUNTO SPLIT IZQPAREN CADENAS DERPAREN
                | variables PUNTO SPLIT IZQPAREN CADENAS COMA NUMERO DERPAREN
    '''

def p_puts(p):
    '''puts : PUTS expresion
            | PUTS IZQPAREN expresion DERPAREN
            | PUTS IZQPAREN comparacion DERPAREN
    '''

def p_print(p):
    '''print : PRINT expresion
            | PRINT IZQPAREN expresion DERPAREN
            | PRINT IZQPAREN comparacion DERPAREN
    '''

def p_comentarios(p):
    '''comentarios : COMENTARIO 
    '''

def p_append(p) :
    '''append : variables PUNTO APPEND IZQPAREN expresion DERPAREN
    '''

def p_slice(p) :
    '''slice : ARREGLOS PUNTO SLICE IZQPAREN NUMERO DERPAREN
            | variables PUNTO SLICE IZQPAREN NUMERO DERPAREN
            | variables PUNTO SLICE IZQPAREN NUMERO COMA NUMERO DERPAREN
            | ARREGLOS PUNTO SLICE IZQPAREN NUMERO COMA NUMERO DERPAREN
    '''
def p_booleanos(p) :
    '''booleanos : TRUE
                | FALSE
    '''

def p_valorNumerico(p) :
    '''valorNumerico : NUMERO
                | FLOTANTES
    '''

#Fin Milen Ortega



#Inicio Gabriela Pazmiño

def p_variables(p):
    '''variables : VGLOBALES
                | VLOCALES
                | VCLASE
                | VINSTANCIA
                | CONSTANTES
    '''

def p_valor(p):
    '''valor : valorNumerico
            | CADENAS
            | ARREGLOS
            | MAPAS
            | variables
    '''

def p_valor_Matematico(p):
    '''valor_Matematico : NUMERO
            | FLOTANTES
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
                | IF comparaciones base ELSIF comparaciones base finalIf
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
    ''' listas : IZQ_CORCH expresion COMA expresion DER_CORCH
    '''

def p_mapas(p):
    ''' mapas : IZQ_LLAVE expresion COMA expresion DER_LLAVE
    '''

#Fin Gabriela Pazmiño



#Inicio Hayleen Carrillo

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
    ''' clear : variables PUNTO CLEAR IZQPAREN DERPAREN
    '''

def p_operacionMat(p):
    ''' operacionMat : valor operadorMat valor
                        | IZQPAREN valor operadorMat expresion DERPAREN
                        | IZQPAREN valor operadorMat expresion DERPAREN operadorMat operacionMat
                        | valor operadorMat valor operadorMat operacionMat
                        | operacionMat operadorMat operacionMat
    '''


def p_operadorMat(p):
    ''' operadorMat : MAS
             | MENOS
             | MULTIPLICACION
             | DIVISION
             | EXPONENCIAL
             | MODULO
    '''

#Fin Hayleen Carrillo


#errores
def p_error(p):
     print("Syntax error in input!")

##Reglas Semánticas

#Inicio Milen Ortega
def p_reglaSemanticaCondiciones(p):
    '''reglaSemanticaCondiciones : valorNumerico IGUAL_COMP valorNumerico
                                | valorNumerico DIFERENTE valorNumerico
                                | valorNumerico MENOR valorNumerico
                                | valorNumerico MAYOR valorNumerico
                                | valorNumerico OR valorNumerico
                                | valorNumerico AND valorNumerico
                                | CADENAS IGUAL_COMP CADENAS
                                | CADENAS DIFERENTE CADENAS
                                | CADENAS MENOR CADENAS
                                | CADENAS MAYOR CADENAS
                                | CADENAS OR CADENAS
                                | CADENAS AND CADENAS
                                | booleanos IGUAL_COMP booleanos
                                | booleanos DIFERENTE booleanos
                                | booleanos OR booleanos
                                | booleanos AND booleanos
                                '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '==':
        p[0] = p[1]== p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]




#contruccion del parser
parser = yacc.yacc()



data = [
        'PUTS "Hola"', 'PUTS ("Hola")', 'PUTS a=10', 'PUTS [1, 2, 3]', 'PRINT "Hola"', 'PRINT ("Hola")', 'PRINT a = 10', 'PRINT [1, 2, 3]',
        '#asdas', 'arreglo.APPEND(10)', 'arreglo2.APPEND("Hola")', '[1, 2, 3, 4].SLICE(2)', '[1, 2, 3, 4].SLICE(1, 3)', 'variable.SLICE(2)',
        'variable.SLICE(1, 3)', 'a<b', "10!=30", 'FOR a in 1..2 DO PUTS a=3 END', 'WHILE 10<8 DO PUTS "Hola" END', 'UNLESS a!=10 DO PUTS "Hola" END',
        '[10, 9]', '\{10, 9\}', 'BEGIN PUTS a=3 END', 'DEF suma 8+8 END', 'a.POP("hola")','a.POP()', 'a.PUSH("hola")', 'a.CLEAR()',
        '7+7+7%7+7-7+7*7/7-7']


data = ["true<false"]

#algoritmo para validar

'''
for s in data:
    if not s: continue
    result = parser.parse(s)
    print(result, s)
'''



def inputSint(cadena):
    result = parser.parse(cadena)
    print(result)
    return str(result)




# while True:
#    try:
#        s = input('Python > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

#reglas Semanticas
def p_regla_Semantica_Operaciones_Matematicas(p):
    '''p_regla_Semantica_Operaciones_Matematicas : valor_Matematico MAS valor_Matematico
                                                  | valor_Matematico MENOS valor_Matematico
                                                  | valor_Matematico MULTIPLICACION valor_Matematico
                                                  | valor_Matematico DIVISION valor_Matematico
                                                  | valor_Matematico EXPONENCIAL valor_Matematico
                                                  | valor_Matematico MODULO valor_Matematico
    '''


def p_regla_Semantica_Operaciones(p):
    '''p_regla_Semantica : valor operadorMat valor
                              | operacionMat operadorMat valor
    '''
    if (type(p[1]) != type(p[3])):
        print("No se puede realizar la operacion matematica por que los valores no son del mismo tipo")

