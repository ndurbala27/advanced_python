file_name = 'goodbye.txt'
search_trm = input("What are you looking for? ")
found = False

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found")
else:
    if contents:
        if search_trm in contents:
            print("Found it")
        else:
            print("not found")