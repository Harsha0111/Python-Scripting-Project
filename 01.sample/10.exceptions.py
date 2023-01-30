
try: #just try something in python 
    input = int(input("Enter num: "))
    print (f"num is {input}") #f is a format string used for{input} --.ar name is given inside brases

#expected 'except' or 'finally' block for try block
except ValueError:   #to indicate the customized error msg and ValueError is for entering Variable
    print("Please enter integer not variables")  
