import re


def myFun():
    print("this is my first function")
    
def two(a,b):
    sum=a+b
    print(sum)

def three(a,b,c):
    sum=a+b+c
    print("print in three()",sum)
    return sum


def squareSumRoot(x,y):
    sqrtSum=x*x+y*y;
    return sqrtSum**0.5

def sort(x,y,z):
    temp=[x,y,z]
    temp.sort()
    return temp

def practice (x):
    print(x)
    if(len(x)>3):
        return [x[0],x[1]]
    else:
        return len(x)

def fib(x:int):
    fibList=list()
    fibList.append(0)
    fibList.append(1)

    for i in range (1,x+1):
        fibList.append (fibList[-1]+fibList[-2])
    print(fibList)
temp = 10
def var():
    temp = 20
    print("temp in function",temp)


def practiceWhile ():
    ls=[121,'abc',45,'def',45,'ghi',60,3.14]
    newList1 =list()
    i=0
    while (i<len(ls)):
        newList1.append(ls[i])
        i+=1
    print("Q1",newList1)
    
    newList2=list()
    while (len(newList1)):
        newList2.append(newList1.pop(-1))
    print(newList2)

    newList3=list()

    i=0
    while (i<len(ls)):
        if(i%2==0):
            newList3.append(ls[i])
        i+=1
    print(newList3)

    newList4=list()
    while(len(newList3)):
        newList4.append(newList3.pop(-1))
    print(newList4)


def while2():
    n=20
    nums=list();
    i=0
    while(i<21):
        nums.append(i)
        i+=1

    print(nums)

def Prime():
    num=[];
    i=2
    for i in range(2,100):
        j=2
        for j in range(2,i):
            if(i%j==0):
                break
            else:
                if( i in num):
                    pass
                else:
                    num.append(i)
    print(num)

def bmi(h,w):
    index = w/((h/100)**2)
    print(index)
    if (index <18.5):
        return "過輕"
    elif (index>=18.5 and index<24):
        return "剛好"
    else:
        return "過重"


if __name__=='__main__':
    #myFun()
    #two(1,2)
    #ans = three(1,2,3)
    #print("print in main() ",ans)
    #ans = squareSumRoot(1,1)
    # print(ans)

    #a=sort(1,2,3)
    #print(a)

    #print( practice([1,2,3,4,5,6,7,8,9,10]))
    #print( practice([1,2]))

    # for i in range(10):
    #     fib(i)
    #var()
    #print (temp)
    #practiceWhile()
    #while2()
    #Prime()
    print( bmi(170,64))

