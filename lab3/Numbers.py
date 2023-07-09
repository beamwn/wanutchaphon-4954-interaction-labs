class Numbers:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    @classmethod
    def display_factors(cls, n):
        if n%2 == 0:
            n1 = n2 = n//2
        else:
            n1 = n//2
            n2 = n1+1
        return (f'Factors of {n} is {n1} and {n2}')
    
    @staticmethod
    def is_valid_divisor(x):
        if x != 0:
            return (f'{x} is a valid divisor')
        else:
            x == 0
            return (f'{x} is not a valid divisor')

if __name__ == '__main__':
    print(f'2 + 3 is {Numbers(2, 3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.is_valid_divisor(2))
    print(Numbers.is_valid_divisor(0))
            


    
