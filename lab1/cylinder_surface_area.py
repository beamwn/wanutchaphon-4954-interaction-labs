import math

radius = float(input('Enter radius: '))
if (radius >= 0):
    
    height = float(input('Enter height: '))
    if (height >= 0):
        area = 2*math.pi*(radius**2) + 2*math.pi*radius*height
        print(f'The surface area of a cylinder with radius\n{radius} and height {height} is {area}')
    else:
         print('Please enter a positive number for height')

else:
    print('Please enter a positive number for radius')


