import random
import time
import turtle
def turtledraw(lenght, hight):
    my_turtle = turtle.Turtle()
    my_turtle.speed(5)
    for i in range(1000):
        my_turtle.forward(lenght)
        my_turtle.left(hight)

print("example lenght=100 left=90")

data=input("Leght: ")
data1=input("hight: ")
turtledraw(int(data),int(data1))
