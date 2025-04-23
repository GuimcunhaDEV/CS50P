greeting = str(input("Greet the banker: ")).lower().strip()
lower = greeting.split()[0]
first = greeting[0]


if lower == "hello":
    print("$0");
elif lower == "hello,":
    print("$0");
elif first.startswith("h"):
    print("$20");
else:
    print("$100")
