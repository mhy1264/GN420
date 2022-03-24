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
    choice =int(input("enter choise"))
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


if __name__ == "__main__":
    # even()
    Sort()