name = input("Enter name: ")
print(name)
match name:
    case "Hello" :
        print("Hii")

    case "Herry" :
        print("Hiiiiii")
    case _:
        print("Invalid")
