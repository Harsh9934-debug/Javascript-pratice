#Area of the gemotric figures

def circle(r):
    area = 3.14*r*r
    print("The area of the circle is ",area)

def rectangle(l,b):
    area = l*b
    print("The area of the rectangle is ",area)

def triangle(b,h):
    area = 0.5*b*h
    print("The area of the triangle is ",area)

radius = int(input("Enter the radius of circle"))
circle(radius)

length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
rectangle(length,breadth)

base = int(input("Enter the base of the triangle"))
height = int(input("Enter the height of the triangle "))
triangle(base,height)