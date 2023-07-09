import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    while True:
        try:
            circle = Circle(int(input('Enter a radius:')))
            print(f'The circle with radius {circle.radius:.1f} has the area as {circle.area():.2f} and the circumference as {2*math.pi*circle.radius:.2f}')
            break
        except ValueError:
            print('Please enter a valid decimal number')
