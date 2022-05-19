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


if __name__=="__main__":
    practice2()
    # practice1()
    # person()
