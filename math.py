import math
def circleArea():
    r=float(input("r"))
    circleArea = math.pow(r,2)*math.pi
    print(circleArea)

def birthSquare():
    sum=2002+11+1
    print(math.sqrt(sum))

def km2mile():
    km=int(input("km "))
    mile= km*0.62
    print(mile)

def degree():
    c=int(input("degree "))
    #25°C×9/5+32
    c*=9
    c/=5
    c+=32
    print(int(c))

def log10():
    n=int(input("log10 "))
    print(math.log10(n))

def power():
    x=int(input("base "))
    y=int(input("power "))
    print(math.pow(x,y))

    
if __name__ == '__main__':
    #circleArea()
    #birthSquare()
    #km2mile()
    #degree()
    #log10()
    #power()