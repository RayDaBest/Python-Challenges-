import turtle 

def triangle_draw(x,y,z): 
  turtle.speed(0)
  turtle.penup
  turtle.goto(x,y)
  turtle.pendown
  for i in range (4): 
    turtle.forward(z)
    turtle.right(90)

triangle_draw(0,0,10)
