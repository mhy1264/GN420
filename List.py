def iterator():
    str="123456,7890"
    str=str.split(',')
    for i in range(0,len(str)):
        print(str[i])
def nested():
    a=['a',1243,1213.123,['A']]
    a[0]='j'
    print(a)
    print(len(a))

def usingIndex():
    score=[60,59,100,12,30]
    score[score.index(59)]=60
    print(score)

def usingIn():
    score=[60,59,100,12,30]
    print (60 in score)

def end():
    a=[1,2,3]
    b=[4,5,6]
    print(a.extend(b))
    
def testList ():
    List = ['a', 'b', 'c', 'd']
    print ('b' in List)
    List[2]="OK!"
    List.append([2,3,4,5,6])
    print(List)
    temp=int(input("temp "))
    List.append(temp)
    print(List)

if __name__ == "__main__":
    # iterator() 
    # nested()
    # usingIndex()
    # usingIn()
    # append()
    testList ()