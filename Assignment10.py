0.

u = 17132992
num = str(u)

print("The student number is:",u)


1.
digit = []
for i in num:
    digit = digit + [int(i)]
p = 0
for i in digit:
    
    if i==0:
        continue
    if i==1:
        continue
    if i == 2:
        p = p + 1
        continue
    if i >2:
        for x in range(2,i):
            if i%x ==0:
                break
        else:
            p = p+1
    
print("The number of prime numbers in this student number is:",p)


2.
from random import randint
q = randint(25,50)
print("The random number is:",q)


3.
r = round(q/p)
print("The number of strings to be generated is:",str(r))   

#Question 4
4.
import random
import string
def randomString(r):
    for num in range(1,r+1):
    
        if (num % 2) == 0:
                a= 7
   
        else:
            a = 5
    
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(a))   
print("")
print("list of strings")

#Question 5
5.
stringlist = []
for i in range(1,r+1):
    a = randomString(i)
    stringlist = stringlist + [a]
    print(a)
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
print("")
print("sorted list:")
for i in stringlist:
    vowels = 0
    if a in i :
         vowels = vowels + 1
    if e in i :
         vowels = vowels + 1
    if i in i :
         vowels = vowels + 1
    if o in i :
         vowels = vowels + 1
    if u in i :
         vowels = vowels + 1
    print(i,"(Vowels:",vowels,")")
