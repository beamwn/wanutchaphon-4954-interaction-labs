import math

def hypotenuse (num1,num2):
 
 try:
    return (math.sqrt((num1**2) + (num2**2)))
 
 except TypeError:
   return None

print(f'hypotenuse(3,4) is {hypotenuse(3.0, 4.0)}')
print(f"hypotenuse('3','4') is {hypotenuse('3', '4')}")
print(f"hypotenuse(3,'4.0') is {hypotenuse(3, '4.0')}")