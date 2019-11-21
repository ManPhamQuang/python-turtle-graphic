# Pham Quang Man
# s3804811
import turtle
length = 100

def drawPolygonOfGivenSides(sides, tito):
    num_of_triangle = sides - 2
    sum_of_interior_angles = num_of_triangle * 180
    angle = sum_of_interior_angles / sides
    tito.begin_fill()
    for i in range(sides):
        tito.color("black", "#ADD8E6")
        tito.forward(length/2)
        tito.stamp()
        tito.forward(length / 2)
        tito.left(180 - angle)
    tito.end_fill()

def drawPolygons():
    tito = turtle.Turtle()
    win = turtle.Screen()
    tito.speed(0)
    tito.pencolor("white")
    tito.setpos(-400, -100)
    win.bgcolor("white")
    tito.pensize(1)
    tito.fillcolor("#ADD8E6")
    for i in range(10, 2, -1):
        drawPolygonOfGivenSides(i, tito)
        tito.forward(length)
    win.exitonclick()

def drawCircle(tito, length):
    tito.begin_fill()
    tito.circle(length)
    tito.left(10)
    tito.end_fill()

def drawFlower():
    tito = turtle.Turtle()
    tito.speed(10000)
    tito.pencolor("black")
    win = turtle.Screen()
    win.colormode(255)
    win.bgcolor("white")
    tito.pensize(1)
    tito.setpos(length*1.25,-length*1.25)
    for i in range(0,4):
        for i in range(0, 36, 1):
            tito.fillcolor(80, i * 7, 160)
            tito.pencolor(i * 7, 160, 80)
            drawCircle(tito, 100)
        tito.left(90)
        tito.forward(length*2.5)

    win.exitonclick()

def main():
    option = int(input("Enter an option (1/2/3):"))
    if option == 1:
        drawPolygons()
    elif option == 2:
        drawFlower()
    elif option == 3:
        print("exiting")

main()


