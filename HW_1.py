def put():
    pass


def toss():
    pass


def think(n):
    n = 0
    

def move():
    pass


def take():
    pass


def turn_left():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_back():
    turn_left()
    turn_left()


def object_here():
    pass


def wall_on_right():
    pass


def front_is_clear():
    pass


def right_is_clear():
    pass


def at_goal():
    pass


#Around 1:
put()
move()
x = object_here()
for i in range(4):
    while front_is_clear():
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
    while front_is_clear():
        move()
        x = object_here()
        if x == ['token']:
            break
    turn_left()


#Around 1 - apple:
x = object_here()
for i in range(4):
    while front_is_clear():
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
    while front_is_clear():
        x = object_here()
        if x == ['token']:
            break
        if right_is_clear():
            break
        move()
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


#Around 3:
turn_left()
put()
x = object_here()
move()
while True:
    while front_is_clear():
        x = object_here()
        if x == ['token']:
            break
        if right_is_clear():
            break
        move()
    if x == ['token']:
            break
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


#Around 4:
turn_back()
put()
x = object_here()
move()
while True:
    while front_is_clear():
        x = object_here()
        if x == ['token']:
            break
        if right_is_clear():
            break
        move()
    if x == ['token']:
        break
    if right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


#Center 1:
x = 0
while front_is_clear():
    move()
    x += 1
turn_back()
for i in range(int(x/2)):
    move()
put()


#Center 2:
turn_left()
x = 0
while front_is_clear():
    move()
    x +=1
turn_back()
for i in range(int(x/2)):
    move()
put()


#Harvest 1:
def harvest_one_row1():
    for _ in range(6):
        move()
        object_here()
        if object_here() == ["carrot"]:
            take()
    move()


move()
turn_left()
move()
move()
turn_right()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_right()
        move()
        turn_right()
    else:
        turn_left()
        move()
        turn_left()







#Harvest 2:
def harvest_one_row1():
    for _ in range(6):
        move()
        object_here()
        if object_here() == ["carrot"]:
            while object_here() == ["carrot"]:
                take()
                object_here()
    move()


move()
turn_left()
move()
move()
turn_right()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_right()
        move()
        turn_right()
    else:
        turn_left()
        move()
        turn_left()




#Harvest 3:
think(50)


def harvest_one_row1():
    for _ in range(6):
        move()
        object_here()
        if object_here() == ["carrot"]:
            while object_here() == ["carrot"]:
                take()
                object_here()
        put()
    move()


move()
turn_left()
move()
move()
turn_right()
x = 0

for i in range(6):
    harvest_one_row1()
    x += 1
    if x % 2 == 0:
        turn_right()
        move()
        turn_right()
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
    turn_right()
    move()
    turn_right()
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
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()



#Hurdle 3:
think(20)


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    while front_is_clear():
        move()
    jump()



#Hurdle 4:
think(20)


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
    while front_is_clear():
        move()
    jump()




#Maze:
think(20)


def turn_right():
    turn_right()


while not at_goal():
    if right_is_clear():
        turn_right()
        if at_goal():
            break
        move()
    elif front_is_clear():
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
    turn_right()
    move()
    move()


def step_down():
    move()
    move()
    turn_left()
    move()
    turn_right()


for i in range(3):
    step_up()
put()
turn_back()
for i in range(3):
    step_down()



#Newspaper 1:
think(20)
take()
x = 0


def step_up():
    turn_left()
    move()
    turn_right()
    move()
    move()


def step_down():
    move()
    move()
    turn_left()
    move()
    turn_right()


for i in range(3):
    step_up()
while object_here() == ['token']:
    take()
put('star')
turn_back()

for i in range(3):
    step_down()


#Rain 0:
think(20)
for i in range(6):
    move()
build_wall()
turn_back()
for i in range(5):
    move()

# Rain 1:
think(20)


def turn_right():
    turn_right()


move()
turn_right()
move()

x = 0
y = -1
n = 0
m = -1
i = 0
while x != 0 or y != 0:
    while not right_is_clear():
        if front_is_clear():
            move()
            x += n
            y += m
        else:
            turn_left()
            i += 1
            if i % 4 == 0:
                m = -1
                n = 0
            if i % 4 == 1:
                m = 0
                n = 1
            if i % 4 == 2:
                m = 1
                n = 0
            if i % 4 == 3:
                m = 0
                n = -1
    if x == 0 and y ==0:
        break
    turn_right()
    build_wall()
    turn_left()
    move()
    x += n
    y += m


