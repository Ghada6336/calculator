
def main():
    first = input("Enter the first number:")
    second = input("Enter the second number:")
    operation = (input("Choose the operation (+, -, /, *):"))
    
    if (str(first).isdigit()) and (str(second).isdigit()):
        
        if operation== "*":
            
            print ("the answer =",int(first)*int(second))
        elif operation== "-" :
            print ("the answer =" ,int(first)-int(second))
        elif operation == "+" :
            print ("the answer =" ,int(first)+int(second))
        elif operation == "/" :
            print ("the answer =", int(first)/int(second))
        else:
            print ("invalid opration")
    else:
            print ("not a number")
    pass
if __name__ == '__main__':
     main()
