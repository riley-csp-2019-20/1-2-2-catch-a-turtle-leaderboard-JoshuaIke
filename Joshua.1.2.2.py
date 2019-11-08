# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb
#-----game configuration----
turtleshape= "turtle"
turtlecolor= "brown"
turtlesize = 3
score=0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#scoreboard variables
leaderboard_file_name="a122_leaderboard.txt"
leader_names_list= []
leader_scores_list= []
player_name= input("Please Enter Name")
#-----initialize turtle-----
Boota = trtl.Turtle(shape=turtleshape)
Boota.color(turtlecolor)
Boota.shapesize(turtlesize)
Boota.speed(0)
Scoreboard=trtl.Turtle()
Scoreboard.penup()
Scoreboard.goto(390,360)
Scoreboard.ht()
Scoreboard.write(score, font=font_setup)
font_setup=("Arial",30, "bold")

counter =  trtl.Turtle()
counter.penup()
counter.goto(-400,340)
counter.ht()
#-----game functions--------
def Boota_clicked(x,y):
    print("Boota got clicked")
    change_position()
    update_score()
    change_color()


def change_position():
    Boota.penup()
    Boota.ht()
    if not timer_up:
        Bootax = random.randint(-400,400)
        Bootay = random.randint(-300,300)
        Boota.goto(Bootax,Bootay)
        Boota.st()  

def update_score():
    global score
    score += 1
    print(score)
    Scoreboard.clear()
    Scoreboard.write(score, font= font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Game Over", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#this code changes the mole color when clicked
def change_color():
    Boota_colors = ["teal", "blue", "green", "orange", "purple", "tan"]
    new_color = random.choice(Boota_colors)
    if timer == 29:
        new_color("tan")

    Boota.color(new_color)

def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global Boota

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, Boota, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, Boota, score)



#-----events----------------
wn = trtl.Screen()
#this is the code that changes the backgroundcolor line 71.
wn.bgcolor("lightblue")
Boota.onclick(Boota_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()