# Rain 2:
think(20)
def turn_right():
    turn_left()
    turn_left()
    turn_left()


move()
move()
move()
turn_right()
move()

x = 0
y = -1
n = 0
m = -1
i = 0
while x != 0 or y != 0:
    while not right_is_clear():
        if front_is_clear():
            move()
            x += n
            y += m
        else:
            turn_left()
            i += 1
            if i % 4 == 0:
                m = -1
                n = 0
            if i % 4 == 1:
                m = 0
                n = 1
            if i % 4 == 2:
                m = 1
                n = 0
            if i % 4 == 3:
                m = 0
                n = -1
    if x == 0 and y ==0:
        break
    move()
    if right_is_clear():
        i -= 1
        turn_back()
        move()
        turn_left()
        move()
    else:
        turn_back()
        move()
        turn_left()
        build_wall()
        turn_left()
        move()
    if i % 4 == 0:
        m = -1
        n = 0
    if i % 4 == 1:
        m = 0
        n = 1
    if i % 4 == 2:
        m = 1
        n = 0
    if i % 4 == 3:
        m = 0
        n = -1

    x += n
    y += m


# Storm 1:
think(20)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
n = 0
while front_is_clear():
    move()
    while object_here() == ["leaf"] :
        take()
        n += 1
turn_back()
while front_is_clear():
    move()
turn_right()
while n != 0:
    toss()
    n -= 1


# Storm 2:
think(20)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
n = 0
m = 0
for i in range(6):
    while front_is_clear():
        while object_here() == ["leaf"]:
            take()
            n += 1
            object_here()
        move()
    if wall_on_right() and m != 0:
        break
    if i % 2 == 0:
        turn_left()
        move()
        turn_left()
    else:
        turn_right()
        move()
        turn_right()
    m += 1
turn_back()
for i in range(3):
    while front_is_clear():
        move()
    turn_right()
turn_right()
for i in range(4):
    while front_is_clear():
        while object_here() == ["leaf"]:
            take()
            n+=1
            object_here()
        move()
    turn_left()
for i in range(4):
    while front_is_clear():
        move()
    turn_right()
turn_left()
while n != 0:
    toss()
    n -= 1







#  Storm 3,4:
think(20)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
n = 0
m = 0
x = 0
u = 0
while front_is_clear():
    move()
    x += 1
turn_back()
while front_is_clear():
    move()
turn_back()
while not wall_on_right() or front_is_clear() or m < 1:
    y = 0
    while front_is_clear():
        while object_here() == ["leaf"]:
            take()
            n += 1
            object_here()
        move()
        y += 1
    while object_here() == ['leaf']:
            take()
            n += 1
            object_here()
    if y < x - 1 and u == 0:
        turn_right()
        move()
        while object_here() == ['leaf']:
            take()
            n += 1
            object_here()
        turn_left()
        move()
        while object_here() == ['leaf']:
            take()
            n += 1
            object_here()
        move()
        while object_here() == ['leaf']:
            take()
            n += 1
            object_here()
        turn_left()
        move()
        turn_right()
        u += 1
        continue
    if wall_on_right() and not front_is_clear() and m >= 1:
        break
    if m%2 == 0:
        turn_left()
        move()
        turn_left()
    elif m == 1:
        turn_right()
        move()
        turn_left()
        move()
        turn_back()
    else:
        turn_right()
        move()
        turn_right()
    m += 1
turn_left()
if not front_is_clear():
    turn_left()

while not at_goal():
    while front_is_clear():
        move()
    turn_left()
    move()
    if right_is_clear():
        turn_right()
        move()
        move()
        turn_right()
        move()
        turn_right()

while n != 0:
    toss()
    n -= 1


#Tokens 1,2,3:
think(20)
n = 0
while not at_goal():
    object_here()
    while object_here() == ['token'] and n < 1:
        take()
        toss()
        n += 1
        object_here()
    move()


#Tokens 4:
think(20)
n = 0
while not at_goal():
    object_here()
    while object_here() == ['token']:
        take()
        n += 1
        object_here()
    move()
turn_back()
while n != 0:
    toss()
    n -= 1


#Tokens 5:
think(20)
n = 0
while not at_goal():
    object_here()
    while object_here() == ['token']:
        take()
        n += 1
        object_here()
    move()
turn_back()
move()
while n != 0:
    toss()
    n -= 1
turn_back()
move()
