import pygame


 
class Floor:
    def __init_(self, floors_number):
        self.floors_number = floors_number
        self.current.floor = 0
        self.time.clock = 0
        self.button = False
        self.red = (255, 0, 0)
        self.green = (0, 0, 0)
        self.color_button = self.red                                                        
        self.sound = ("")
        self.image = pygame.display.set_caption() 
    
    def color_button(self, color_button, button):
        sound_file_path = "path/to/your/sound/file.mp3"
        if  self.button == True : 
            color_button = self.green
            self.play_sound(sound_file_path)
    def play_sound(sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    sound_file_path = "path/to/your/sound/file.mp3"
    play_sound(sound_file_path)
   
    def timer(number_elevator, floors_number):
        distance = abs(number_elevator -  floors_number)
        timer = distance 

    def 















