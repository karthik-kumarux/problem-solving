d={}
x=int(input("enter for x: "))
for i in range(1,x+1):
    d.update({i:i*i})
print(d)
