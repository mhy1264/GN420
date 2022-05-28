import matplotlib.pyplot as plt
import numpy as np

def cos():
    x=np.arange(-360,360)
    y=np.cos(x*np.pi/180)
    plt.plot(x,y)
    plt.title("cosine")
    plt.xlim(-400,400)
    plt.ylim(-15,15)
    plt.show()

def sine():
    x=np.arange(-360,360)
    y=np.sin(x*np.pi/180)
    plt.plot(x,y)
    plt.title("sine")
    plt.xlim(-400,400)
    plt.ylim(-15,15)
    plt.show()

def line():
    x=np.arange(-400,400)
    y=10*x+20 
    plt.plot(x,y)
    plt.plot(0)
    # plt.title("sine")
    plt.xlim(-40,40)
    plt.ylim(-40,40)
    plt.show()

def merge():
    x=np.arange(-360,360)
    plt.subplot(311)
    plt.plot(x,np.cos(x*np.pi/180))
    plt.subplot(312)
    plt.plot(x,np.sin(x*np.pi/180))
    plt.subplot(313)
    x=np.arange(-360,360)

    plt.plot(x,np.sin(x*np.pi/180)/np.cos(x*np.pi/180))
    plt.show()


def histogram()  :
    plt.figure()
    #        範圍                 製作數字    條樹   飽和度
    plt.hist(np.random.randn(),range=(0,1),bins=5,alpha=0.1)
    plt.show()
    
if __name__ =="__main__":
    histogram()    
    # merge()
    # line()
    # cos()
    # sine()