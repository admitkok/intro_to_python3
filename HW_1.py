#Around 1:
put()
move()
x = object_here()
for i in range(4):
    while(front_is_clear()):
        move()
        x = object_here()
        if x == ['token']:
            break  
    turn_left()


#Around 1 - variable:
put()
move()
x = object_here()
for i in range(5):
    while(front_is_clear()):
        move()
        x = object_here()
        if x == ['token']:
            break  
    turn_left()


#Around 1 - apple:
x = object_here()
for i in range(4):
    while(front_is_clear()):
        move()
        x = object_here()
        if x == ['apple']:
            take() 
    turn_left()
   
   
#Around 2:
put()
x = object_here()
move()
for i in range(7):
    while(front_is_clear()):
        x = object_here()
        if x == ['token']:
            break
        if(right_is_clear() == True):
            break
        move()
    if(right_is_clear() == True):
        turn_left()
        turn_left()
        turn_left()
        move()
    else:   
        turn_left()


#Around 3:
turn_left()
put()
x = object_here()
move()
while(True):
    while(front_is_clear()):
        x = object_here()
        if x == ['token']:
            break
        if(right_is_clear() == True):
            break
        move()
    if x == ['token']:
            break
    if(right_is_clear() == True):
        turn_left()
        turn_left()
        turn_left()
        move()
    else:   
        turn_left()
   
   
#Around 4:
turn_left()
turn_left()
put()
x = object_here()
move()
while(True):
    while(front_is_clear()):
        x = object_here()
        if x == ['token']:
            break
        if(right_is_clear() == True):
            break
        move()
    if x == ['token']:
            break
    if(right_is_clear() == True):
        turn_left()
        turn_left()
        turn_left()
        move()
    else:   
        turn_left()
        
        
#Center 1:
x = 0
while(front_is_clear()):
    move()
    x +=1
turn_left()
turn_left()
for i in range(int(x/2)):
    move()
put()


#Center 2:
turn_left()
x = 0
while(front_is_clear()):
    move()
    x +=1
turn_left()
turn_left()
for i in range(int(x/2)):
    move()
put()


#Harvest 1:
def harvest_one_row1():
    for _ in range(6):
        move()
        n = object_here()
        if (n == ["carrot"]):
            take()
    move()


move()
turn_left()
move()
move()
turn_left()
turn_left()
turn_left()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
        move()
        turn_left()







#Harvest 2:
def harvest_one_row1():
    for _ in range(6):
        move()
        n = object_here()
        if (n == ["carrot"]):
            while n == ["carrot"]:
                take()
                n = object_here()
    move()


move()
turn_left()
move()
move()
turn_left()
turn_left()
turn_left()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
        move()
        turn_left()


    
    
#Harvest 3:
think(50)
def harvest_one_row1():
    for _ in range(6):
        move()
        n = object_here()
        if (n == ["carrot"]):
            while n == ["carrot"]:
                take()
                n = object_here()
        put()
    move()


move()
turn_left()
move()
move()
turn_left()
turn_left()
turn_left()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
        move()
        turn_left()




#Hurdle 1:
think(20)
def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

for i in range(6):
    jump()
    
    

#Hurdle 2:
think(20)
def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

while(at_goal() == False):
    jump()



#Hurdle 3:
think(20)
def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

while(at_goal() == False):
    while(front_is_clear() == True):
        move()
    jump()



#Hurdle 4:
think(20)
def jump():
    turn_left()
    while(wall_on_right() == True):
        move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    while(front_is_clear() == True):
        move()
    turn_left()

while(at_goal() == False):
    while(front_is_clear() == True):
        move()
    jump()




#Maze:
think(20)
while(at_goal() == False):
    if(right_is_clear() == True):
        turn_left()
        turn_left()
        turn_left()
        if(at_goal() == True):
            break
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
        
 
 
#Newspaper 0:
think(20)
take()
x = 0
def step_up():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    
def step_down():
    move()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    
for i in range(3):
    step_up()
put()
turn_left()
turn_left()

for i in range(3):
    step_down()

    
    
#Newspaper 1:
think(20)
take()
x = 0
def step_up():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    move()
    
def step_down():
    move()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    
for i in range(3):
    step_up()
while object_here() == ['token']:
    take()
put('star')
turn_left()
turn_left()

for i in range(3):
    step_down()