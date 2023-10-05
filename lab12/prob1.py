num1 = int(input("Enter the dividend : "))
num2 = int(input("Enter the divisor : "))

assert num2 != 0, "the divisor cannot be zero"

result = num1 / num2

print(f"{num1} / {num2} = {result}")
