camel = input("Insert camelCase to be converted to snake_case: ")
print("snake_case: ", end="")

for i in camel:
    if i.islower():
        print(i, end="")
    if i.isupper():
        print("_", i.lower(), end="", sep="")

print()
