#Hurdle 1 and hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    move();
    turn_left();
    move();
    turn_right();
    move();
    turn_right();
    move();
    turn_left();
  
#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    else :
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()

#Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right(): 
        move()
    turn_right()
    move() 
    turn_right()
    while front_is_clear(): 
        move()
    turn_left()

while not at_goal():
    if front_is_clear():  
        move()  
    else:
        jump()  
        
    
#Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def maze_move():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

while not at_goal():
    maze_move()
