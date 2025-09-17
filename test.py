import pygame
import sys

from pygame.examples.music_drop_fade import starting_pos

pygame.init()

screen = pygame.display.set_mode((500, 500))

###SNAKE Settings###
snake_direction = "Left"
snake_speed = 1
snake_length = 1

###SNAKE BODY###
head = pygame.Surface((20, 20))
head.fill((44, 44, 44))
start_position_head = (0,0)
current_position_head = (0,0)

###Snake def###

def Move_Snake(Direction, speed, Position):
    global current_position_head
    if Direction == "Left":
        current_position_head = (Position[0] - speed, Position[1])
    if Direction == "Right":
        current_position_head = (Position[0] + speed, Position[1])
    if Direction == "Up":
        current_position_head = (Position[0], Position[1] - speed)
    if Direction == "Down":
        current_position_head = (Position[0], Position[1] + speed)


while True:

    screen.blit(head, current_position_head)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                snake_direction = "Up"
            if keys[pygame.K_s]:
                snake_direction = "Down"
            if keys[pygame.K_a]:
                snake_direction = "Left"
            if keys[pygame.K_d]:
                snake_direction = "Right"

    Move_Snake(snake_direction, snake_speed, current_position_head)





