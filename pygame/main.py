# import all packages needed
import pygame
import os
import random

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constant variables
WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED_OVERLAY = (255, 0, 0, 150)
GREEN_OVERLAY = (0, 255, 0, 150)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
ENEMY_VEL = 2
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
RED_OVERLAY_DURATION = 15
GREEN_OVERLAY_DURATION = 35

# Load assets
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
BACKGROUND_IMAGE = pygame.image.load(os.path.join("Assets", "game background.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90
)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270
)
# Sound effecs
BULLET_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'bullet sfx.mp3'))
MISSED_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'miss sfx.mp3'))  
LEVELUP_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'level up sfx.mp3'))  
SHOT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'scored sfx.mp3'))  

# Helvetica font for score
FONT = pygame.font.SysFont("helvetica", 15)

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        self.vel = ENEMY_VEL

    def update(self):
        self.rect.x -= self.vel

    def draw(self, window):
        window.blit(RED_SPACESHIP, (self.rect.x, self.rect.y))

    def is_off_screen(self):
        return self.rect.x < -SPACESHIP_WIDTH

def draw_window(yellow, yellow_bullets, enemies, score, defeat, red_overlay_timer, green_overlay_timer):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for enemy in enemies:
        enemy.draw(WIN)
    score_text = FONT.render(f"Points: {score}/10", True, (255, 255, 255))
    defeat_text = FONT.render(f"Miss: {defeat}", True, (255, 255, 255))
    WIN.blit(score_text, (10, 10))
    WIN.blit(defeat_text, (10, 40))
    # initializing color overlays
    if red_overlay_timer > 0:
        red_overlay_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        red_overlay_surface.fill(RED_OVERLAY)
        WIN.blit(red_overlay_surface, (0, 0))
    if green_overlay_timer > 0:
        green_overlay_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        green_overlay_surface.fill(GREEN_OVERLAY)
        WIN.blit(green_overlay_surface, (0, 0))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VEL + yellow.width < WIDTH:
        yellow.x += VEL
    if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT:
        yellow.y += VEL

def handle_bullets(yellow_bullets, enemies):
    score = 0
    for bullet in yellow_bullets[:]:
        bullet.x += BULLET_VEL
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            continue
        for enemy in enemies[:]:
            if bullet.colliderect(enemy.rect):
                yellow_bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                SHOT_SOUND.play()
                break
    return score

def main():
    global VEL, BULLET_VEL, ENEMY_VEL
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    enemies = []
    score = 0
    defeat = 0
    red_overlay_timer = 0
    green_overlay_timer = 0
    enemy_spawn_timer = 0
    enemy_spawn_delay = 120
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_SOUND.play() 
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= enemy_spawn_delay:
            new_enemy = Enemy(WIDTH, random.randint(50, HEIGHT - SPACESHIP_HEIGHT - 50))
            enemies.append(new_enemy)
            enemy_spawn_timer = 0
        for enemy in enemies[:]:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)
                defeat += 1
                MISSED_SOUND.play()
                red_overlay_timer = RED_OVERLAY_DURATION
        if red_overlay_timer > 0:
            red_overlay_timer -= 1
        if green_overlay_timer > 0:
            green_overlay_timer -= 1
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        score += handle_bullets(yellow_bullets, enemies)
        if score >= 10:
            VEL += 1
            BULLET_VEL += 1
            ENEMY_VEL += 1
            score = 0
            green_overlay_timer = GREEN_OVERLAY_DURATION
            LEVELUP_SOUND.play()
        draw_window(yellow, yellow_bullets, enemies, score, defeat, red_overlay_timer, green_overlay_timer)
    pygame.quit()

if __name__ == "__main__":
    main()
