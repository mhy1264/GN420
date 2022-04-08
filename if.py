def even():
    n=int(input("enter a number"))
    if (n%2):
        print("odd")
    else:
        print("even")

def Sort():
    print("enter 3 number")
    n=input()
    List = n.split(' ')
    print(List)
    print("1) SORT \n","2) SORTED \n")
    choice =int(input("enter choice"))
    if choice==1:
        List.sort()
        print(List)
    elif choice==2:
        newList =List.sorted()
        print("newList ",newList,"\n")
        print("oldList ",List,"\n")
    else:
        print("Your program should not execute here")
        exit(-1)

def doCompare():
    first = int (input("enter first number"))
    second = int (input("enter second number"))

    if (first>second):
        print(first,">",second)
    elif (first<second):
        print(first,"<",second)
    elif (first == second):
        print(first,"=",second)
    else:
        print("Your program should not execute here")

def password():
    db={"uber":"eat"}
    while(True):
        print("1) Add user ")
        print("2) change user ")
        print("3) delete password ")
        
        ch= int (input("enter choice "))
        

        if(ch==1):
            if(usr in db):
                print("user is already in database")
            else:
                Adduser= input("enter new user")
                Addpass= input("enter new password")
                temp=dict({Adduser:Addpass})
                db.update(temp)
                print(db)
        elif (ch==2):
            usr= input("enter userName ")
            if(usr in db):
                newpd = input("enter new password")
                temp=dict({usr:newpd})
                db.update(temp)
            else:
                print("user is not found ")
        elif(ch==3):
            usr= input("enter userName ")
            if(usr in db):
                del db[usr]
            else:
                print("user is not found ")  
        else:
            break;

if __name__ == "__main__":
    # even()
    # Sort()
    # doCompare()
    password()
