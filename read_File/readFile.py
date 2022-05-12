import os
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





if __name__=='__main__':
    # print("read in main")
    # read()
    # write()
    # practice()
    practice2()

