import pgzrun
WIDTH = 1500
HEIGHT = 800
box1 = Rect((50,250),(150,100))
box2 = Rect((650,250),(150,100))
box3 = Rect((350,0),(150,100))
box4 = Rect((350,500),(150,100))
bvx = 2
b2vx = -2
b3vx = 1
b4vx = 1

def draw():
    screen.fill('black')
    screen.draw.filled_rect(box1,'yellow')
    screen.draw.filled_rect(box2,'blue')
    screen.draw.filled_rect(box3,'Red')
    screen.draw.filled_rect(box4,'white')

def update():
    global bvx,b2vx,b3vx,b4vx
    box1.x += bvx
    box2.x += b2vx
    box3.y += b3vx
    box4.y += b4vx

    if box1.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.explosion1.play()

    if box3.colliderect(box4):
        b3vx = -b3vx
        b4vx = -b4vx
        sounds.cling.play()


    if box1.left < 0:
        bvx = -bvx
        sounds.explosion1.play()

    if box2.right > 850:
        b2vx = -b2vx
        sounds.explosion1.play()    

    if box3.top < 0:
        b3vx = -b3vx
        sounds.cling.play()

    if box4.bottom > 600:
        b4vx = -b4vx
        sounds.cling.play()

    
pgzrun.go()