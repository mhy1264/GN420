def person():
    class Person():
        def __init__(self,Gender,Name,H,W):
            self.name = Name
            self.gender = Gender
            self.height=H
            self.weight=W
        def Bmi(self):
            return self.weight/(self.height/100)**2
    MHY=Person("male","MHY",100,60)
    print(MHY.Bmi())

def practice1():
    class Student():
        def __init__(self, name ,id , gender):
            self.__name = name 
            self.__id = id 
            self.__gender = gender 
            self.__score =list()

        def add(self,point):
            self.__score.append (point)

        def avg(self):
            sum = 0
            for i in self.__score:
                sum+=i
            return sum/len(self.__score)
        
    me=Student("Me",1,"male")  

    me.add(100)
    me.add(60)
    print(me.avg())    

def practice2():
    class Bank:
        def __init__(self,name,id,Remaining):
            self.name = name 
            self.id = id
            self.money = Remaining

        def showRemaining(self):
            print("Remaining: {}".format(self.money))

        def despoit (self,amount):
            self.money+=amount
            self.showRemaining()

        def withdraw(self,amount):
            if(self.money>=amount):
                self.money-=amount
                self.showRemaining()
            else:
                print("Not enough money")
    
    obj = Bank("Me",1,123)
    obj.withdraw(100)
    obj.withdraw(123)
    obj.despoit(100)

def practice3():
    class gradeSys():
        def __init__(self):
            self.grade=dict()
        
        def update(self):
            stdid = input("student id ")
            score=int(input("score "))
            self.grade.update({stdid:score})

        def getHigh(self):
            high=-1
            for i in self.grade:
                if(high<self.grade[i]):
                    high=self.grade[i]
            print ("max -> {}".format(high))

        def getAvg(self):
            sum=0
            n=0
            for i in self.grade:
                sum+=self.grade[i]
                n+=1
            print ("avg -> {}".format(sum/n))
        
        def getAll(self):
            for i in self.grade:
                print("{} ==> {}".format(i,self.grade[i]))

        def getOne(self):
            stdid = input("student id ")
            try:
                print("{} ==> {}".format(stdid,self.grade[stdid]))
            except:
                print ("找不到")

        def getOutput(self):
            score=open("grade.txt",'w')
            for i in self.grade:
                print("{},{}".format(i,self.grade[i]),file=score)
            print("otpuut finish")
        
        def clear(self):
            self.grade.clear()

    grade = gradeSys()
    while(True):
        op = int (input("input choice "))
        if(op==1):
            grade.update()
        elif(op==2):
            grade.clear()
        elif(op==3):
            grade.getHigh()
        elif(op==4):
            grade.getAvg()
        elif(op==5):
            grade.getAll()
        elif(op==6):
            grade.getOne()
        elif(op==7):
            grade.getOutput()
        else:
            break
        

            


if __name__=="__main__":
    practice3()
    # practice2()
    # practice1()
    # person()
