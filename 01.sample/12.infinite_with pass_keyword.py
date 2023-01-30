def main():
    #num(3)
    x = num("Enter num: ")  
    print(x)
    
def num(prompt):
 while True:
    try:
      return int(input(prompt)) #will fn will be calling the main fnwill define parameter
    
    except ValueError:
        pass  #catching the error and not doing anythong again ask x value to enter

main()