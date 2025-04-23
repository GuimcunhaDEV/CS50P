expression = input("Type the expression: ").strip()
split = expression.split()

if len(split) != 3:
    print("Error! Invalid Format. Try again using something like x + y.")
    exit()

try:
    x = float(split[0])
    y = split[1] # operator
    z = float(split[2])
except ValueError:
    print("Error! sure to input valid numbers.")

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if y == 0:
        print("Error! Cannot divide by zero.")
        exit()
    result = x / z
else:
    print("Error! Invalid operator.")
    exit()

print(f"{result:.1f}")
