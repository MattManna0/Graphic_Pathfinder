import pygame
import Pathfinder
from Pathfinder import row_length
from Pathfinder import column_height

pygame.init()

screen = pygame.display.set_mode((700, 700))

white = [255, 255, 255]

cheese = pygame.image.load(r'C:\Users\Mthew\Java\Pathfinders\Cheese.jpg')
cheese_small = pygame.transform.rotozoom(cheese, .09, .09)

mouse_trap = pygame.image.load(r'C:\Users\Mthew\Java\Pathfinders\New_Mousetrap.PNG')
mouse_trap_small = pygame.transform.rotozoom(mouse_trap, .30, .30)

cheese_spacing_x = 700 / row_length
cheese_spacing_y = 700 / column_height

ev = pygame.event.get()


x_coord = 0
y_coord = 0
index = 0

first_run = True

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if first_run:
        screen.fill(white)
        first_run = False

    pygame.display.set_caption("Pathfinder Algorithm")

    if index == 0:
        for cheese_1 in range(column_height):
            # print(y_coord, x_coord)
            for cheeses_2 in range(row_length):
                screen.blit(cheese_small, (x_coord, y_coord))
                x_coord += cheese_spacing_x
                pygame.display.update()
            x_coord = 0
            y_coord += cheese_spacing_y

    index = 1

    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            if pygame.mouse_position.color() == white:
                print("6")

    pygame.display.update()
