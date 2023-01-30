array = []


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
        print(array)
        menu()
    elif option == 2:
        number = 1
        try:
            number = int(input("Please enter a number to be added: "))
        except ValueError:
            print("Enter a valid number!!!")
            menu()
        array.append(number)  # insert() fn also can use
        print("Inserted Successfully")
        menu()
    elif option == 3:
        update = 1
        num = 2
        try:
            update = int(input("Please enter a number to be delete: "))
        except ValueError:
            print("Enter a valid number!!!")
            menu()
        array.remove(update)
        try:
            num = int(input("Please enter a number to be update: "))
        except ValueError:
            print("Enter a valid number!!!")
            menu()
        array.append(num)
        print("Updated Successfully")
        menu()
    elif option == 4:
        delete = 3
        try:
            delete = int(input("Please enter a number to be delete: "))
        except ValueError:
            print("Enter a valid number!!!")
            menu()
        array.remove(delete)
        print("Deleted Successfully")
        menu()
    elif option == 5:
        print("Thank you")
    else:
        print("Invalid Option")
        menu()


menu()
