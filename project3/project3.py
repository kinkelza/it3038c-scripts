# import gui items
import tkinter as tk
from tkinter import simpledialog, messagebox

#Create TK root window - Without this error occurs
ROOT = tk.Tk()
ROOT.withdraw()
# loops until a process is performed
while (True):
    # get input
    Type = simpledialog.askstring(title="Type of Math", prompt="Please Enter + for Addition, - for Subtraction, * for Multiplication, / for division, ^ for Square, q to quit")
    # Previous Method
    # Type = input("Please Enter + for Addition, - for Subtraction, * for Multiplication, / for division, ^ for Square, q to quit")

    # Addition - can handle any ammount all functions for Addition, Subtraction, Multiplication and Division work the same
    if Type == "+":
        print("You Chose Addition")
        numbercount = simpledialog.askinteger(title="Amount of Numbers", prompt="How many Numbers are you Using?")
        # Previous Method
        # numbercount = int(input("How many Numbers are you Using?"))
        count = int(0)
        answer = int(0)
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = simpledialog.askfloat(title="Number", prompt="Please enter the number")
            # Previous Method
            # num = float(input("Please enter the number"))
            answer = answer + num
            count = count + 1
        # Answer printing
        prompt = messagebox.showinfo(title="Answer", message=answer)
        # Previous Method
        # print(answer)
        break;

    # Subtraction - can handle any amount
    elif Type == "-":
        print("You Chose Subtraction")
        numbercount = simpledialog.askinteger(title="Amount of Numbers", prompt="How many Numbers are you Using?")
        # Previous Method
        # numbercount = int(input("How many Numbers are you Using?"))
        count = int(0)
        answer = int(0)
        answer = answer + simpledialog.askfloat(title="Number", prompt="Please enter the number")
        # Previous Method
        # answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = simpledialog.askfloat(title="Number", prompt="Please enter the number")
            # num = float(input("Please enter the number"))
            answer = answer - num
            count = count + 1
        # Answer printing
        prompt = messagebox.showinfo(title="Answer", message=answer)
        # Previous Method
        # print(answer)
        break;

    #multiply - can handle any amount
    elif Type == "*":
        print("You Chose Multiplication")
        numbercount = simpledialog.askinteger(title="Amount of Numbers", prompt="How many Numbers are you Using?")
        # Previous Method
        # numbercount = int(input("How many Numbers are you Using?"))
        count = int(0)
        answer = int(0)
        answer = answer + simpledialog.askfloat(title="Number", prompt="Please enter the number")
        # answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = simpledialog.askfloat(title="Number", prompt="Please enter the number")
            # Previous Method
            # num = float(input("Please enter the number"))
            answer = answer * num
            count = count + 1
        # Answer printing
        prompt = messagebox.showinfo(title="Answer", message=answer)
        # Previous Method
        # print(answer)
        break;

    #division - can handle any amount
    elif Type == "/":
        numbercount = simpledialog.askinteger(title="Amount of Numbers", prompt="How many Numbers are you Using?")
        # Previous Method
        #numbercount = int(input("How many Numbers are you Using?"))
        count = int(0)
        answer = int(0)
        answer = answer + simpledialog.askfloat(title="Number", prompt="Please enter the number")
        # Previous Method
        # answer = answer + float(input("Please enter the number"))
        # set outside loop due to first input
        numbercount = numbercount - 1
        # determines number of loops until requested number is reached
        while numbercount > count:
            num = simpledialog.askfloat(title="Number", prompt="Please enter the number")
            # Previous Method
            # num = float(input("Please enter the number"))
            answer = answer / num
            count = count + 1
        # Answer printing
        prompt = messagebox.showinfo(title="Answer", message=answer)
        # Previous Method
        # print(answer)
        break;

    # square - only handles 1 input
    elif Type == "^":
        print("You Chose Square")
        num1 = simpledialog.askfloat(title="Square", prompt="Please enter the number you wish to square")
        # Previous Method
        # num1 = float(input("Please enter your Number you wish to square"))
        answer = float(num1 * num1)
        # Answer printing
        prompt = messagebox.showinfo(title="Answer", message=answer)
        # Previous Method
        # print(answer)
        break;
        
    # quit method - get out of program
    elif Type == "q":
        # print quit note
        prompt = messagebox.showwarning(title="Quit", message="You Quit")
        # Previous Method
        # print("You Quit")
        break;

    # Other - if the wrong input is received
    else:
        # print error message in dialog box
        prompt = messagebox.showerror(title="Error", message="This is not a valid operator")
        # previous method
        # print("This is not a valid operator")


print("Thanks for using this calculator")
