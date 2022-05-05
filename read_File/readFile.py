from inspect import modulesbyfile
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







if __name__=='__main__':
    # print("read in main")
    # read()
    # write()
    practice()

