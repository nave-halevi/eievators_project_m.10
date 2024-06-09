import pygame
from Floor import Floor
from Elevator import Elevator

class Building():
    def __init__(self,floor_number, elevator_number):
        self.__floors = []
        self.__elevators = []
        self.__floor_number = floor_number
        self.__elevator_number = elevator_number

 
    def building(self, screen):
        for i in range(self.__floor_number):
            self.__floors.append(Floor(i))
            self.__floors[i].draw_floor(screen)
            pygame.display.flip()
        for j in range(self.__elevator_number):
           self.__elevators.append(Elevator(j))
           self.__elevators[j].draw_elevator(screen) 
           pygame.display.flip() 
    
    
    def please_elevator(self, floor_number):
        opt_elevator, _  = self.move_nearest_elevator_to_floor(floor_number)
        if opt_elevator:
            opt_elevator.set_elevator_queue(floor_number, _ ) 
          
            
    def move_nearest_elevator_to_floor(self, floor_number):
        nearest_elevator = None
        min_distance = float('inf')
        last_timer = 0
        last_floor = 0 
        for elevator in self.__elevators:
            last_task = elevator.get_last_task()
            
            if last_task:
                last_floor = last_task[0] 
                last_timer = last_task[1]
            else :
                last_floor, last_timer = elevator.current_floor, 0
            distance = abs(last_floor - floor_number / 2) + last_timer
            if distance < min_distance:
                min_distance = distance
                nearest_elevator = elevator  
        if nearest_elevator:
            nearest_elevator.go_to_floor(floor_number)
        return nearest_elevator, distance 
   
   
    def get_self__floors(self): 
         return  self.__floors      


    def get_elevators(self):
        return self.__elevators
    
    
    def move_all_elevators(self, screen):
        for elevator in self.__elevators:
            if elevator.get_first_task() is not None:
                floor_num = elevator.get_first_task()[0]
                floor = self.__floors[floor_num] 
                floor_y = floor.get_floor_y()
                floor_number  = elevator.move_elevator_to_floor(floor_y, floor)
                if floor_number :
                    floor_finish =  self.__floors[floor_num] 
                    floor_finish.elevator_came(screen)                    
                pygame.display.flip()   

    # def timer(self):
    #    pygame.time.get_ticks()
    # pass
                
                