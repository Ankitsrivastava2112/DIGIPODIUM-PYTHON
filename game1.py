import pgzrun
box = Rect((50,50),(150,100))
box2 = Rect((600,50),(150,100))
box3 = Rect((300,50),(150,100))
box4 = Rect((300,200),(150,100))
bvx = 5
b2vx = -5
def draw():
    screen.fill('black')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box2,'Purple')
    screen.draw.filled_rect(box3,'Red')
    screen.draw.filled_rect(box4,'Green')

def update():

    box3.y +=1
    box4.y -=1
    global bvx,b2vx
    box.x += bvx
    box2.x += b2vx

    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.cling.play()

    if box.left <0:
        bvx = -bvx
        sounds.cling.play()

    if box2.right > 800:
        b2vx = -b2vx
        sounds.cling.play()


pgzrun.go()