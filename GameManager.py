import pygame
import sys
pygame.init()
screen_width = 1000
screen_height =1000
screen = pygame.display.set_mode((screen_width, screen_height)) 
wight = (255, 255, 255)
red = (255, 0, 0)
# pygame.display.set_caption()  
# image = pygame.image.load("elv.png")
# image_rect = image.get_rect()
# x ,y = screen_width // 2 -image.get.screen_width, screen_height // 2 -image_rect.screen_height
run =True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    screen.fill(red)
    pygame.display.flip()
    # screen.blit(image, (x, y))
    # pygame.display.flip()  
pygame.quit() 
sys.exit()


# pygame.draw.rect()
# pygame.key.get_pressed()
# pygame.mixer.Sound()
# pygame.time.Clock()
# pygame.font.Font()
# pygame.



   
   
















# pygame.display.set_caption()  








































































































































