x=int(input("enter a number: "))
f=1
if (x==0):
    print('0! is 1')
elif(x==1):
     print('1')
else:
    for i in range(1,x+1):
        f=f*i
        print(f,',',end="")
