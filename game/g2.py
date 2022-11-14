import pgzrun
HEIGHT =  600
WIDTH = 800

c = Actor('chick',(100,100))
w = Actor('walrus',(300,300))

def draw():
    screen.fill("white")
    c.draw()
    w.draw()
   # #screen.draw.text("A chicken story", (10,WIDTH//2),'red')

def update():
    if keyboard.W:
        c.y -= 3
    elif keyboard.S:
        c.y += 3
    elif keyboard.A:
        c.x -= 3
    elif keyboard.D:
        c.x += 3

pgzrun.go()




