import turtle
# Variable remeber attribuites they hold onto a piece of info
# Functions are used to remember lines of code


# By simply putting this we are saying yes this is a code for a square
#   Square
#   mo = turtle.Turtle()
#   mo.forward(100)
#   mo.right(90)
#   mo.forward(100)
#   mo.right(90)
#   mo.forward(100)
#   mo.right(90)
#   mo.forward(100)
#   turtle.mainloop()

# A better more efficient way of doing this is by simply making a function
# making a function requires you to def (define), give a name, then place
# what you want it to do inside
mo = turtle.Turtle()
def square():
    x = input()
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
    mo.right(90)
    mo.forward(100)
# if you run it nothing will happen because you must call the function
square()
#to get more square in different position you will remove the object from the function
#after doing this you may do the followig
mo.forward(200)
square()
mo.right(90)
mo.forward(200)
square()




turtle.mainloop()