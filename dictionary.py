def default():
    price={"apple":30, "orange":20}
    applePrice1 = price.get("apple")
    print(applePrice1)
    price2=price['apple']
    print(price2)

def update():
    fruit={"apple":30, "orange":20}
    fruit.update({"apple":50})
    print(fruit.get("apple"))

    # add item using update 
    fruit2={"lemon":70}
    fruit.update(fruit2);
    print(fruit)

def copy():
    fruit={"apple":30, "orange":20}
    newFruit = fruit
    print(newFruit)

def deleted():
    fruit={"apple":30, "orange":20}
    try:
        fruit.__delitem__("apple")
    except:
        print("not ")

def practiceDict():
    score={"s110000":100,"s1100001":90}
    print(score.get("s110000"))

    score.update({"s110000":90,})
    print(score.get("s110000"))
    
    temp ={"s1100002":20,"s1100003":345}
    score.update(temp)
    print(score)

if __name__ =='__main__':
    # default()
    # update()
    # copy()
    deleted()