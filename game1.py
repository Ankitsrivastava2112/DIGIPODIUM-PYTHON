import pgzrun
box = Rect((50,50),(150,100))
box2 = Rect((600,50),(150,100))
box3 = Rect((300,50),(150,100))
box4 = Rect((300,200),(150,100))
bvx = 5
b2vx = -5
b3vx = 5
b4vx = -5

def draw():
    screen.fill('black')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box2,'Purple')
    screen.draw.filled_rect(box3,'Red')
    screen.draw.filled_rect(box4,'Green')

def update():
    global bvx,b2vx,b3vx,b4vx
    box3.y += b3vx
    box4.y += b4vx
    box.x += bvx
    box2.x += b2vx

    if box3.colliderect(box4):
        b3vx = -b3vx
        b4vx = -b4vx

    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.explosion1.play()

    if box3.top < -600:
        b3vx = -b3vx
        sounds.cling.play()

    if box4.bottom > 600:
        b4vx = -b4vx
        sounds.cling.play()

    if box.left <0:
        bvx = -bvx
        sounds.explosion1.play()

    if box2.right > 800:
        b2vx = -b2vx
        sounds.explosion1.play()


pgzrun.go()