import ply.lex as lex
#RESERVED WORDS
reserved = {
    'var': 'VAR', 'let':'LET' ,
    'new':'NEW',
    'if':'IF', 'else':'ELSE', 'while':'WHILE', 'for':'FOR',
    '||':'OR', '&&':'AND', '!':'NOT'  ,
    'true':'TRUE', 'false':'FALSE',
    'of': 'OF',
    'Date': 'DATE'

}

#RESERVED FUNCTION NAMES
function = {
    '\.toUpperCase':'TOUPPERCASE',
    '\.toLowerCase': 'TOLOWERCASE',
    '\.startsWith': 'STARTSWITH',
    '\.pop':'POP',
    '\.push':'PUSH',
    '\.shift':'SHIFT',
    '\.setDate':'SETDATE', '\.toString':'TOSTRING', '\.getFullYear':'GETFULLYEAR',
    '\.has':'HAS' ,  '\.intersection':'INTERSECTION', '\.union':'UNION',
    'Set': 'SET'
}

literals = ['{', '}']

# TOKENS
tokens = ["PRINT","MINUS","PLUS","TIMES","DIVIDE","MOD","LPAREN","RPAREN","ID", "EQUAL",
          "LBRACKET","RBRACKET","EQUALS","NOTEQUALS","MORETHAN","LESSTHAN",
          "MORETHANEQUALS","LESSTHANEQUALS","STRICTEQUALS","STRICTNOTEQUALS",
          "SEMICOLON", "COMMA", "NEWLINE", "LBRACE", "RBRACE",
          "NUMBER", "STRING"] + list(reserved.values()) + list(function.values())

#REGEX OF TOKENS
t_TOUPPERCASE = r'.toUpperCase'
t_TOLOWERCASE = r'.toLowerCase'
t_STARTSWITH = r'.startsWith'
t_POP = r'.pop'
t_PUSH = r'.push'
t_SHIFT = r'.shift'
t_SETDATE = r'.setDate'
t_TOSTRING = r'.toString'
t_GETFULLYEAR = r'.getFullYear'
t_HAS = r'.has'
t_INTERSECTION = r'.intersection'
t_UNION = r'.union'
t_MINUS = r'-'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_NUMBER = r'-?[0-9]+(\.\d+)?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUAL = r'\='
t_EQUALS = r'\=\='
t_NOTEQUALS = r'\!\='
t_MORETHAN = r'\>'
t_LESSTHAN = r'\<'
t_MORETHANEQUALS = r'\>\='
t_LESSTHANEQUALS = r'\<\='
t_STRICTEQUALS = r'\=\=\='
t_STRICTNOTEQUALS = r'\!\=\='
t_IF = r'if'
t_FOR = r'for'
t_WHILE = r'while'
t_ELSE = r'else'
t_NEW = r'new'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_NOT = r'!'
t_SEMICOLON = r';'
t_COMMA = r'\,'
t_STRING= r'[\"][A-Za-z0-9\s\.\,\:\-]+[\"] | [\'][A-Za-z0-9\s\.\,\:\-]+[\']'

t_ignore = ' \t'

def t_lbrace(t):
    r'\{'
    t.type = 'LBRACE'
    return t

def t_rbrace(t):
    r'\}'
    t.type = 'RBRACE'
    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += (t.value.count("\n") + 1)
    #t.type = "NEWLINE"
    #pass


def t_PRINT(t):
    r'console\.log'
    t.type = "PRINT"
    return t

def t_ID(t):
    r'[$_]?[a-zA-Z][a-zA-Z_0-9\$]*'
    #t.value = t.value.encode('unicode_escape')
    #t.value = t.value.replace(".","\.")
    if reserved.get(t.value)!=None:
        t.type = reserved.get(t.value)
    elif function.get(t.value)!=None:
        t.type = function.get(t.value)
    else:
        t.type= 'ID'  # Check for reserved words
    return t

def printLex(cadena):
    try:
        with open('data.txt','r') as file:
            cadena += file.read()
        print_Lexer(cadena)
    except:
        print_Lexer(cadena)

def print_Lexer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    for tok in analizador:
        print(tok)

def t_COMMENT(t):
     r'(\/\/.*)|(\/\*.*\*\/)'
     pass

def t_error(t):
    print("No se ha reconocido en lexico {}".format(t.value[0]))
    t.lexer.skip(1)

analizadorL = lex.lex()
printLex("")
################## EJEMPLOS ###########
#print(function.get(".toLowerCase"),function.keys())
#print("EJEMPLOS\n")
# cadena= "let example = \"hello\" of 5;"
#cadena="if(a>5){\nb=5}"
# cadena2= "a.toLowerCase()"
# cadena3 = "function hola(){hola=5}"
# cadena4 = "console.log(hola)"
# cadena5 = "var example = \"\""
# cadena6 = "example = 2"
# cadena7 = "true===1"
# cadena8 = "var arr = [1,2.5,3]"
# cadena9 = "carro = {\"llanta\",\"luces\"}"
#print(cadena)
#printLex(cadena)
# print("\n",cadena2)
# printLex(cadena2)
# print("\n",cadena3)
# printLex(cadena3)
# print("\n",cadena4)
# printLex(cadena4)
# print("\n",cadena5)
# printLex(cadena5)
# print("\n",cadena6)
# printLex(cadena6)
# print("\n",cadena7)
# printLex(cadena7)
# print("\n",cadena8)
# printLex(cadena8)
# print("\n",cadena9)
# printLex(cadena9)
#cadenas =["let  example = \"hello\";", "a.toLowerCase()","if(a>5){\nb=5}","if(a>5){hola}else if{adios}else{adios de nuveo}" ]
# cadenas1 = ["function hola(){hola=5}","console.log(hola)", "let array = [1,2,4]" ]
# cadenas2=["var cambio= texto.startsWith(\"Este\");", "var ultimo= a.pop();", "var texto= fecha.toString();"]
'''
for example in cadenas:
   printLex(example)
   print("\n\n")
'''
# for example in cadenas1:
#     printLex(example)
#     print("\n\n")
#
# for example in cadenas2:
#     printLex(example)
#     print("\n\n")
