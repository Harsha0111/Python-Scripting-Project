name = input("Enter your name: ")

file = open("name.txt" ,"a") #open a name.txt file to store i/p, and "a" is append(to add the content below with existing)
file.write(f"{name} \n")  #\n is to print the new line b/w i/p
file.close()  #close is to save the file

#or file read
#with open("name.txt","r") as file:
 #   lines = file.readlines()

    #here using with we need not to close the file it automatically closes 

#for line in lines:  #print one by one
 #   print("hello", line.rstrip())  
          #rstrip is right side remove white spaces
#or
with open("name.txt","r") as file:
    for line in file:
        print("hello",line,end="") #instead end="" use .rstrip()