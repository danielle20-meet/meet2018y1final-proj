import turtle, random,time
turtle.bgpic("seabg.png")#background as a picture
turtle.setup(1800,1200)#size of the screen
turtle.penup()
turtle.tracer(1,0)
turtle.goto(0,300)
turtle.hideturtle()
turtle.write("Welcome if you wanna play press space", align="center", font =("Ariel" , 40, "normal"))
score=0
direction = "up"

# set up turtles
turtle.register_shape("coin.gif")#make the turtle as a coin
coin = turtle.clone()#main that every thing that turtle was now coin are
coin.shape("coin.gif")
coin.speed(0)#the fastest speed
coin.penup()
coin.hideturtle()
coin2 = coin.clone()#make the seconed coin as same as the first one
coin2.speed(0)
coin2.hideturtle()
coin3 = coin.clone()
coin3.speed(0)
coin3.hideturtle()

jfish = turtle.Turtle()
turtle.register_shape("jfish.gif")#make the turtle as a cjfish
jfish.shape("jfish.gif")
jfish.penup()
jfish.hideturtle()
jfish.speed(0)
jfish2 = jfish.clone()#make the seconed jfish as same as the first one
jfish3 = jfish.clone()


trash = turtle.Turtle()
turtle.register_shape("plasticbag.gif")
trash.shape("plasticbag.gif")
trash.hideturtle()
trash.penup()
trash2=trash.clone()
trash3=trash.clone()

def make():#make the coin
    global coin,score,coin2,coin3,jfish,jfish2,jfish3
    y_pos = random.randint(-12,12)*40#set the random "y"
    coin.goto(500,y_pos)
    coin.showturtle()
    coin2.goto(500, random.randint(-12, 12)*40)
    coin2.showturtle()
    coin3.goto(500, random.randint(-12, 12)*40)
    coin3.showturtle()
    print("Making jellyfish!")
    y_pos = random.randint(-12,12)*40#set the random "y"
    print("First random y position: " + str(y_pos))

    jfish.goto(500, random.randint(-12, 12)*40)#jfish go th the start pos
    jfish.showturtle()
    jfish.speed(0)
    jfish2.goto(500, random.randint(-12, 12)*40)
    jfish2.showturtle()
    jfish3.goto(500, random.randint(-12, 12)*40)
    jfish3.showturtle()

    trash.goto(500, random.randint(-12, 12)*40)#jfish go th the start pos
    trash.showturtle()
    trash.speed(0)
    trash2.goto(500, random.randint(-12, 12)*40)
    trash2.showturtle()
    trash2.speed(0)
    trash3.goto(500, random.randint(-12, 12)*40)
    trash3.showturtle()
    trash3.speed(0)
    
