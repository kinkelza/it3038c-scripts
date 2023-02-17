# loops until a process is performed
while (True):
    # get input
    Type = input("Please Enter + for Addition and - for Subtraction")
    # Addition
    if Type == "+":
        print ("You Chose Addition")
        num1 = float(input("Please enter the first number"))
        num2 = float(input("Please enter the Second number"))
        answer = float(num1 + num2)
        print (answer)
        break;
    # Subtraction
    elif Type == "-":
        print("You Chose Subtraction")
        num1 = float(input("Please enter the first number"))
        num2 = float(input("Please enter the Second number"))
        answer = float(num1 - num2)
        print(answer)
        break;
    # Other
    else:
        print("This is not a valid operator")

print("Thanks for using this calculator")
