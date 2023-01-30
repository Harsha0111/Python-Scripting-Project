file = open("CRUD_File_input.txt") .close()


def menu():
    print("Menu:")
    print("1.View")
    print("2.Insert")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")
    option = 1
    try:
        option = int(input("Enter num: "))
    except ValueError:
        print("Enter a valid number!!!")
        menu()

    if option == 1:
        with open('CRUD_File_input.txt') as file:
            contents = file.read()
            print(contents)
        menu()

    elif option == 2:
        try:
            text = input("What Do You Want To Write To Your File:")
            saveFile = open('CRUD_File_input.txt', 'a')
            saveFile.write(text)
            saveFile.write("\n")
            saveFile.close()
        except ValueError:
            print("Enter a valid number!!!")
            menu()
        print("Inserted Successfully")
        menu()

    elif option == 3:
        try:
            with open('CRUD_File_input.txt') as file:
                contents = file.read()
            text = input("Enter the word to be replace: ")
            textUpdate = input("Enter the word to be update: ")
            contents = contents.replace(text,textUpdate)
            with open('CRUD_File_input.txt', 'w') as file:
                file.writelines(contents)
        except ValueError:
            print("Enter a valid number!!!")
            menu()
            
        print("Updated Successfully")
        menu()

    elif option == 4:
        deleteLine = input("Enter the word to be deleted = ")
        with open('CRUD_File_input.txt', 'r') as file:
            contents = file.readlines()
        with open('CRUD_File_input.txt', 'w') as file:  
            for textLine in contents:
                if textLine.strip("\n") != deleteLine:
                    file.write(textLine)
        print("Deleted Successfully")
        menu()

    elif option == 5:
        print("Thank you")
    else:
        print("Invalid Option")
        menu()
menu()
