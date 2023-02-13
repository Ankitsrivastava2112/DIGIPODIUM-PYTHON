from turtle import*
speed(0)
def polygon(side,dis):
    for i in range(side):
        fd(dis)
        lt(360/side)

for i in range(3,100):
    polygon(3,i*10)
    bk(5)
done()    