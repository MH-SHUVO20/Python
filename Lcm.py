import math
print("Calculating LCM of Two Numbers \n")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
Lcm=(a*b)/math.lcm(a,b)
print("The LCM of",a,"and",b,"is",Lcm)