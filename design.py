import turtle as t
t.speed(0)

tle = t.Turtle()
t.bgcolor('black')
t.speed(0)

for i in range(10):
    for color in ['red', 'magenta', 'blue']:
        t.color(color)
        t.pensize(3)
        t.left(12)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
inp = input()        
