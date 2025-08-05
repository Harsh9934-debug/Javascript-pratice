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
    s(0,y) or
    s(x,0) or 
    s(4,y)or
    s(x,3)or 
    s(x+min(y,4-x),y-min(y,4-x)) or
    s(x-min(x,3-y),y+min(x,3-y))
    )
s(0,0)