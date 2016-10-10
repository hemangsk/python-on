#Variables
a = 4
b =5
a = "Hemang"

if a>4:
    print "a is greater"
else:
    print "Inside else"

if a >8:
    print "a is greater"
    print ""
elif a < 8:
    print "a is "

#char arr = new char[10];
arr = []
print len(arr)
print arr.append(9)
print arr.insert(0, 10)
#print del(arr, 0)
print arr.pop()
#print arr.pop(1)


#List, Tuples, Dictionaries

(9, 10 , 10)

#Dictionary

range(10)


#loop for, while



for i in range(3):
    print "HHeaea"
    print i

i = 0
while (i<10):
    print "Hemang"
    i+=1



#Function
def add(a,b):
    sumO = a+b
    mult = 0
    return sumO, mult

firstVar, secondVar =  add(9,8)
print firstVar
print secondVar



class Car:

    def __init__(self):
        self.aa = 0
        self.name = "Maruti"
        self.model = 0

    def add(self):
        self.aa +=1
        return self.aa

    def __str__(self):
        return str(self.aa) + ", " + str(self.name)


a = "7"
a = int(a)
b = 67
b = str(b)
print a, b
c = Car()
print c.add()
print c
