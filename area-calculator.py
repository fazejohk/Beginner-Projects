import time
import turtle
print("example lenght=100 left=90")
print("Ctrl + C to Exit")
colori=str(input("Select your color first letter must start whit a capital letter: "))
def turtledraw(lenght, hight):
    try:
        for i in range(1000):
            my_turtle.color(colori)
            my_turtle.forward(lenght)
            my_turtle.left(hight)
    except KeyboardInterrupt:
        print("Exiting")



data=input("Leght: ")
data1=input("hight: ")
my_turtle = turtle.Turtle()
my_turtle.speed(5)
turtledraw(int(data),int(data1))
