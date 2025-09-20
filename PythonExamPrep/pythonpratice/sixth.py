#Tuple operation

tpl = ('1','2','3','4','5','6','7','8')

tpl = tpl+('9',)
print(tpl)

s = ''.join(tpl)
print(s)

for i in tpl:
    print(i)

lst = list (tpl)
print(lst)

tpl = tpl[:3]+tpl[7:]
print(tpl)

tpl = tpl[:3]
print(tpl)