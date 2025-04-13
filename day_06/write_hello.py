file_name = "write_hello.txt"
greeting = "Greetings\n"
lines = ['hello world\n', 'i like spam\n', 'Bacon.']

with open(file_name, 'w') as f:
    f.write(greeting)
    #f.writelines(lines)
    #for line in lines:
        #f.write(line+"\n")

f.close()

with open(file_name, 'a') as g:
    g.writelines(lines)