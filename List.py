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

def testAppend ():
    List1=[1,2,3,4,5]
    List2=[6,7,8,9,10]
    print("appending...\n")
    List1.append(List2)
    print(List1)

def testExtend ():
    List1=[1,2,3,4,5]
    List2=[6,7,8,9,10]
    print("extending...\n")
    List1.extend(List2)
    print(List1)

def testAppendAndExpand():
    testAppend ()
    testExtend ()

def listReview1():
    str='''Knowledge is one thing virtue is another good sense is not conscience refinement is not humility nor is largeness and justness of view faith Philosophy however enlightened however profound gives no command over the passions no influential,motives,no,vivifying,principles Liberal Education makes not the Christian not the Catholic but the gentleman It is well to be a gentleman it is well to have a cultivated intellect a delicate taste a candid equitable dispassionate mind a noble and courteous bearing in the conduct of life these are the connatural qualities of a large knowledge they are the objects of a University. I am advocating I shall illustrate and insist upon them but still I repeat they are no guarantee for sanctity or even for conscientiousness and they may attach to the man of the world to the profligate to the heartless pleasant alas and attractive as he shows when decked out in them.'''
    strList = str.split(' ')
    numStrList = len(strList)

    print(numStrList)

    print(strList[65])


    print("intelligence" in strList)


    print(strList.index("Philosophy"))

    info="My student ID is 1103334"

    print(strList.append(info))

    buffer = "influential,motives,no,vivifying,principles";
    bufferList = buffer.split(",")

    buffstr=""
    for i in bufferList:
        buffstr+=i
        buffstr+=' '

    buffind =strList.index(buffer);

    strList[strList.index(buffer)]=buffstr.split(" ")

    print(strList[buffind][1])

def listReview2():
    artStr='k,n,o,w,l,e,d,g,e,i,s,o,n,e,t,h,i,n,g,v,i,r,t,u,e,i,s,a,n,o,t,h,e,r,g,o,o,d,s,e,n,s,e'
    artList=artStr.split(',')
    print(artList.count("e"))

    name =input("Name ")
    for i in name :
        artList.insert(-1,i)
    print(artList)

    print("removing 1-9\n")
    for i in range(1,10):
        artList.remove(artList[i])
    print(artList)

    print("insert 'z' to 1 \n")
    artList.insert(1,'z')  
    print(artList)

    print("sort \n")
    artList.sort(reverse=True)
    print (artList)


    try:
        artList.remove(artList.index("a"))
    except:
        print("a is not in the list")

def insertList():
    List=[1,2,3,4,5]
    List.insert(1,"A")
    print(List)

def delete ():
    List=[1,2,3,4,5]
    print(List)
    print(List.count(3))
    del List

    try :
        print(List)
    except:
        print("List is not Exists")

def sort():
    List =[5,4,6,2,1]
    List.sort()
    List1=sorted(List ,reverse=True)
    print(List1)
    print(List)
    List.sort(reverse=True)
    print(List)

def practiceSort():
    score =[33,100,99,45,77,35,100,12,100,99,45]

    sort_score=sorted(score,reverse=True)
    print(sort_score)

    score.sort()
    print(score)

    
    score.sort(reverse=True)
    print(score)

    print(sort_score.count(99)) 

    new=[59,34,10,88,90]
    sort_score.extend(new)
    print (sort_score)

    sort_score.sort(reverse=True)
    print(sort_score)

    sort_score[sort_score.index(59)]=60
    print(sort_score)

if __name__ == "__main__":
    # iterator() 
    # nested()
    # usingIndex()
    # usingIn()
    # append()
    # testList ()
    # listReview1 ()
    # listReview2()
    # testAppendAndExpand()
    # insertList()
    # delete ()
    # sort()
    practiceSort()