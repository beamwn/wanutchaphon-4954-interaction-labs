
def compute_factorial(num):
    while True:
        if num ==1:
           return 1
        else:
           return num * compute_factorial(num-1)

while True:
   try:
      num = int(input('Enter an integer: '))
      if num < 0:
         print('Please enter a non-negative integer')
         break
      else:
         factorial = compute_factorial(num)
         print(f'Factorial({num}) is {factorial}')
   except ValueError:
      print('Please enter valid integer')
      break