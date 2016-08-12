def add(x, y):
    return x + y
    #Evaluates x + y and returns the INTEGER result back to the point where this function was called from.

def sub(a, b):
    return a - b

def mult(p, r):
    return p * r

def div(a, b):
    return a / b

def remainder(m,n):
    return m % n

print(" ** CALCULATOR ** ")
print("Enter two numbers")
a = input()
b = input()

#Suppose user enters 3 and 5, Then a = "3", b = "5", "3" and "5" are strings
#But we need a = 3, and not "3" and b = 5, and not "5", so that they become integers and then we can perform arithmetic operations.

a = int(a) # This line converts whatever is stored in a to INTEGER Type and assigns that value to a.
b = int(b) # This line converts whatever is stored in b to INTEGER Type and assigns that value to b again.

#SO simply put, int function converts variables to INTEGER data type
# And similiarly, there is an str() function which converts variables to STRING data type

print("\n\nResults!")

# Suppose I entered a=1, b=2 then this happens,

print(add(a,b))     #Addition, add(a,b) becomes --> 3, 3 gets printed on screen.
print(sub(a,b))     #Subtraction, sub(a,b) --> -1
print(div(a,b))     #Division, div(a,b) --> 0
print(mult(a,b))    #Multiplication, mult(a,b) -> 2
print(remainder(a,b))   #Remainder, remainder(a,b) -> 1
