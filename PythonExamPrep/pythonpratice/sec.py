def add(x,y):
    return x+y

def multiply(x,y):
    return x*y

def sub(x,y):
    return x-y

def divide(x,y):
    return x/y


print("Select form the following")
print("1.Add   2.Multiply    3.Subtract     4.Divide" )
while True:
    try:
        choice = input("Enter your choice from the following")
        num1 = float(input("Enter the first number"))
        num2  = float(input("Enter the second number"))
    except ValueError:
        print("Invalid input")
        continue
    
    if choice == '1':
        print("The sum of the two number is: ",add(num1,num2))
    elif choice == '2':
        print("The multiplication of the two number is :",multiply(num1,num2))
    elif choice =='3':
        print("The subtract of the two number is:",sub(num1,num2))
    elif choice == '4':
        print("The divide of the teo number is :",divide(num1,num2))

    valu = input("Do you want to continue: ")
    if valu == 'no':
        break
    elif valu =='yes':
        continue
    else:
        print("Invalid input")
    

