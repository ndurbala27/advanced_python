file_name = 'goodbye.txt'
search_trms = ['spam', 'are', 'ham', 'today']

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found")
else:
    if contents:
        for trm in search_trms:
            if trm in contents:
                print("Found it")
            else:
                print("not found")
