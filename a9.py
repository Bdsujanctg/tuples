import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
PLAYER_SIZE = 40
ENEMY_SIZE = 30
MOVE_SPEED = 5
score = 0
font = pygame.font.SysFont(None, 36)
player = pygame.Rect(WIDTH//2, HEIGHT//2, PLAYER_SIZE, PLAYER_SIZE)
enemies = []
for _ in range(7):
    x = random.randint(0, WIDTH - ENEMY_SIZE)
    y = random.randint(0, HEIGHT - ENEMY_SIZE)
    enemy = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += MOVE_SPEED
    if keys[pygame.K_UP]:
        player.y -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        player.y += MOVE_SPEED
    player.x = max(0, min(WIDTH - PLAYER_SIZE, player.x))
    player.y = max(0, min(HEIGHT - PLAYER_SIZE, player.y))
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        if player.colliderect(enemy):
            score+=1
            score 
            enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)
            enemy.y = random.randint(0, HEIGHT - ENEMY_SIZE)
        pygame.draw.rect(screen, RED, enemy)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