def move():
    global score,jfish,jfish2,jfish3,coin,coin2,coin3
    jfish.back(8)
    coin.back(8)
    coin2.back(8)
    coin3.back(8)
    jfish2.back(8)
    jfish3.back(8)
    trash.back(8)
    trash2.back(8)
    trash3.back(8)
    if coin.pos()[0]==-500 or coin2.pos()[0]==-500 or coin3.pos()[0]==-500: #check if the jfish is in the same x as the sea turtle
        if abs(coin.pos()[1] - seat.pos()[1]) <= 40 or abs(coin2.pos()[1] - seat.pos()[1]) <= 40  or abs(coin3.pos()[1] - seat.pos()[1]) <= 40:#check if the sea t in the range of the coin
            print("you caught the coin")
            score-=75
            turtle.clear()
            turtle.write(score ,move=False, align="center", font=("Ariel", 30, "normal"))#cahnge the score
            make()#the coins +jfish return to the start
        if score <= -100:
            turtle.clear()
            turtle.write("Game over! your score is " +str(score) , move=False, align="center", font=("Ariel", 30, "normal"))        
            time.sleep(5)
            turtle.clear()
            score=0
            turtle.write("Restart", move=False, align="center", font=("Ariel", 30, "normal"))    
            
    
    if jfish.pos()[0]==-500 or jfish2.pos()[0]==-500 or jfish3.pos()[0]==-500: #check if the jfish is in the same x as the sea turtle
        print("you caught the jellyfish")
        if abs(jfish.pos()[1] - seat.pos()[1]) <= 80 or abs(jfish2.pos()[1] - seat.pos()[1]) <= 80  or abs(jfish3.pos()[1] - seat.pos()[1]) <= 80:#check if the sea t in the range of the jfish
            score+=150
            turtle.clear()
            turtle.write(score , move=False, align="center", font=("Ariel", 30, "normal"))        
            make()
    if trash.pos()[0]==-500 or trash2.pos()[0]==-500:
         if abs(trash.pos()[1] - seat.pos()[1]) <= 80 or abs(trash2.pos()[1] - seat.pos()[1]) <= 80:#check if the sea t in the range of the jfish
            turtle.clear()
            turtle.write("Game over! your score is " +str(score) , move=False, align="center", font=("Ariel", 30, "normal"))        
            time.sleep(5)
            turtle.clear()
            score=0
            turtle.write("Restart", move=False, align="center", font=("Ariel", 30, "normal"))    
    if jfish.pos()[0] <-850:
        make()
   
    turtle.ontimer(move, 10)

def game():
    #if the player presses the space button then the game begins
    global seat,score,direction
    turtle.clear()
    turtle.register_shape("seat.gif")
    seat = turtle.clone()
    seat.showturtle()
    seat.shape("seat.gif")
    seat.penup()
    seat.goto(-500,0)
    make()
    move()

def up():
    #if the player presses the up button then it'll go up
    global seat,score, direction #every change with this var will stay for the game
    direction = "up"
    
    pos_list = seat.pos()
    x_pos = pos_list[0]
    y_pos = pos_list[1]
    seat.goto(x_pos, y_pos+40)
    print("you pressed the up key!")
    x_pos = pos_list[0]
    y_pos = pos_list[1]

    print("New y pos:")
    print(y_pos)
    
    if y_pos>480 or y_pos<-480:
        turtle.clear()
        turtle.write("GAME OVER" ,move=False, align="center", font=("Ariel",50,"normal"))
        time.sleep(1)
        turtle.clear()
        score=0
        turtle.write("Restart", move=False, align="center", font=("Ariel", 30, "normal"))
        time.sleep(1)
        turtle.clear()
        seat.goto(x_pos,y_pos-100)

        
def down():
    #if the player presses the down button then it'll go down
    global seat,down_e,up_e,score
    direction = "down"
    pos_list = seat.pos()
    x_pos = pos_list[0]
    y_pos = pos_list[1]
    seat.goto(x_pos, y_pos-40)
    x_pos = pos_list[0]
    y_pos = pos_list[1]
    print("you pressed the down key!")
    if y_pos>480 or y_pos<-480:#what happened when your downer thn the edge
        turtle.clear()
        turtle.write("GAME OVER" ,move=False, align="center", font=("Ariel",50,"normal"))
        time.sleep(1)
        turtle.clear()
        score=0
        turtle.write("Restart", move=False, align="center", font=("Ariel", 30, "normal"))
        time.sleep(1)
        turtle.clear()
        seat.goto(x_pos,y_pos+100)  
        
        
    
#main program
up_e=500
down_e=-500

turtle.onkeypress(game, "space")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down,"Down")
turtle.listen()
lines= turtle.clone()
lines.hideturtle()
lines.penup()
lines.goto(-860,500)
lines.speed(0)
for i in range(2):
    lines.pendown()
    lines.pensize(5)
    lines.forward(1700)
    lines.right(90)
    lines.forward(1000)
    lines.right(90)


    

up_e=500
down_e=-500

turtle.mainloop()







