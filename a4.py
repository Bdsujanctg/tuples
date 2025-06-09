import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game Screen")
font = pygame.font.SysFont(None, 40)
text = font.render("My First Game Screen", True, (0, 0, 0))
rect = pygame.Rect(0, 0, 300, 200)
rect.center = (300, 220)
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    text_rect = text.get_rect(center=(300, 80))
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
