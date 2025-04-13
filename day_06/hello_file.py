file_name = 'hello.txt'

try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found")
else:
    if contents:
        print(contents)