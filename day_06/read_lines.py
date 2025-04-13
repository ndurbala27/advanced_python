file_name = "goodbye.txt"
search_trm = "i am fine."
found = False

with open(file_name) as f:
    for line in f:
        print(line.rstrip())

f.close()

with open(file_name) as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)

for line in lines:
    if line.rstrip() == search_trm:
        found = True

if found:
    print("Found it")
else:
    print("404")
