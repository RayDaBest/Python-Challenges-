import turtle 
def triangle_draw(x): 
  turtle.speed(0)
  turtle.penup()
  for j in range(6): 
    for i in range(3): 
      turtle.pendown()
      turtle.forward(50)
      turtle.right(120)
    turtle.forward(50)
    turtle.right(60)
triangle_draw(10)