def circle(r):
    print("The area of the circle is ")
    print(3.14*r*r)

def rectangle(l,b):
    print("The area of the rectangle is ")
    print(l*b)

def triangle(b,h):
    print("The area of he triangle is ")
    print(0.5*b*h)


radius = int(input("Enter the radius of the circle"))
circle(radius)
length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
rectangle(length,breadth)
base = int(input("Enter the base of the triangle"))
height = int(input("Enter the height of the triangle"))
triangle(base,height)