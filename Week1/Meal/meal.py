def main():
    time = input("What time is it? ").strip()
    hour = convert(time)
    if  hour >= 7.00 and hour <= 8.00:
        print("breakfast time");
    elif  hour >= 12.00 and hour <= 13.00:
        print("lunch time");
    elif hour >= 18.00 and hour <= 19.00:
        print("dinner time");
    else:
        return

def convert(time):
    h, m = time.split(":")
    hr = float(h)
    min = float(m) * 1 / 60
    return float(hr+min)

if __name__ == "__main__":
    main()
