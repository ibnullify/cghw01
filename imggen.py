# -*- coding: utf-8 -*-

import random

file = open('image.ppm', 'w')

file.write("P3\n")
file.write("500 500\n")
file.write("255\n")


arr=[]
def makeBackground():
    str = ""
    for y in range(500):
        for x in range(500):
            str+= "255 0 0 "
        str += "\n"
    return str

#row size is 500
#element is going to be 500*row + column
def makeBack(arr):
    for y in range(500):
        for x in range(500):
            arr.append( "0 220 0 ")
    return arr

#level = distance from the edge (max is 249)
def makePattern(arr):
    level = 1
    while (level < 250):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = "" + str(r) + " " + str(g) + " " + str(b) + " "
        for y in range(level, 500 - level):
            for x in range(level, 500 - level):
                arr[500*(x)+(y)] = color
        #print("here")
        level += 5
    return arr
            
            
                       
makeBack(arr)
makePattern(arr)
file.write(' '.join(arr))

#file.write(“Hello World”)
#file.read()


file.close()
