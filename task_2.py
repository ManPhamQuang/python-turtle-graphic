import turtle
tito = turtle.Turtle()
win = turtle.Screen()
tito.speed(0)
tito.pencolor("white")
tito.setpos(-400, -100)
win.bgcolor("lightgreen")
tito.pensize(1)
tito.fillcolor("#ADD8E6")

def getFibonanci():
    fibonanciList = [0, 1]
    numListStart = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numListEnd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 999):
        fibonanciList.append(fibonanciList[i] + fibonanciList[i - 1])
    for number in fibonanciList:
        for digit in range(0, 11):
            if int(str(number)[:1]) == digit:
                numListStart[digit] += 1
            if int(str(number)[-1:]) == digit:
                numListEnd[digit] += 1
    return [numListStart, numListEnd]
def drawBar(tito, height):
    tito.begin_fill()
    tito.left(90)
    tito.forward(height)
    tito.write(str(height))
    tito.right(90)
    tito.forward(40)
    tito.right(90)
    tito.forward(height)
    tito.left(90)
    tito.end_fill()

numListStart = getFibonanci()[0]
numListEnd = getFibonanci()[1]
print(numListStart)
print(numListEnd)
for number in numListStart:
    drawBar(tito, number)
for number in numListEnd:
    drawBar(tito, number)
win.exitonclick()
