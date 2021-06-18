import random


def shake_my_sent(t):
  sem = 0

  if t[-1] == ";":
    t.pop(-1)
    sem = 1

  random.shuffle(tab)

  for i in range(len(t)):
    t[i] = t[i] + " "

  if sem == 1:
    t.append(";")


def print_tab_lines(t):
  for mot in t:
    print(mot)


def make_sent(t):
  return ("".join(t))


tab = ["a", "=", "c", "+", "d", ";"]
tap = ["a", "=", "c", "+", "d"]

shake_my_sent(tab)
pouet = make_sent(tab)

nameSave = "clearLines.txt"
file = open(nameSave, "a")
file.write(pouet)

