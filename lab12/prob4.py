text = input("Enter text:")
pattern = input("Enter pattern :")

position = text.find(pattern)

if position != -1:
    print(f"Found {pattern} in {text} at {position}")
else:
    print(f"Cannot find {pattern} in {text}")