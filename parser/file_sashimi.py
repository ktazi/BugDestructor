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

#content = "".join(open("acl_add_perm.c").readlines())

#print(content)
#print("===========================")
#print(remove_preprocess(remove_c_comments(content)))

#print(sashimi_char("ffffffffflwefkwejf", 'f'))
print(remove_char("ffffffffflwefkwejf", 'f'))
