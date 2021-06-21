
def isKeyword(string):
    keywords = ["auto","break","case","const","continue","default","do","else","enum","extern","for","goto",
    "if","register","return","sizeof","static","struct","switch","typedef","union","void","volatile","while"]

    if string in keywords:
        return True
    return False

def isOperator(string):
    list = ['+','-','/']

    if(string in list):
        return True
    return False

def isValue(string):
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

def isOptType(string):
    list = ['short']

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
    keyword = 11
    pointVirg = 12
    etoile = 13
    par1 = 14
    par2 = 15
    curly1 = 16
    curly2 = 17
    croch1 = 18
    croch2 = 19
    virgule = 20
    deuxPoints = 21

type = []
words = ["ahdi", "a", "\'++\"", "\"++\"",  "++",  "static", ";", "ahdi", "'hello'", "null", ']']
tab = []
for cpt in range(len(words)):
    tab.append([words[cpt], 0])
    if len(words[cpt]) == 1:
        if isOperator(words[cpt]):
            tab[cpt][1] = 2
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
        elif words[cpt] == ',':
            tab[cpt][1] = 20
        elif words[cpt] == ':':
            tab[cpt][1] = 21
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
        elif isKeyword(words[cpt]):
            tab[cpt][1] = 11
        elif words[cpt].isidentifier():
            tab[cpt][1] = 1
            
cpt = 0
for i in Type:
   print(i , " : ", cpt)
   cpt +=1

c = chr(65+3)
print(c)
string = ''
for word in tab:
    c = chr(65+word[1])
    string += c

print(words)
print(tab) 
print(string)



