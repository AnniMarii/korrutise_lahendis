print("Tere, programm genereerib sulle kaks suvalist arvu, sinu ülesandeks on leida nende korrutis")
from random import randint
print("A on")
a = randint(0, 10)
print(a)
from random import randint
print("B on")
b = randint(0, 10)
print(b)

print("Sisesta vastus")
x = int(input())

c = a * b
if x == c:
    print("Vastasid õigesti")
    
else:
    print("Vale vastus, õige vastus on")
print(c)



    


