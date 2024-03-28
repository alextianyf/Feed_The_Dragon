import pygame

#initialize pygame
pygame.init()

#Create a display surface 
WINDOW_WIDTH = 600
WIDWOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WIDWOW_HEIGHT))

#Set its caption
pygame.display.set_caption("Feed The Dragon")

running = True
while running:
    #Loop through a list of event objects that have occured
    for evnt in pygame.event.get():
        print(evnt)
        if evnt.type == pygame.QUIT:
            running = False

pygame.quit()
