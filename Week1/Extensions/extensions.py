file = str(input("Type the file's name: ")).strip().lower()
file = '.' + file.split('.')[-1]

match file:
    case ".gif":
        print("image/gif");
    case ".jpg" | ".jpeg":
        print("image/jpeg");
    case ".png":
        print("image/png");
    case ".pdf":
        print("application/pdf");
    case ".txt":
        print("text/plain");
    case ".zip":
        print("application/zip");
    case _:
        print("application/octet-stream");
