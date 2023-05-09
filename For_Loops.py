import turtle
mo = turtle.Turtle()
mo.speed(5)
def square():
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)

for i in range(4):
    square()


turtle.mainloop()

