def sashimi_char(st,c):
    tab = []
    it = 0
    a = 0
    while st[a] == c :
        it += 1
        tab.append(c)
        a +=1
    tab.append(st[a])
    a+=1
    for i in st[a:] :
        if i==c :
            it += 2
            tab.append(c)
            if a != len(st) - 1:
                tab.append('')
        else :
            tab[it] = tab[it] + i
        a += 1
    return tab
"""

def sashimi_words(t,w):
    tab = []
    it = 0
    a = 0
    for st in t :
        while st.find(w) != -1:
            if len(st) > st.find(w) + len(w) + 1 :
                if st[st.find(w) + len(w) + 1] == ' ' :
                    if st.find(w) == 0 :
                        tab.append(w)
    return tab
"""
def remove_char(st, c) :
    return "".join([i for i in st if i != c])


def remove_c_comments(st) :
    while st.find('/*') != -1:
        if st.find('/*') != -1 and st.find('*/') != -1 :
            a = st.find('/*')
            print("deb = ",  str(a))
            b = st.find('*/')
            print("fin = ",  str(b))

            if a < b :
                st = st[:a] + st[b+2:]
            else:
                return "Erreur"
    return st




def remove_preprocess(st) :
    while st.find('#') != -1 :
        deb = st.find('#')
        fin = st[deb:].find('\n') +deb
        if fin != -1 :
            st = st[:deb] + st[fin:]
        else :
            st = st[:deb]
    return st

def remove_cpp_comment(st):
    while st.find('//') != -1:
        deb = st.find('//')
        fin = st[deb:].find('\n') + deb
        if fin != -1:
            st = st[:deb] + st[fin:]
        else:
            st = st[:deb]
    return st


keywords = ["auto","break","case","char","const","continue","default",
    "do","double","else","enum","extern","float","for","goto",
    "if","int","long","register","return","short","signed",
    "sizeof","static","struct","switch","typedef","union",
    "unsigned","void","volatile","while"]



content = "".join(open("acl_add_perm.c").readlines())

print(content)
print("===========================")
#print(remove_preprocess(remove_c_comments(content)))
#print(sashimi_char("ffffffffflwefkwejf", 'f'))

#premiers a enlever, sensible au retour a la ligne

content = remove_c_comments(remove_preprocess(content))

#second a enlever

content = remove_cpp_comment(content)
content = remove_char(content, '\t')

#sashimi premiere vague

content = remove_char(content, '\n')
sa

print(content)
