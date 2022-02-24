x=int(input("input a number"))
ans=0
upBound,downBound=x,0
digit=0

while digit!=5:
    for i in range(downBound,upBound):
        if i*i > x and (i+1)*(i+1) < x:
            ans/=10
            ans*=i;
