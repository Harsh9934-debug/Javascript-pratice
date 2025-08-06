v={}
def s(x,y):
 if(x==2 and y==0)or(x==0 and y==2):
    print((x,y))
    return 1
 if(x,y)in v:
    return 0
 v[(x,y)]=1
 print((x,y))
 return (
    s(x,0) or 
    s(0,y) or
    s(x,3) or 
    s(4,y) or
    s(x+min(y,4-x),y-min(y,4-x)) or
    s(y+min(x,3-y),x-min(x,3-y))
    )
s(0,0)