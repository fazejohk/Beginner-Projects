import random
import time
import turtle
color={
1:"red", 2:"green", 3:"blue", 4:"pink", 5:"orange", 6:"black"
    }
randcolor=(random.randint(1,6))
def turtledraw(lenght, hight):
    try:
        for i in range(1000):
            my_turtle.color(color[randcolor])
            my_turtle.forward(lenght)
            my_turtle.left(hight)
    except KeyboardInterrupt:
        print("Exiting")

print("example lenght=100 left=90")

data=input("Leght: ")
data1=input("hight: ")
my_turtle = turtle.Turtle()
my_turtle.speed(5)
turtledraw(int(data),int(data1))
