import turtle
turtle.bgcolor("black")
door=turtle.Turtle()
door.speed(0)
door.shape("circle")
door.pencolor("pink")

def circle(r): 	
	turtle.draw_circle(20)
maya=turtle.Turtle()
maya.speed(0)
maya.shape("triangle")
maya.pencolor("purple")



door.ondrag(door.goto,btn=1)
maya.ondrag(maya.goto,btn=3)

#def write():
	#turtle.pu()
	#turtle.onclick(turtle.goto)
	#turtle.pd()
#turtle.onskreenclick(write,btn=1)
#turtle.onskreenclick(circle,btn=3)
#door.write(door.goto,btn=1)
#maya.write(maya.goto,btn=3)


turtle.mainloop()
