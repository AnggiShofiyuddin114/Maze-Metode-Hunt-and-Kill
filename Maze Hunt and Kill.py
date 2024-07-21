import pygame
WIDTH = 600
HEIGHT = 600

FPS = 100

BGCOLOR = (255, 255, 0)

SQUARE_SIZE = 40
THICKNESS = 2
import random

x=0
y=0

def drawMaze(maze, surface, square_size, thickness, current):

    pygame.draw.rect(surface,
            (255, 0, 0), 
            (current[1] * square_size,
            current[0] * square_size,
            square_size,
            square_size),    
        )
    for i, line in enumerate(maze):
        for j, element in enumerate(line):
            if 'l' in element:
                pygame.draw.line(surface,
                    (1 , 0, 0),
                    (j * square_size, i * square_size),
                    (j * square_size, i * square_size + square_size),
                    thickness
                )

            if 'u' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),
                    (j * square_size, i * square_size),
                    (j * square_size + square_size, i * square_size),
                    thickness
                )

            if 'r' in element:
                pygame.draw.line(surface,
                    (0 , 0, 0),
                    (j * square_size + square_size, i * square_size),
                    (j * square_size + square_size, i * square_size + square_size),
                    thickness
                )

            if 'd' in element:
                pygame.draw.line(surface,
                    (1 , 1, 1),
                    (j * square_size, i * square_size + square_size),
                    (j * square_size + square_size, i * square_size + square_size),
                    thickness
                )

def nextMove(current, maze, unvisited, visited,x,y, surface,square_size):
    
    neighbours = []

    if current[0] + 1 < len(maze) and (current[0] + 1, current[1]) in unvisited:
        neighbours.append((current[0] + 1, current[1]))

    if current[1] + 1 < len(maze) and (current[0], current[1] + 1) in unvisited:
        neighbours.append((current[0], current[1] + 1))

    if current[0] - 1 >= 0 and (current[0] - 1, current[1]) in unvisited:
        neighbours.append((current[0] - 1, current[1]))

    if current[1] - 1 >= 0 and (current[0], current[1] - 1) in unvisited:
        neighbours.append((current[0], current[1] - 1))

    if len(neighbours) > 0:

        nextPos = random.choice(neighbours)

        if current[0] == nextPos[0]:
            if nextPos[1] > current[1]:
                direction = 'r'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('r', '')
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('l', '') 

            else:
                direction = 'l'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('l', '')
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('r', '')

        else:
            if nextPos[0] > current[0]:
                direction = 'd'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('d', '')
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('u', '')

            else:
                direction = 'u'
                maze[current[0]][current[1]] = maze[current[0]][current[1]].replace('u', '')
                maze[nextPos[0]][nextPos[1]] = maze[nextPos[0]][nextPos[1]].replace('d', '')

        current = nextPos
        if current not in visited:
            visited.append(current)

        if current in unvisited:
            unvisited.remove(current)
    else:
        scan=(x,y)
        pygame.draw.rect(surface,
            (255, 0, 0), 
            (scan[1] * square_size+6,
            scan[0] * square_size+6,
            square_size-10,
            square_size-10),    
        )
        bScan=False
        if scan in unvisited:
            if(y-1>0 and (x,y-1) in visited):
                y=y-1
                current=(x,y)
                bScan=True
            elif(x-1>0 and (x-1,y) in visited):
                x=x-1
                current=(x,y)
                bScan=True
            elif(y+1>0 and (x,y+1) in visited):
                y=y+1
                current=(x,y)
                bScan=True
            elif(x+1>0 and (x+1,y) in visited):
                x=x+1
                current=(x,y)
                bScan=True
        if not bScan:
            if(y+1<len(maze)):
                y=y+1
            else:
                x=x+1
                y=0
        if bScan:
            x=0
            y=0

    return maze, current, visited, unvisited,x,y


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

squares_side = WIDTH // SQUARE_SIZE
print(squares_side)

maze = [['lurd' for i in range(squares_side)] for j in range(squares_side)]

current = (0,0) 

unvisited = [(i, j) for i in range(squares_side) for j in range(squares_side)]
unvisited.remove(current)

visited = [current]

finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()

    screen.fill(BGCOLOR)
    drawMaze(maze, screen, SQUARE_SIZE, THICKNESS, current)

    maze, current, visited, unvisited,x,y = nextMove(current, maze, unvisited, visited,x,y,screen,SQUARE_SIZE)

    pygame.display.flip()

pygame.quit()
