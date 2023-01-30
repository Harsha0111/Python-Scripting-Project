name = []

with open("name.txt") as file:
    for line in file:
        name.append(line.rstrip())  #append is to add new line to existing one
            #leave an empty line to close done automatic by "with" method
for nam in sorted(name):
    print("hello", name)
