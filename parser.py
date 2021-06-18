import re

def isKeyword(string):
    keywords = ["auto","break","case","char","const","continue","default",
    "do","double","else","enum","extern","float","for","goto",
    "if","int","long","register","return","short","signed",
    "sizeof","static","struct","switch","typedef","union",
    "unsigned","void","volatile","while"]

    if string in keywords:
        return True
    return False

def isDelimiter(string):
    delimiters = [' ', '*', '/', ',', ';', '(', ')', '[', ']', '{', '}']
    if(string in delimiters):            
        return 1
    elif(string in ['=', '<', '>', '+', '-']):
        return 2
    else:
        return 0


def isOperator(string):
    operators = ['+','-', '*', '/', '>', '<']

    if(string in operators):
        return True
    return False


def subString(string, left, right):
    subStr = ''
    for i in range(left, right+1):
        subStr += string[i]
    
    return subStr

# Parsing the input STRING.
def parse(text):
    right = 0
    left = 0
    while right < len(text) and left <= right:
        delim = isDelimiter(text[right])
        #if its not a delimiter we keep going for the next character
        if delim == 0:
            right +=1
        #if its a delimiter an its only on character
        elif delim == 1 and left == right: 
            #We check if its an operator
            if isOperator(text[right]) == True:
                word.append(text[right])
                type.append('operator')
                print(text[right], " IS AN OPERATOR\n")
            #We move on to the next 'word'
            right+=1
            left = right

        #if its an ambiguous delimiter ("=", "+", "-")
        elif(delim == 2 and left == right):
            #check for the next character
            subStr = subString(text, left, right+1)
            if(subStr == '++' or subStr == '--'):
                print(subStr, " IS A INCREMENTOR\n")
                word.append(subStr)
                type.append('incrementor')
                right+=2
                left = right  
            elif (subStr == '<=' or subStr == '>=' or subStr == '=='):
                print(subStr, " IS A COMPARATOR\n")
                word.append(subStr)
                type.append('comparator')
                right+=2
                left = right 
            elif(text[right] == '<' or text[right] == '>'):
                print(text[right], " IS A COMPARATOR\n")
                word.append(text[right])
                type.append('comparator')
                right+=1
                left = right
            else:
                print(text[right], " IS AN AFFECTATION OPERATOR\n")
                word.append(text[right])
                type.append('operator')
                right+=1
                left = right
        
        elif (delim == 1 or delim == 2) and left != right or (right == len(text) and left != right):
            subStr = subString(text, left, right - 1)
            if (isKeyword(subStr) == True):
                word.append(subStr)
                type.append('keyword')
                print( subStr, " IS A KEYWORD\n")
  
            elif (subStr.isidentifier() == True and isDelimiter(text[right - 1]) == 0):
                word.append(subStr)
                type.append('identifier')
                print(subStr, " IS A VALID IDENTIFIER\n")
  
            elif (subStr.isnumeric() == True or subStr.replace('.','',1).isdigit()):
                word.append(subStr)
                type.append('number')
                print(subStr, " IS A NUMBER\n")

            else:
                print(subStr ," IS NOT A VALID IDENTIFIER\n")
                word.append(subStr)
                type.append('invalid')
            left = right
    return 0

def remove_nwline(s) :
    return "".join([i for i in s if i!='\n'])

text = open("test.txt", "r")
text = text.read()
text = remove_nwline(text)
type = [] #Contains the type of a word (comparator, operator etc.) 
word = [] 
parse(text)
for i in range(len(word)):  
    print(word[i], " : ", type[i])
print(word)
print(type)
print(text)










