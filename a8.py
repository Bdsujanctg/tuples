import pygame
pygame.init()
screen_width, screen_height = 500, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Two Rectangular Sprites")
move_speed = 5
background_color = pygame.Color('lightblue')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(0, min(self.rect.x + x_change, screen_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y + y_change, screen_height - self.rect.height))
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('red'), 50, 30)
sprite1.rect.topleft = (100, 100)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color('black'), 50, 30) 
sprite2.rect.topleft = (300, 200)
all_sprites.add(sprite2)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * move_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * move_speed
    sprite1.move(x_change, y_change)
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
