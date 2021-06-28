import random
import file_sashimi as sash


def shake_my_sent(t):
  sem = 0

  if t[-1] == ";":
    t.pop(-1)
    sem = 1

  random.shuffle(t)
  print(t)
  for i in range(len(t)):
    t[i] = t[i] + " "

  if sem == 1:
    t.append(";")

def suprem_check(tt):
  for i in range(len(tt)):
    shake_my_sent(tt[i])

def print_tab_lines(t):
  for mot in t:
    print(mot)


def make_sent(t):
  return ("".join(t))


def write_sents(t):
  pouet = ''
  nameSave = "clearLines.txt"
  for i in range(len(t)):
    pouet = make_sent(t[i])
    file = open(nameSave, "a")
    file.write(pouet)
    file.write("\n")


test = sash.sashimi_file('gtk-hotkey-marshal.c')
print(test)

tab = [["a", "=", "c", "+", "d", ";"], ["a", "=", "c", "+", "d"], ["if", "a", "<", "b", "{"]]
#tap = ["a", "=", "c", "+", "d"]
#tac = ["if", "a", "<", "b", "{"]

suprem_check(test)
write_sents(test)
print(tab)




