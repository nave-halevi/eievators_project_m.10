import pygame
from pygame import mixer
BLACK = (0, 0, 0)
LIGHT_BLUE = (0, 255, 255)
LINE_BLACK_HEIGHT = 7
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FLOOR_IMAGE_PATH = "WhatsApp Image 2024-05-29 at 15.20.54.jpeg"
BUTTON = (0, 0, 30, 25)
FONT = (0, 0, 26, 21)
LINE_BLACK_WIDTH = 133
TEXT_SIZE = 30
TIMER_RECT_X = 900
TIMER_RECT_HEIGHT = 30
TIMER_RECT_WIDTH = 30
SOUND_FILE = "ding.mp3"
class Floor:
    def __init__(self, floors_number):
        self.__floors_number = floors_number
        self.button_rect = pygame.Rect(BUTTON)
        self.button_color = LIGHT_BLUE
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
        self.__floor_y = 0
    def draw_black_line(self, x, y, screen):
        line_black = pygame.Rect(x, y - LINE_BLACK_HEIGHT, LINE_BLACK_WIDTH, LINE_BLACK_HEIGHT)
        pygame.draw.rect(screen, BLACK, line_black)

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.button_color, self.button_rect)
        button_center = self.button_rect.center
        font = pygame.font.Font(None, TEXT_SIZE)
        text_surface = font.render(str(self.__floors_number), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = button_center
        screen.blit(text_surface, text_rect)

    def timer(self, y, screen):
        rect_timer = pygame.Rect(TIMER_RECT_X, y - self.image.get_height(), TIMER_RECT_HEIGHT, TIMER_RECT_WIDTH)
        pygame.draw.rect(screen, RED, rect_timer)

    def draw_floor(self, screen):
        occupied_pixels = self.image.get_height() * self.__floors_number
        x = 0
        y = screen.get_height() - occupied_pixels
        rect = self.image.get_rect()
        rect.bottomleft = (x, y)
        pygame.draw.rect(screen, LIGHT_BLUE, rect)
        screen.blit(self.image, rect)
        self.__floor_y = rect.topleft[1]
        if self.__floors_number > 0:  
            self.draw_black_line(x, y, screen)
        self.button_rect = pygame.Rect(BUTTON)
        self.button_rect.center = rect.center
        self.draw_button(screen)
        self.timer(y, screen)

    def button_clicked(self, screen, mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            self.button_color = GREEN 
            self.draw_button(screen)
            pygame.display.flip()
        return True 
    # def elevator_came(self, screen, __floors_number):
    #     if 
    #         self.button_color = RED
    #         self.draw_button(screen)
    #         pygame.display.flip()
   
    def get_floors_number(self):
        return self.__floors_number
   
    def get_floor_y(self):
        return  self.__floor_y 