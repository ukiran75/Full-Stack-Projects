import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    uday = turtle.Turtle()
    uday.shape('turtle')
    uday.color('black')
    uday.speed(2)
    for i in range(0,72):
        draw_square(uday)
        uday.left(5)
    #draw_circle(uday)
    window.exitonclick()

def draw_square(given_turtle):
     for i in range(0,4):
        given_turtle.forward(70)
        given_turtle.left(90)
def draw_circle(given_turtle):
    given_turtle = turtle.Turtle()
    given_turtle.circle(100)

draw_art()