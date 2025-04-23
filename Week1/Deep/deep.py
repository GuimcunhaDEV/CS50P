question = input("Answer: ")
lower = question.lower().strip()

if lower == "42":
    print("Yes");
elif lower == "forty-two":
    print("Yes");
elif lower == "forty two":
    print("Yes");
else:
    print("No");

