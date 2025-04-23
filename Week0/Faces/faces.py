def convert(faces):
    faces = faces.replace(":)", "🙂").replace(":(", "🙁")
    return faces

def main():
    feel = input("Type something here:")
    print(convert(feel))

main()
