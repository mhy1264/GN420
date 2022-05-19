import os
import atm
def read():
    myFile=open('read_File\\text.txt','r')
    # print("File name",myFile.name)
    # print("File mode",myFile.mode)
    str=myFile.read()
    print(str)
    myFile.close()

def write ():
    myFile=open('read_File\\text.txt','a')
    myFile.write("test\n")
    myFile.close()
    print("read in Write")
    read()
    
def practice():
    os.chdir("read_File")
    print("check workDir ",os.getcwd())

    try:
        os.mkdir("pythonTest")
    except:
        pass

    os.chdir("pythonTest")

    f=open("myText",'a')
    f.write("I Love Py\n")

    f.close()

    os.rename("myText","myText2")
    file = open("myText2",'a')
    file.write("I love C++ more")
    file.close()

    os.remove("myText2")
    os.chdir("..")
    print("check workDir ",os.getcwd())

    try:
        os.rmdir("pythonTest")
    except:
        print("cann't remove pythonTest")


def practice2():
    os.chdir("read_File")
    op=0
    FileName=""
    while 1==1:
        print("(1) Open new File ")
        print("(2) read file and add")
        print("(3) read and overWrite")
        print("(4) quit")

        op = int(input())

        if(op==1):
            FileName = input()
            FileName += ".txt"
            f = open(FileName,'a')
            content = input("content")
            f.write(content)
            f.close()

        if(op==2):
            f=open(FileName,'a')
            content = input("content: ")
            f.write(content)
            f.close()

        if(op==3):
            f=open(FileName,'w')
            content = input("content: ")
            f.write(content) 
            f.close()

        if(op==4):
            break

def practice3():
    print(os.getcwd())
    os.chdir("read_File")

    f=open("db.txt",'r')  
    buffer= f.readlines()
    f.close()
    temp =list()
    for i in range(0,len(buffer)):
        temp.append(buffer[i][0:-1].split(','))

    op=0
    while(op!= 5):
        op = int(input())
        if(op==1):
            info=input().split(' ') # user 端輸入帳號米馬
            id = 0
            status = False
            for i in range(0,len(temp)):
                if (temp[i][0]==info[0] and temp[i][1]==info[1]):
                    status = True
                    id = i

            if(status):
                des = int(input())
                temp[id][2]=int(temp[id][2])+des
            else:
                print("Wring Accounts or Password")

        if(op==2):
            info=input().split(' ') # user 端輸入帳號米馬
            id = 0
            status = False
            for i in range(0,len(temp)):
                if (temp[i][0]==info[0] and temp[i][1]==info[1]):
                    status = True
                    id = i

            if(status):
                withdraw = int(input())
                temp[id][2]=int(temp[id][2])-withdraw
            else:
                print("Wring Accounts or Password")
        
        if(op==3):
            info=input().split(' ') # user 端輸入帳號米馬
            id = 0
            status = False
            for i in range(0,len(temp)):
                if (temp[i][0]==info[0] and temp[i][1]==info[1]):
                    status = True
                    id = i

            if(status):
                print("Remaining Bills ",temp[id][2])
            else:
                print("Wring Accounts or Password")
        
        if(op==4):
            info=input().split(' ') # user 端輸入帳號米馬
            info.append(0)

            temp.append(info)
    
        f=open("db.txt",'w')
        for i in range(0,len(temp)):
            print("{},{},{}".format(temp[i][0],temp[i][1],temp[i][2]),file=f)
        f.close()

if __name__=='__main__':
    # print("read in main")
    # read()
    # write()
    # practice()
    # practice2()
    practice3()

