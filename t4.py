#star
from turtle import*
side=8
speed("fast")
si=3
for i in range(side):
    color("blue")
    rt(360/side)
    fd(100)
    dot(20)

    for i in range(si):
         color("red")
         rt(360/si)
         fd(100)    
done()