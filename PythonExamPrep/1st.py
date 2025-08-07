#DATA TYPES IN PYTHON 
class datatypes:
    a = 0
    if a>0:
        print("The entered data is ",a)
        print("The value entered is an positive interger")
    elif a<0:
        print("The entered data is ",a)
        print("The value entered is an negative interger ")
    elif a==0:
        print("The entered data is: ",a)
        print("The value entered is zero and it is an interger")
    print("Data_type of a is ")
    print(type(a))
    print("****************************************************")

    b=0b01
    print("The value of b is ",b)
    print("The data type of the b is ")
    print(type(b))
    print("****************************************************")

    c=-1.2
    if c<0:
        print("The value enter of C is ",c)
        print("The value entered is an negative value")
        print("The data type of C is")
        print(type(c))
    else:
        print("The data entered in c is ",c)
        print("The value enterd is an positive interger")
        print(type(c))
    print("************************************************************")

    d = 1.2+5
    print("The value entered in the D is ",d)
    print(type(d))
    print("********************************************************")

    e = False
    print("The data entered in the E is ",e)
    print("The data type of the E is ")
    print(type(e))
    print("**********************************************************")

    f = "Hello"
    print("The data enterd in the F is ",f)
    print("The data type of F is ")
    print(type(f))