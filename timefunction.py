import time 
import calendar
def basicTime1():
    print(time.time())
    print(time.ctime())

def localtime ():
    local=time.localtime()
    # print(type(local))
    for i in local:
        print(i)

def formatTime():
    #          STRing Format TIME
    print(time.strftime("%Y-%m-%d %H:%M:%S ==> %A",time.localtime()))

def calender ():
    
    print(calendar.month(2022,12,w=3,l=1)) 
    print(calendar.month(2022,12,w=4,l=2))
    print(calendar.calendar(2022,w=4,l=2,c=6))
    print(calendar.isleap(2022))
    print(calendar.monthcalendar(2022,5))

    for i in calendar.monthcalendar(2022,5):
        print(i)
        for j in i:
            print(j)


def practice():
    date=input().split('.')
    days= ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    for i in calendar.monthcalendar(int(date[0]),int(date[1])):
        for j in i:
            if(j==int(date[2])):
                print(days[i.index(j)])
                break

if __name__=='__main__':
    practice()
    # calender ()
    # formatTime()
    # basicTime1()
    # localtime()

