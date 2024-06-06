import pygame
from Floor import Floor
from Elevator import Elevator
from Building import Building
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
white = (255, 255, 255)
red = (255, 0, 0)
screen.fill(white)
building = Building(10, 4)
pygame.display.flip()
floor = Floor(0)
building.building(screen)

run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for floor in building.get_self__floors():
                    floor.button_clicked(screen, mouse_pos) 
                    if floor.button_rect.collidepoint(mouse_pos):
                        floor_number = floor.get_floors_number()
                        building.please_elevator(floor_number) 
    building.move_all_elevators(screen) 
    for elevator in building.get_elevators():
         elevator.draw_elevator(screen)  
    for floor in building.get_self__floors():
        floor.draw_floor(screen)     
    pygame.display.flip()
    pygame.time.Clock().tick(60)              
pygame.quit()

    
   