import math

def compute_hypotenuse (num1,num2):
 compute = math.sqrt((num1**2) + (num2**2))
 print(f'Sqrt({num1}^2 + {num2}^2) = {compute}')

compute_hypotenuse(3.0, 4.0)
compute_hypotenuse(3, 4)
compute_hypotenuse(3, 4.0)