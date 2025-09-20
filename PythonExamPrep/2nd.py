# To demnstrate the Arithematic operation in python

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Select the operator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice from the following")
    if choice in ('1','2','3','4'):
        try:
            num1 = int(input("Enter the first number"))
            num2 = int(input("Enter the second number "))
        except ValueError:
            print("Invalid input ! Enter an valid number ")
            continue
    if choice == '1':
        print(num1 ,"+",num2 ," = ", add(num1,num2))
    elif choice == '2':
        print(num1 ,"-",num2 ," = ", subtract(num1,num2))
    elif choice == '3':
        print(num1 ,"*",num2 ," = ", multiply(num1,num2))
    elif choice == '4':
        print(num1 ,"/",num2 ," = ", divide(num1,num2))
    next_validate = input("Do you want to continue :")
    if next_validate == 'no':
        break
    else:
        ("Invalid input")