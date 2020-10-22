##############################
# Snake / Roque / 2020-10-20 #
##############################

import os
import keyboard
import time
import math

# Level Constants
EMPTY_CELL = ' '        # Char of the empty space
H_WALL = '═'            # Char of the top/bottom wall
V_WALL = '║'            # Char of the sides wall
TOP_LEFT_CORNER = '╔'   # Char of the top left corner wall
TOP_RIGHT_CORNER = '╗'  # Char of the top right corner wall
BOT_LEFT_CORNER = '╚'   # Char of the bottom left corner wall
BOT_RIGHT_CORNER = '╝'  # Char of the bottom right corner wall
HEIGHT = 20             # Level HEIGHT
WIDTH = 80              # Level WIDTH

# Game Constants
SNAKE_BODY = '█'   # Char of the body of the snake
SNAKE_HEAD = '▓'   # Char of the head of the snake
POINT = '■'        # Char of the snake food
SPEED = 1          # Game speed (time in seconds between each refresh)

# Movement
direction = 'RIGHT' # Direction which the snake is headed to
snake_pos = {
  'x' : 0,         # X position of the snake
  'y' : 0          # Y position of the snake
}

level = []

def generateLevel(x, y):
  global level, snake_pos
  level = []
  # row = []
  # for i in range(x):
  #   row.append(EMPTY_CELL)

  # for i in range(y):
  #   level.append(row)

  level = [[ EMPTY_CELL for i in range(x) ] for j in range(y) ]

  snake_pos['x'] = math.ceil(y / 2)
  snake_pos['y'] = math.ceil(x / 2)

  level[snake_pos['x']][snake_pos['y']] = SNAKE_BODY


def drawLevel():
  global level, snake_pos, WIDTH, HEIGHT
  print(f'WIDTH: {WIDTH}\nHEIGHT: {HEIGHT}')
  for i in range(HEIGHT + 2):
    row = ''
    for j in range(WIDTH + 2):

      # Draws the left wall
      if j == 0:
        if i != 0 and i != HEIGHT + 1:
          row += V_WALL
        elif i == 0:
          row += TOP_LEFT_CORNER
        else:
          row += BOT_LEFT_CORNER
      
      # Draws the right wall
      elif j == WIDTH + 1:
        if i != 0 and i != HEIGHT + 1:
          row += V_WALL
        elif i == 0:
          row += TOP_RIGHT_CORNER
        else:
          row += BOT_RIGHT_CORNER
      
      # Draws the up and bottom walls
      elif i == 0 or i == HEIGHT + 1:
        row += H_WALL

      else:
        # if level[i-1][j-1] == SNAKE_BODY:
        #   row += SNAKE_BODY
        if snake_pos['x'] == i-1 and snake_pos['y'] == j-1:
          row += SNAKE_BODY
        else:
          row += EMPTY_CELL

    print(row)


def assignDirection(d):
  global direction
  direction = d

keyboard.on_press_key('up', lambda _:assignDirection('UP'))
keyboard.on_press_key('left', lambda _:assignDirection('LEFT'))
keyboard.on_press_key('down', lambda _:assignDirection('DOWN'))
keyboard.on_press_key('right', lambda _:assignDirection('RIGHT'))

def move():
  global level, direction, snake_pos

  if direction == 'LEFT':
    snake_pos['y'] -= 1
  elif direction == 'RIGHT':
    snake_pos['y'] += 1

  elif direction == 'UP':
    snake_pos['x'] -= 1
  else:
    snake_pos['x'] += 1

def main():
  global level, WIDTH, HEIGHT
  generateLevel(WIDTH, HEIGHT)

  while True:
    os.system('cls')
    move()
    drawLevel()
    time.sleep(SPEED)


main()