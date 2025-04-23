def main():
    mass = int(input("Type a value for mass: "))
    energy = calc(mass)
    print(f"The energy in Joules is equal to {energy}")

def calc(m):
    c = 300000000
    return m * c**2

main()
