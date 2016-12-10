"""Press n to turn on branch numbers
Press l to turn on leaves
Press up to increase the number of branches
Press down to decrease the number of branches
Hold the mouse to make the tree sway"""

import sys
import random
import math

def setup():
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())
    
def drawLineAngle(color, start, angle, length, width):
    angle += 180
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0], location[1], 10, 10)

def drawNum(location):
    stroke(0, 50, 0)
    fill(100, 255, 100)
    strokeWeight(0.5)
    ellipse(location[0], location[1], 25, 25)
    fill(0, 0, 0)
    textAlign(CENTER)
    text(str(countnum), location[0], location[1])
    
    
def drawTree(start, leaf, depth, angle, w, count, l):
    global constant
    end = drawLineAngle([0, 0, 0], start, angle, l, w)
    if depth == 0:
        if leaf:
            drawLeaf(end)
    else:
        drawTree(end, leaf, depth - 1, angle - count * constant, w * 0.65, count * 0.9, l * 0.9)
        drawTree(end, leaf, depth - 1, angle + count / constant, w * 0.65, count * 0.9, l * 0.9)
    global countnum
    countnum -= 1
    if num:
        drawNum(end)
        
def sway():
    global constant
    global bool
    if bool:
        constant += 0.0025
        if constant >= 1.15:
            bool = not bool
    else:
        constant -= 0.0025
        if constant <= 0.86956:
            bool = not bool
        
def keyPressed():
    global leaf
    if key == "l":
        leaf = not leaf
    global num
    if key == "n":
        num = not num
    global branches
    if keyCode == UP:
        branches += 1
        draw()
    if keyCode == DOWN:
        if branches > 0:
            branches -= 1
        draw()
        
def setup():
    global leaf
    leaf = False
    global num
    num = False
    global branches
    branches = 7
    global constant
    constant = 1
    global bool
    bool = True
    global col
    col = [0, 0, 0]
    
def draw():
    clear()
    if mousePressed:
        sway()
    global branches
    global countnum
    countnum = 2 * (2 ** branches) - 1
    background(255)
    drawTree((550, 800), leaf, branches, 0, 25, 30, 100)
        