"""
Compute final amount using formula of compound interest
"""

principal =int( input("Principal Amount ? "))
rate =int (input("Annual nominal interest rate ? "))
compoundCount = int( input("Number of times the interest is compounded per year ? "))
time = int(input("Number of years ?"))

print ("Amount = Rs",  principal * ( (1 + rate/compoundCount)** (compoundCount * time)))
