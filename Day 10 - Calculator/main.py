num1 = int(input("What's the first number?: "))
num2 = int(input("What's the next number?: "))
operation = input("choose an operation from the following - '+','-','*','/':  ")

def add(num1,num2):
    if operation == "+":
        print(num1 + num2)

def sub(num1,num2):
    if operation == "-":
        print(num1 - num2)

def multiply(num1,num2):
    if operation == "*":
        print(num1 * num2)

def divide(num1,num2):
    if operation == "/":
        print(num1 / num2)
    
add(num1=num1,num2=num2)
sub(num1=num1,num2=num2)
multiply(num1=num1,num2=num2)
divide(num1=num1,num2=num2)

