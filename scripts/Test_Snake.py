#!/usr/bin/env python
import curses
import time
import random
from curses import panel
from collections import deque

curBoard = curses.initscr()
curses.cbreak()
curBoard.keypad(1)
curses.halfdelay(1)
curses.noecho()
curses.curs_set(0)
dimensions = curBoard.getmaxyx()
snake = deque()
fruitC = [40,40] 
random.seed()
def makeBoard():
    #Initializes a deque to hold location of snake dots
    snake.append((32,29))
    snake.append((32,30))
    snake.append((32,31))
    snake.append((32,32))
    #Graphically shows the fruits and the snake
    curBoard.addstr(fruitC[0],fruitC[1],'@')
    for x in range(4):
        curBoard.addstr(32,32-x,'O')
            
def main():
    makeBoard()
    curBoard.border(0)
    curBoard.refresh()
    #direction is direction to move, 1 is right, 2 is up, 3 is left, 4 is down
    direction=1
    while True:
        #Gets keyboard entries and refreshes screen
        face = curBoard.getch()
        #Reads in the key press and decides which direction to start moving in, cannot move in opp. direction
        if face==ord('a'):
            if direction==2 or direction==4:
                direction=3
        elif face==ord('s'):
            if direction==1 or direction==3:
                direction=2
        elif face==ord('w'):
            if direction==1 or direction==3:
                direction=4
        elif face==ord('d'):
            if direction==2 or direction==4:
                direction=1
        elif face==ord('q'):
            curses.endwin()
            break
        #Looks at head location to figure out where to move to next
        head = snake.pop()
        snake.append(head)
        if direction==1:
            newHead=(head[0],head[1]+1)
        elif direction==2:
            newHead=(head[0]+1,head[1])
        elif direction==3:
            newHead=(head[0],head[1]-1)
        elif direction==4:
            newHead=(head[0]-1,head[1])
        #Figures out if head has hit a lose case(border or hit itself)
        if newHead[0]==0 or newHead[0]==dimensions[0] or newHead[1]==0 or newHead[1]==dimensions[1] or curBoard.instr(newHead[0],newHead[1],1)=='O':
            print "You Lose!"
            time.sleep(5)
            curses.endwin()
            break
        #Checks if location is a "fruit" or not, if it is spawns a new fruit, does not delete tail
        if curBoard.instr(newHead[0],newHead[1],1)=='@':
            fruitC=[random.randint(0,dimensions[0]),random.randint(0,dimensions[1])]
            curBoard.addstr(fruitC[0],fruitC[1],'@')
        else:
            #If a fruit has not eaten, the tail dot is removed
            remove = snake.popleft()
            curBoard.addstr(remove[0],remove[1], ' ')
        #Either way, a new head is appended
        curBoard.addstr(newHead[0],newHead[1],'O')
        snake.append(newHead);
        time.sleep(0.1)
    
main()
curses.endwin()
