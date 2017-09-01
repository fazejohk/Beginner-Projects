import random
import time
def game():
    randomtf=random.randint(1,2)
    tf={1:"TRUE!!!", 2:"FALSE!!!"}

    print (tf[randomtf])
    game1()

def game1():
    data=input("[ENTER]")
    game()

game1()
