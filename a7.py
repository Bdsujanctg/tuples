import pygame
import random
screen_width, screen_height = 500, 400
move_speed = 5
font_size = 72
pygame.init()
background_image = pygame.transform.scale(pygame.image.load('bg.jpg'), (screen_width, screen_height))
font = pygame.font.SysFont('Times New Roman', font_size)
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000) 
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.update_color(color)
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
    def update_color(self, new_color):
        self.color = new_color
        self.image.fill(pygame.Color('dodgerblue'))  # optional border/background
        pygame.draw.rect(self.image, new_color, pygame.Rect(0, 0, self.width, self.height))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Collision')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('Red'), 20, 30)
sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, screen_height - sprite1.rect.height)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color('Black'), 20, 30)
sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)
all_sprites.add(sprite2)
running, won = True, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            new_color1 = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_color2 = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            sprite1.update_color(new_color1)
            sprite2.update_color(new_color2)

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * move_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * move_speed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render('You Win!', True, pygame.Color('Black'))
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2, (screen_height - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
