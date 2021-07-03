def isOperator(string):
    list = ['+','-','/']

    if(string in list):
        return True
    return False

def isValue(string):
    #print('AAAAAAAAAAAAAAAAAAAAAAAAAA')
    #print(string)
    if (string.isnumeric() == True or string.replace('.','',1).isdigit()) or ((string[0] == "'" and string[-1]) == "'" or (string[0] == "\"" and string[-1] == "\"")):
        return True
    return False

def isComparator(string):
    list = ['<','>', '<=', '>=', '==', '!=']

    if(string in list):
        return True
    return False

def isIterrator(string):
    list = ['++','--']

    if(string in list):
        return True
    return False

def isAffectation(string):
    list = ['=','+=','-=']

    if(string in list):
        return True
    return False

def isType(string):
    list = ['char','int','float', 'double', 'void']

    if(string in list):
        return True
    return False


import enum
  
# creating enumerations using class
class Type(enum.Enum):
    notDefined = 0
    id = 1
    operator = 2
    value = 3
    comparator = 4
    itterrator = 5
    affectation = 6
    type = 7
    optionType = 8
    sign = 9
    long = 10
    virgule = 11
    pointVirg = 12
    etoile = 13
    par1 = 14
    par2 = 15
    curly1 = 16
    curly2 = 17
    croch1 = 18
    croch2 = 19
    deuxPoints = 20
    whil = 21
    aut = 22
    brea = 23
    case = 24
    const = 25
    cont = 26
    default = 27
    do = 28
    els = 29
    enum = 30
    extern = 31
    f = 32
    goto = 33
    i = 34
    register = 35
    ret = 36
    sizeof = 37
    static = 38
    struct = 39
    switch = 40
    typedef = 41
    union = 42
    void = 43
    volatile = 44

def findType(words):
    tab = []
    for cpt in range(len(words)):
        tab.append([words[cpt], 0])
        if len(words[cpt]) == 1:
            if isOperator(words[cpt]):
                tab[cpt][1] = 2
            if isValue(words[cpt]) or words[cpt] == 'NULL':
                tab[cpt][1] = 3
            elif isComparator(words[cpt]):
                tab[cpt][1] = 4
            elif isAffectation(words[cpt]):
                tab[cpt][1] = 6
            elif words[cpt] == ',':
                tab[cpt][1] = 11
            elif words[cpt] == ';':
                tab[cpt][1] = 12
            elif words[cpt] == '*':
                tab[cpt][1] = 13
            elif words[cpt] == '(':
                tab[cpt][1] = 14
            elif words[cpt] == ')':
                tab[cpt][1] = 15
            elif words[cpt] == '{':
                tab[cpt][1] = 16
            elif words[cpt] == '}':
                tab[cpt][1] = 17
            elif words[cpt] == '[':
                tab[cpt][1] = 18
            elif words[cpt] == ']':
                tab[cpt][1] = 19
            elif words[cpt] == ':':
                tab[cpt][1] = 20
            elif words[cpt].isidentifier():
                tab[cpt][1] = 1
        else:
            if isValue(words[cpt]) or words[cpt] == 'NULL':
                tab[cpt][1] = 3
            elif isComparator(words[cpt]):
                tab[cpt][1] = 4
            elif isIterrator(words[cpt]):
                tab[cpt][1] = 5
            elif isAffectation(words[cpt]):
                tab[cpt][1] = 6
            elif isType(words[cpt]):
                tab[cpt][1] = 7
            elif words[cpt] == "short":
                tab[cpt][1] = 8
            elif words[cpt] == "signed" or words[cpt] == "unsigned":
                tab[cpt][1] = 9
            elif words[cpt] == "long":
                tab[cpt][1] = 10
            elif words[cpt] == "while":
                tab[cpt][1] = 21
            elif words[cpt] == "auto":
                tab[cpt][1] = 22
            elif words[cpt] == "break":
                tab[cpt][1] = 23
            elif words[cpt] == "case":
                tab[cpt][1] = 24
            elif words[cpt] == "const":
                tab[cpt][1] = 25
            elif words[cpt] == "continue":
                tab[cpt][1] = 26
            elif words[cpt] == "default":
                tab[cpt][1] = 27
            elif words[cpt] == "do":
                tab[cpt][1] = 28
            elif words[cpt] == "else":
                tab[cpt][1] = 29
            elif words[cpt] == "enum":
                tab[cpt][1] = 39
            elif words[cpt] == "extern":
                tab[cpt][1] = 31
            elif words[cpt] == "for":
                tab[cpt][1] = 32
            elif words[cpt] == "goto":
                tab[cpt][1] = 33
            elif words[cpt] == "if":
                tab[cpt][1] = 34
            elif words[cpt] == "register":
                tab[cpt][1] = 35
            elif words[cpt] == "return":
                tab[cpt][1] = 36
            elif words[cpt] == "sizeof":
                tab[cpt][1] = 37
            elif words[cpt] == "static":
                tab[cpt][1] = 38
            elif words[cpt] == "struct":
                tab[cpt][1] = 39
            elif words[cpt] == "switch":
                tab[cpt][1] = 40
            elif words[cpt] == "typedef":
                tab[cpt][1] = 41
            elif words[cpt] == "union":
                tab[cpt][1] = 42
            elif words[cpt] == "void":
                tab[cpt][1] = 43
            elif words[cpt] == "volatile":
                tab[cpt][1] = 44  
            elif words[cpt].isidentifier():
                tab[cpt][1] = 1
    return tab

def to_ascii(tab) :
    string = ''
    for word in tab:
        c = chr(65 + word[1])
        string += c
    return string

def lex_to_str(t) :
    return [to_ascii(findType(i)) for i in t]

#keywords = ["while", "auto","break","case","const","continue","default","do","else","enum","extern","for","goto","if","register","return","sizeof","static","struct","switch","typedef","union","void","volatile"]


