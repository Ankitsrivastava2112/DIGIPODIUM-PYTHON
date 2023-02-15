from turtle import*
speed(0)
pencolor('blue')
fillcolor('yellow')
pensize(5)
side = 5
for i in range(side):
    fd(150)
    begin_fill()
    for i in range(side):
        fd(75)
        for i in range(side):
            fd(75/2)
            lt(360/side)
            dot(25)
        rt(360/side)        
    end_fill()
    lt(360/side)    

done()
hideturtle()    