correct_input = False

while not correct_input:
 try:
  celsius = float(input('Enter a temperature in Celsius: '))
  farenheit = ( 9 / 5 )*celsius + 32
  print(f'{celsius:.2f} in Celsius is {farenheit:.2f} Farenheit')
 except ValueError:
  print('Please enter a valid floating point for the temperature.')
 else:
  correct_input = True
 


