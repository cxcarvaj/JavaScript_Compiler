import ply.yacc as sintaxis
import lexico
tokens = lexico.tokens


def p_sentencias(p):
    '''sentencias : statement
    | if
    | for
    | while
    | statement sentencias
    | if sentencias
    | while sentencias
    | for sentencias'''

def p_statements(p):
    '''statement : stm
    | stm SEMICOLON'''

def p_stm_asignacion(p):
    'stm : asignacion'

def p_stm_asignacion_date(p):
    'stm : asignacion_date'


def p_stm_array(p):
    'stm : array'

def p_stm_set(p):
    'stm : set'

def p_stm_expression(p):
    'stm : expresion'

def p_stm_metodos(p):
    'stm : metodos'

def p_metodos(p):
    '''metodos : imprimir
    | touppercase
    | tolowercase
    | startwith
    | tostring
    | pop
    | push
    | shift
    | setdate
    | getfullyear
    | has
    | intersection
    | union'''

def p_imprimir(p):
    'imprimir : PRINT LPAREN factor RPAREN'



def p_to_upper_case(p):
    '''touppercase : ID TOUPPERCASE LPAREN RPAREN
    | type ID EQUAL ID TOUPPERCASE LPAREN RPAREN'''


def p_to_lower_case(p):
    '''tolowercase : ID TOLOWERCASE LPAREN RPAREN
    | type ID EQUAL ID  TOLOWERCASE LPAREN RPAREN'''

def p_start_with(p):
    '''startwith : ID STARTSWITH LPAREN STRING RPAREN
    | type ID EQUAL ID STARTSWITH LPAREN STRING RPAREN'''

def p_to_string(p):
    '''tostring : ID TOSTRING LPAREN RPAREN
        | type ID EQUAL ID  TOSTRING LPAREN RPAREN'''

def p_pop(p):
    '''pop : ID POP LPAREN RPAREN
    | type ID EQUAL ID POP LPAREN RPAREN'''

def p_push(p):
    '''push : ID PUSH LPAREN factor RPAREN
    | type ID EQUAL ID PUSH LPAREN factor RPAREN'''

def p_shift(p):
    '''shift : ID SHIFT LPAREN RPAREN
    | type ID EQUAL ID SHIFT LPAREN RPAREN'''

def p_set_date(p):
    '''setdate : ID SETDATE LPAREN NUMBER RPAREN
    | type ID EQUAL ID SETDATE LPAREN NUMBER RPAREN'''

def p_get_full_year(p):
    '''getfullyear : ID GETFULLYEAR LPAREN RPAREN
    | type ID EQUAL ID GETFULLYEAR LPAREN RPAREN'''

def p_has(p):
    '''has : ID HAS LPAREN factor RPAREN
    | type ID EQUAL ID HAS LPAREN factor RPAREN'''

def p_intersection(p):
    '''intersection : ID INTERSECTION LPAREN set_parametro RPAREN
    | type ID EQUAL ID INTERSECTION LPAREN set_parametro RPAREN'''

def p_union(p):
    '''union : ID UNION LPAREN set_parametro RPAREN
    | type ID EQUAL ID UNION LPAREN set_parametro RPAREN'''


def p_while(p):
    '''while : WHILE LPAREN condicion RPAREN LBRACE sentencias RBRACE'''

def p_if(p):
    '''if : IF LPAREN condicion RPAREN LBRACE sentencias RBRACE
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE else
    | IF LPAREN condicion RPAREN LBRACE sentencias RBRACE elseif'''

def p_condicion(p):
    '''condicion : TRUE
    | FALSE
    | NOT expresion
    | expresion operadorlogico expresion
    | LPAREN condicion RPAREN operadorlogico expresion
    | expresion operadorlogico LPAREN condicion RPAREN
    | expresion operador_comparison expresion'''

def p_else(p):
    'else : ELSE LBRACE sentencias RBRACE'

def p_else_if(p):
    'elseif : ELSE IF LPAREN condicion RPAREN LBRACE sentencias RBRACE else'

def p_for(p):
    '''for : FOR LPAREN type ID OF ID RPAREN LBRACE sentencias RBRACE'''

def p_asignacion(p):
    '''asignacion : ID EQUAL expresion
    | declaracion'''

def p_asignacion_new_date(p):
    '''asignacion_date : type ID EQUAL NEW DATE LPAREN RPAREN
    | type ID EQUAL NEW DATE LPAREN date_param RPAREN'''

def p_array(p):
    '''array : type ID EQUAL LBRACKET RBRACKET
    | type ID EQUAL LBRACKET arr_parametro RBRACKET'''


def p_set(p):
    '''set : type ID EQUAL NEW SET LPAREN RPAREN
    | type ID EQUAL NEW SET LPAREN set_parametro RPAREN'''

def p_arr_parametro(p):
    '''arr_parametro : expresion
    | expresion COMMA arr_parametro'''

def p_set_parametro(p):
    '''set_parametro : LBRACKET arr_parametro RBRACKET
    | ID'''

def p_declaracion(p):
    '''declaracion : type ID EQUAL expresion'''

def p_date_param(p):
    '''date_param : STRING
    | NUMBER
    | NUMBER COMMA NUMBER
    | NUMBER COMMA NUMBER COMMA NUMBER
    '''


def p_type(p):
    '''type : VAR
    | LET'''

def p_expresion_operacion(p):
    '''expresion : NUMBER operador NUMBER'''


def p_operador(p):
    '''operador : MINUS
    | PLUS
    | DIVIDE
    | TIMES
    | MOD'''


def p_operador_logico(p):
     '''operadorlogico : EQUALS
     | NOTEQUALS
     | STRICTEQUALS
     | MORETHAN
     | LESSTHAN
     | MORETHANEQUALS
     | LESSTHANEQUALS
     | STRICTNOTEQUALS'''

def p_operador_comparison(p):
     '''operador_comparison : AND
     | OR'''


def p_expresion_term(p):
    'expresion : term'

def p_term_factor(p):
    'term : factor'

def p_factor_id(p):
    'factor : ID'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_str(p):
    'factor : STRING'

def p_factor_bool(p):
    '''factor : TRUE
    | FALSE '''


#Error Generado
def p_error(p):
    try:
        token = "Token {} ({}) En la linea {}".format(p.type, p.value, p.lineno)
        print("Syntax error: Inesperado {}".format(token))
    except:
        if p == None:
            print("Su sentencia está incompleta")
        else:
            print("Sytax error: Inesperado {} En la linea 1 ".format(p))
    p.lineno=0



def analisis_sintactico():
    try:
        with open('data.txt','r') as file:
            cadena = file.read()
        print_Yacc(cadena)
    except:
        print("")

def print_Yacc(cadena):
    parser = sintaxis.yacc()
    while True:
        if not cadena: continue
        result = parser.parse(cadena,tracking=False)
        print(result)
        break


# def parser_Console():
#     parser=sintaxis.yacc()
#     while True:
#         try:
#             s = input('JavaScript > ')
#         except EOFError:
#             break
#         if not s: continue
#         result = parser.parse(s,tracking=True)
#         print(result)
#         break


analisis_sintactico()
