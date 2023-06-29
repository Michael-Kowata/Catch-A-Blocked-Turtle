#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
import time

colors=["red","orange","yellow","purple","white"]

#-----game configuration----
turtle_sizeE=3
turtle_sizeH=2
turtle_size=3
turtle_color="green"
turtle_shape="turtle"

spike_size=5
spike_shape="triangle"

score=0
num1=0
num2=0

font_setup=("Ariel", 20, "normal")

timer = 30
counter_interval = 1000  
timer_up = False

# leaderboard variables
leaderboard_file_name = "a125_leaderboard.txt"
player_name = input ("Please enter your name:")
difficulty = input ("Easy or Hard? (enter e/h) ")

#-----initialize turtle-----
spot = trtl.Turtle() 
spot.shape(turtle_shape)
if difficulty.upper()=="E":
  spot.shapesize(3)
elif difficulty.upper()=="H":
  spot.shapesize(2)
spot.fillcolor(turtle_color)


spike = trtl.Turtle()
spike.shape(spike_shape)
spike.shapesize(spike_size)
spike.fillcolor(rand.choice(colors))


spike2 = trtl.Turtle()
spike2.shape(spike_shape)
spike2.shapesize(spike_size)
spike2.fillcolor(rand.choice(colors))


spike3 = trtl.Turtle()
spike3.shape(spike_shape)
spike3.shapesize(spike_size)
spike3.fillcolor(rand.choice(colors))


spike4 = trtl.Turtle()
spike4.shape(spike_shape)
spike4.shapesize(spike_size)
spike4.fillcolor(rand.choice(colors))


score_writer=trtl.Turtle()

counter=trtl.Turtle()

#-----game functions-----

def change_turtle(x,y):
  new_xpos=rand.randint(-200,200)
  new_ypos=rand.randint(-200,200)
  spot.penup()
  spot.hideturtle()
  spot.goto(new_xpos, new_ypos)
  spot.pendown()
  spot.showturtle()


def change_spike(x,y):
  new_xpos=rand.randint(-100,100)
  new_ypos=rand.randint(-100,100)
  spike.penup()
  spike.hideturtle()
  spike.goto(new_xpos, new_ypos)
  spike.pendown()
  spike.showturtle()

def change_spike2(x,y):
  new_xpos=rand.randint(-150,150)
  new_ypos=rand.randint(-150,150)
  spike2.penup()
  spike2.hideturtle()
  spike2.goto(new_xpos, new_ypos)
  spike2.pendown()
  spike2.showturtle()

def change_spike3(x,y):
  new_xpos=rand.randint(-200,200)
  new_ypos=rand.randint(-200,200)
  spike3.penup()
  spike3.hideturtle()
  spike3.goto(new_xpos, new_ypos)
  spike3.pendown()
  spike3.showturtle()

def change_spike4(x,y):
  new_xpos=rand.randint(-250,250)
  new_ypos=rand.randint(-250,250)
  spike4.penup()
  spike4.hideturtle()
  spike4.goto(new_xpos, new_ypos)
  spike4.pendown()
  spike4.showturtle()

def update_score():
  global score 
  global num1
  score += 1
  score_writer.pencolor("black")
  score_writer.penup()
  score_writer.hideturtle()
  score_writer.goto(250, 220)
  score_writer.clear()
  score_writer.write(score, font=font_setup)
  num1=num1+1

def minus_score():
  global score
  global num2
  score_writer.pencolor("black")
  score=score-1
  score_writer.penup()
  score_writer.hideturtle()
  score_writer.goto(250, 220)
  score_writer.clear()
  score_writer.write(score, font=font_setup)
  num2=num2+1
  

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
    

def countdown():
  counter.penup()
  counter.hideturtle()
  counter.goto(-290, 220)
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def size_change(t_size, s_size):
  global score
  global turtle_size
  diff=(s_size-t_size)
  small_t=(t_size-diff)
  if timer_up==False:
    if (score>=15):
      turtle_size=small_t
      spot.shapesize(turtle_size)

def turtle_clicked(x,y):
  if timer_up==False:
    change_turtle(x,y)
    update_score()
    if difficulty.upper()=="E":
      spot.shapesize(3)
      size_change(4,5)
    elif difficulty.upper()=="H":
      spot.shapesize(2)
      size_change(2,3)
  else:
    spot.hideturtle()
    score_writer.penup()

def spike_clicked(x,y):
  if timer_up==False:
    minus_score()
  else:
    spike.hideturtle()
    score_writer.penup()
    
def spike_clicked2(x,y):
  if timer_up==False:
    minus_score()
  else:
    spike2.hideturtle()
    score_writer.penup()

def spike_clicked3(x,y):
  if timer_up==False:
    minus_score()
  else:
    spike3.hideturtle()
    score_writer.penup()

def spike_clicked4(x,y):
  if timer_up==False:
    minus_score()
  else:
    spike4.hideturtle()
    score_writer.penup()

#---------events---------
score_writer.hideturtle()

spot.onclick(turtle_clicked)
spike.onclick(spike_clicked)
wn = trtl.Screen() 
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("blue")
while timer_up==False:
  x=rand.randint(0,0)
  y=rand.randint(0,0)
  time.sleep(0.75)
  change_spike(x,y)
  change_spike2(x,y)
  change_spike3(x,y)
  change_spike4(x,y)
spike.hideturtle()
spike2.hideturtle()
spike3.hideturtle()
spike4.hideturtle()
spot.hideturtle()
  
wn.mainloop()
