import turtle
mo = turtle.Turtle()
def square():
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)

elephant_weight = 3000
ant_weight = 0.1

if elephant_weight < ant_weight:
    square()
else:
    mo.forward((100))




turtle.mainloop()