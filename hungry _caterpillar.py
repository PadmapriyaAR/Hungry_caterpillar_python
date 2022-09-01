import random
import time
import turtle


#creating a turtle window
turtle.title("Hungry Caterpillar")
turtle.bgpic("newbkg.gif")
turtle.screensize(500,500)
turtle.tracer(1)


#creating a caterpillar(TurtleScreenobject)
#Assigning var name to instance to call it again and to stop window for displaying.
caterpillar=turtle.Turtle()
caterpillar.shape('square')
caterpillar.color('green')
caterpillar.fillcolor('green')
caterpillar.speed(6)
#penup stops turtle from drawing(no drawing when moving)
caterpillar.penup()
caterpillar.hideturtle()

#Creating a fruit
fruit=turtle.Turtle()
turtle.register_shape("apple-icon.gif")
fruit.shape('apple-icon.gif')
fruit.shapesize(0.1)
fruit.color('red')
fruit.penup()
fruit.hideturtle()
fruit.speed(0)

#Starting screen
game_started = False
start_text= turtle.Turtle()
start_text.write('Press Any Key to Start',align='center',font=('Times New Roman',50,'bold'))
start_text.hideturtle()
start_time=time.localtime()


#creating a time label
time_s=turtle.Turtle()
time_s.penup()
time_s.hideturtle()
time_s.setpos(236,270)
time_s.write("TIME:",align="left",font=("Arial",16,"bold"))

#creating a point label
point=turtle.Turtle()
point.penup()
point.hideturtle()
point.setpos(-380,270)
point.write("POINTS:",align="left",font=("Arial",16,"bold"))
point.speed(0)

#creating points
points = turtle.Turtle()
points.speed(0)
points.hideturtle()

#creating a time 
time_t=turtle.Turtle()
time_t.penup()
time_t.hideturtle()
time_t.setpos(295,270)
time_t.speed(0)

#displaying the time
def time_taken(difference):
   time_t.clear() 
   time_t.write(str(difference)+"s",font=("Arial",16))
   time_t.hideturtle()

# creating boundary
def boundary():
    left_b=-turtle.window_width()/2
    right_b=turtle.window_width()/2
    top_b = turtle.window_height()/2
    bottom_b = -turtle.window_height()/2
    #returns tutrle current location
    (x,y) = caterpillar.pos()
    boundary_reached = x < left_b or  x > right_b or  y < bottom_b or y > top_b
    return boundary_reached

#creating a last screen   
def game_over():
    turtle.penup()
    turtle.hideturtle()
    caterpillar.hideturtle()
    fruit.hideturtle()
    turtle.write('GAME OVER!!!',align='center',font=('Times New Roman',50,'bold'))
    turtle.exitonclick()
    
#Showing points on screen
def show_points(s_points):
     points.clear()
     points.penup()
     points.setpos(-280,270)
     points.write(s_points,align='left',font=('Times New Roman',15,'bold'))
     
    #points.write(str(s_points),align='left',font=('Times New Roman',15,'bold'))
     
#randomly placing the food
def place_fruit():
    fruit.hideturtle()
    fruit.setx(random.randint(-250,250))
    fruit.sety(random.randint(-250,250))
    fruit.showturtle()

#main game starts
def main_game():
   global game_started
   if game_started:
       return True
   game_started=True
   score = 0
   difference=0
   start_text.clear()
   #time_s.hideturtle()
   caterpillar_speed=4
   caterpillar_length=1
   caterpillar.shapesize(stretch_len=caterpillar_length)
   caterpillar.showturtle()
   show_points(score)
   place_fruit()

   while True:
       stop_time=time.localtime()
       difference=time.mktime(stop_time)-time.mktime(start_time)
       time_taken(difference)
       caterpillar.forward(caterpillar_speed)
       if(caterpillar.distance(fruit)<30):
           place_fruit()
           caterpillar_length=caterpillar_length+2
           caterpillar.shapesize(stretch_len=caterpillar_length)
           caterpillar_speed = caterpillar_speed + 1
           score=score+10
           show_points(score)
           time_taken(difference)
       if boundary():
           stop_time=time.localtime()
           difference=time.mktime(stop_time)-time.mktime(start_time)
           time_taken(difference)
           game_over()
           break

def up_key():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def down_key():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def left_key():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def right_key():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

turtle.onkeypress(main_game,'')
turtle.onkey(up_key,'Up')
turtle.onkey(right_key,'Right')
turtle.onkey(down_key,'Down')
turtle.onkey(left_key,'Left')
turtle.listen()
turtle.mainloop()
