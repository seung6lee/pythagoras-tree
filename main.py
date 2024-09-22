import turtle as t
import math


t.setup(1000, 1000)
t.shape('turtle')
t.speed(0)
t.setheading(180)

def tree(theta=60, len=100, depth=0):
    if depth == end:
        return

    rad_theta = math.radians(theta)

    t.down()
    t.color('black')
    for i in range(4):
        t.fd(len)
        t.lt(90)
    
    t.up()
    r_new_len = len * math.cos(rad_theta)
    r_x = r_new_len * math.sin(rad_theta)
    r_y = r_new_len * math.cos(rad_theta)
    t.lt(180)
    t.fd(r_x)
    t.lt(90)
    t.fd(r_y)
    t.lt(90 - theta)
    tree(theta, r_new_len, depth+1)

    t.lt(90 + theta)
    t.fd(r_y)
    t.lt(270)
    t.fd(r_x)

    l_new_len = len * math.sin(rad_theta)
    l_x = len * (math.sin(rad_theta) + math.cos(rad_theta)) * math.cos(rad_theta)
    l_y = len * (math.sin(rad_theta) + math.cos(rad_theta)) * math.sin(rad_theta)
    print(l_x, l_y)
    t.fd(l_x)
    t.lt(270)
    t.fd(l_y)
    t.lt(90 + 90 - theta)
    tree(theta, l_new_len, depth+1)

    t.lt(theta)
    t.fd(l_y)
    t.lt(90)
    t.fd(l_x)
    t.lt(180)
    

end = 5
theta = 60
len = 100

tree(theta, len)
t.done()