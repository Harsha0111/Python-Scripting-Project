while True:
    try:
        x = int(input("Enter num: "))

    except ValueError:
        print("x is not integer")
    else:
        break   #until x is num the loop will be infinite and ask X value to enter

    #without break if we give
    #else:
        #print(f"x is {x}") 
                # if we num as i/p also the loop will be running as infinite and ask x value

print(f"x is {x}") #here except number if we give the loop is infinite 
                    #it shows x is not defined sinc x is integer so if we give variable it shows error