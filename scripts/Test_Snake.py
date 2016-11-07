#!/usr/bin/env python
import curses
import time
from curses import panel
from collections import deque

curBoard = curses.initscr()
curses.cbreak()
curBoard.keypad(1)
curses.halfdelay(1)
curses.noecho()
#head is the location of the moving block
snake = deque()
snake.append((32,32))
bHeight = 40
bWidth = 40
board = [[" " for x in range(bWidth)] for y in range(bHeight)]
for row in range(bHeight):
    for column in range(bWidth):
        if row ==0 or column==0 or row==39 or column==39:
            board[row][column] = "*"
        else:
            board[row][column] = " "
            
def makeBoard():
    for row in range(bHeight):
        for column in range(bWidth):
            curBoard.addstr(row, column, board[row][column])
            curBoard.refresh()
            #print board[row][column],
def main():
    #makeBoard()
    curBoard.border(0)
    curBoard.refresh()
    #direction is direction to move, 1 is right, 2 is up, 3 is left, 4 is down
    direction=1
    while True:
        face = curBoard.getch()
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
        curBoard.addstr(newHead[0],newHead[1],'O')
        snake.append(newHead);
        remove = snake.popleft()
        curBoard.addstr(remove[0],remove[1], ' ')
        time.sleep(0.1)
    
main()
curses.endwin()
