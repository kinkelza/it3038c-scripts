# loops until a process is performed
while (True):
    # get input
    Type = input("Please Enter + for Addition, - for Subtraction, * for Multiplication, / for division, ^ for Square, q to quit")
    # Addition - can handle any ammount all functions for Addition, Subtraction, Multiplication and Division work the same
    if Type == "+":
        print("You Chose Addition")
        numbercount = int(input("How many Numbers are you Using?"))
        count = int(0)
        answer = int(0)
        #determines number of loops until requested number is reached
        while numbercount > count:
            num = float(input("Please enter the number"))
            answer = answer + num
            count = count + 1
        print (answer)
        break;
    # Subtraction - can handle any amount
    elif Type == "-":
        print("You Chose Subtraction")
        numbercount = int(input("How many Numbers are you Using??"))
        count = int(0)
        answer = int(0)
        answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = float(input("Please enter the number"))
            answer = answer - num
            count = count + 1
        print(answer)
        break;
    #multiply - can handle any amount
    elif Type == "*":
        print("You Chose Multiplication")
        numbercount = int(input("How many Numbers are you Using??"))
        count = int(0)
        answer = int(0)
        answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = float(input("Please enter the number"))
            answer = answer * num
            count = count + 1
        print(answer)
        break;
    #division - can handle any amount
    elif Type == "/":
        numbercount = int(input("How many Numbers are you Using??"))
        count = int(0)
        answer = int(0)
        answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = float(input("Please enter the number"))
            answer = answer / num
            count = count + 1
        print(answer)
        break;
    # square - only handles 1 input
    elif Type == "^":
        print("You Chose Square")
        num1 = float(input("Please enter your Number you wish to square"))
        answer = float(num1 * num1)
        print(answer)
        break;
    elif Type == "q":
        print("You Quit")
        break;
    # Other - if the wrong input is received
    else:
        print("This is not a valid operator")


print("Thanks for using this calculator")
