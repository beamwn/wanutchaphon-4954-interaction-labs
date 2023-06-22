import math

print('radius\theight\tsurface_area')

for i in range (1,11):
     area = 2*math.pi*(i**2) + 2*math.pi*i*i*2
     print(f'{i:6} {i*2:7} {area:13.2f}')




