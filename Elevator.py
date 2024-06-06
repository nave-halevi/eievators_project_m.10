import pygame
from collections import deque
WHITE = (255, 255, 255)
FLOOR_WIDTH = 133
SOUND_FLIP = "ding.mp3"
pygame.mixer.init()
DING = pygame.mixer.music.load("ding.mp3")

white = (255, 255, 255)
class Elevator:
    def __init__(self, number_elevator):
        self.__number_elevator = number_elevator
        self.__elevator_queue = deque([]) 
        # self.__elevator_position = 0
        pygame.time.Clock()
        self.__elevator_top =1000
        self.current_floor  = 0
   
    def draw_elevator(self, screen):
        elevator_image = pygame.image.load("elv(1)(1)(1).png")
        occupied_pixels = FLOOR_WIDTH + \
            (elevator_image.get_width() * self.__number_elevator)
        y =  self.__elevator_top
        x = occupied_pixels
        rect = elevator_image.get_rect()
        rect.bottomleft = (x, y)
        pygame.draw.rect(screen, WHITE, rect)
        screen.blit(elevator_image, rect)
        self.current_floor  = 0
        return self.__elevator_top
 
    def move_elevator_to_floor(self, floor_y, screen):
        elevator_top = self.__elevator_top 
        if elevator_top != floor_y + 35:
            if elevator_top < floor_y + 35:
                elevator_top +=  1   
            elif elevator_top > floor_y + 35:
                elevator_top -=  1      
            # if elevator_top == floor_y:
            #     pygame.time.wait(2000)  
        self.set_elevator_top(elevator_top)
        if elevator_top == floor_y + 35 :
            print("hallo")
            self.set_elevator_pop_queue()
            # print(self.set_elevator_pop_queue())
        
            # self.draw_elevator()
            # pygame.display.flip()
            
                # DING.play()  
    
        #  pygame.time.get_ticks()
    
    def go_to_floor(self, floor_number):
        self.target_floor = floor_number
        # self.current_floor = floor_number
    
    def get_number(self):
        return self.__number_elevator
    
    def get_last_task(self):
        if self.__elevator_queue:
            return self.__elevator_queue[-1]
        else:
            return None
    
    def set_elevator_queue(self, floor, finish_time):
        self.__elevator_queue.append((floor, finish_time)) 
        print(self.__elevator_queue)

    def get_elevator_number(self):
        return self.__number_elevator
    
    def set_current_floor(self, num_floor):
        self.current_floor = num_floor
 
    def get_elevator_top(self):
        return self.__elevator_top
   
    def set_elevator_pop_queue(self):
        return self.__elevator_queue.popleft()
      
    def get_first_task(self):
        if self.__elevator_queue:
            return self.__elevator_queue[0]
        else:
            return None
   
    def set_elevator_top(self, top):
        self.__elevator_top = top
        
# a = Elevator(1)
# print(a.get_last_task())
# print(a.get_first_task())
 
    
    
    
    
    
    
   