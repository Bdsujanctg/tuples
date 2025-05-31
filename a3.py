import pygame
import sys
pygame.init()
screen_width = 500
screen_height = 500
screen_color = (30, 30, 30) 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game!")
try:
    image = pygame.image.load("smiling.jpg") 
except pygame.error as e:
    print("Unable to load image:", e)
    pygame.quit()
    sys.exit()
image_rect = image.get_rect()
image_rect.center = (300, 300)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(screen_color)       
    screen.blit(image, image_rect)  
    pygame.display.flip()       
pygame.quit()
