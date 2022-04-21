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
if __name__=='__main__':
    #myFun()
    #two(1,2)
    #ans = three(1,2,3)
    #print("print in main() ",ans)
    #ans = squareSumRoot(1,1)
    # print(ans)

    #a=sort(1,2,3)
    #print(a)

    print( practice([1,2,3,4,5,6,7,8,9,10]))
    print( practice([1,2]))
