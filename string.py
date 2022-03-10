def add(): 
    a="123"
    b="456"
    a+=b
    print(a)

def exchange():
    a="123"
    b="456"
    a,b=b,a
    print(a)
    print(b)

def copyStr():
    a="123"
    a*=3
    print(a)

def getChar():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha+=alpha.upper()
    print(alpha)
    print(alpha[1])
    print(alpha[0:10:1])

def getLenght():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha+=alpha.upper()   
    Length=len(alpha)
    print(Length)

def getSplit():
    alpha = "abcde fghij klmno pqrst uvwxy z"
    newString =alpha.split(' ');
    print (type (newString))
    print(newString)

def testJoin():
    alpha = "abcde fghij klmno pqrst uvwxy z"
    newString =alpha.split(' ');
    new='-'.join(newString)
    print(new)

def testReplacement():
    alpha = "abcde fghij klmno pqrst uvwxy z"
    alpha=alpha.replace(' ','')
    print(alpha)

def toLowerCase():
    alpha = "abcde fghij klmno pqrst uvwxy z"
    alpha=alpha.toLower()
    print(alpha)

def review():
    birth=input("birth")
    birth=birth.replace('-','/')
    nid=input("nid")
    nid.upper()
    sid=input("sid")
    sid=sid[1:-1]
    name=input("name")
    name.upper()
    nameLen=len(name)

    print(birth)
    print(nid)
    print(sid)
    print(name)
    print(nameLen)

def review2():
    str="&&&&&123&&45&&&&67&788"
    print(len(str))
    listStr=str.split("&")
    print(listStr)
    newStr='-'.join(listStr)
    print(newStr)
    newStr=newStr.replace('-','@')
    print(newStr)

if __name__ == '__main__':
    # add()
    # exchange()
    # copyStr()
    # getChar()
    # getLenght()
    # getSplit()
    # testJoin()
    # testReplacement()
    # ToLowerCase()
    # review()
    # review2()