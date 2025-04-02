import pgzrun
WIDTH = 800
HEIGHT = 500

apple = Actor('apple.png')
apple.pos = 100,250 

def startanimation():
    animate(apple,pos = (650,250)  , duration = 2)
    
def draw():
    screen.clear()
    apple.draw()

startanimation()
pgzrun.go()
