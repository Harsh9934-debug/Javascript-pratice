v={}
def s(x,y):
 if(x==2 and y==0)or(x==0 and y==2):
    print((x,y))
    return 1
 if(x,y)in v:
    return 0
 v[(x,y)]=1
 print((x,y))
 return any(s(nx, ny) for nx, ny in [(0,y), (x,0), (4,y), (x,3), (x+min(y,4-x), y-min(y,4-x)), (x-min(x,3-y), y+min(x,3-y))])


s(0,0)