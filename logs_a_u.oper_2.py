slovo = input ("Введите слово - ")
a = slovo.count ('a')
e = slovo.count ('e')
i = slovo.count ('i')
o = slovo.count ('o')
u = slovo.count ('u')
count =a+e+i+o+u
print ("Всего гласный - ", count)
print ("Всего согласных - ", len(slovo)-count)

if (a == 0):
    print ("Гласной A в слове - False ")
else:
    print ("a=", a)
    
if (e == 0):
    print ("Гласной Е в слове - False")
else:
    print ("e=", e)
    
if (i == 0):
    print ("Гласной I в слове - False ")
else:
    print ("i=", i)
    
if (o == 0):
    print ("Гласной O в слове - False")
else:
    print ("o=", o)
    
if (u == 0):
    print ("Гласной U в слове - False ")
else:
    print ("u=", u)