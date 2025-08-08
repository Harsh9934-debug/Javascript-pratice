#Area of the gemotric figures

def circle(r):
    area = 3.14*r*r
    print("The area of the cirsle is ",area)

def rectangle(l,b):
    area = l*b
    print("The area of the rectangle is ",area)

def triangle(b,h):
    area = 0.5*b*h
    print("The area of the triangle is ",area)

radius = int(input("Enter the radius of circle"))
circle(radius)

