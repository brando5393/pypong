import pygame
import random

pygame.init()
pygame.mixer.init()

BALL_HIT_SOUND = pygame.mixer.Sound(
    "./audio/Jump-SoundBible.com-1007297584.mp3")
SMASH_POWERUP_SOUND = pygame.mixer.Sound(
    "./audio/Swooshing-SoundBible.com-1214884243.mp3")
FLASH_POWERUP_SOUND = pygame.mixer.Sound(
    "./audio/Blop-Mark_DiAngelo-79054334.mp3")

# sizes and positions
WINDOW_HEIGHT, WINDOW_WIDTH = 600, 1000
PADDLE_HEIGHT, PADDLE_WIDTH = 120, 20
# ball values
ball_radius = 15
ball_x, ball_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
ball_speed_x, ball_speed_y = 0.7, 0.7
# paddle values
left_paddle_y = right_paddle_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
left_paddle_x = 100 - PADDLE_WIDTH // 2
right_paddle_x = WINDOW_WIDTH - (100 - PADDLE_WIDTH // 2)
right_paddle_speed = left_paddle_speed = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VIOLET = (148, 0, 211)
INDIGO = (75, 0, 130)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)


# initial values
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pyPong")
ball_color = WHITE
paddle_color = WHITE
game_is_running = True
player_1 = player_2 = 0
ball_direction = [0, 1]
ball_angle = [0, 1, 2]

# powerups
left_powerup = right_powerup = 0
# total available powerups
left_powerup_total = right_powerup_total = 5


# main game loop
while game_is_running:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_speed = -0.9
            if event.key == pygame.K_DOWN:
                right_paddle_speed = 0.9
            if event.key == pygame.K_RIGHT and right_powerup_total > 0:
                right_powerup = 1
            if event.key == pygame.K_LEFT and right_powerup_total > 0:
                right_powerup = 2
            if event.key == pygame.K_w:
                left_paddle_speed = -0.9
            if event.key == pygame.K_s:
                left_paddle_speed = 0.9
            if event.key == pygame.K_d and left_powerup_total > 0:
                left_powerup = 1
            if event.key == pygame.K_a and left_powerup_total > 0:
                left_powerup = 2

        if event.type == pygame.KEYUP:
            right_paddle_speed = 0
            left_paddle_speed = 0

    # ball movement conditions
    if ball_y <= 0 + ball_radius or ball_y >= WINDOW_HEIGHT - ball_radius:
        ball_speed_y *= -1
    if ball_x >= WINDOW_WIDTH - ball_radius:
        player_1 += 1
        ball_x, ball_y = WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius
        random_direction = random.choice(ball_direction)
        random_angle = random.choice(ball_angle)
        if random_direction == 0:
            if random_angle == 0:
                ball_speed_y, ball_speed_x = -1.4, 0.7
            if random_angle == 1:
                ball_speed_y, ball_speed_x = -0.7, 0.7
            if random_angle == 2:
                ball_speed_y, ball_speed_x = -0.7, 1.4

        if random_direction == 1:
            if random_angle == 0:
                ball_speed_y, ball_speed_x = 1.4, 0.7
            if random_angle == 1:
                ball_speed_y, ball_speed_x = 0.7, 0.7
            if random_angle == 2:
                ball_speed_y, ball_speed_x = 0.7, 1.4
        ball_speed_x *= -1
    if ball_x <= 0 + ball_radius:
        player_2 += 1
        ball_x, ball_y = WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius
        random_direction = random.choice(ball_direction)
        random_angle = random.choice(ball_angle)
        if random_direction == 0:
            if random_angle == 0:
                ball_speed_y, ball_speed_x = -1.4, 0.7
            if random_angle == 1:
                ball_speed_y, ball_speed_x = -0.7, 0.7
            if random_angle == 2:
                ball_speed_y, ball_speed_x = -0.7, 1.4

        if random_direction == 1:
            if random_angle == 0:
                ball_speed_y, ball_speed_x = 1.4, 0.7
            if random_angle == 1:
                ball_speed_y, ball_speed_x = 0.7, 0.7
            if random_angle == 2:
                ball_speed_y, ball_speed_x = 0.7, 1.4

    # paddle movement controls
    if left_paddle_y >= WINDOW_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= WINDOW_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # collision detection
    if left_paddle_x <= ball_x <= left_paddle_x + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        if left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
            ball_x = left_paddle_x + PADDLE_WIDTH
            ball_speed_x *= -1
            BALL_HIT_SOUND.play()

    if right_paddle_x <= ball_x <= right_paddle_x + PADDLE_WIDTH:
        if right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
            ball_x = right_paddle_x
            ball_speed_x *= -1
            BALL_HIT_SOUND.play()

    # powerups

    # smash left paddle
    if left_powerup == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + PADDLE_WIDTH:
            if left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
                ball_x = left_paddle_x + PADDLE_WIDTH
                SMASH_POWERUP_SOUND.play()
                ball_speed_x *= -3.5
                left_powerup = 0
                left_powerup_total -= 1
    # flash left paddle
    elif left_powerup == 2:
        left_paddle_y = ball_y
        left_powerup = 0
        left_powerup_total -= 1
        FLASH_POWERUP_SOUND.play()

    # smash right paddle
    if right_powerup == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + PADDLE_WIDTH:
            if right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
                ball_x = right_paddle_x
                SMASH_POWERUP_SOUND.play()
                ball_speed_x *= -3.5
                right_powerup = 0
                right_powerup_total -= 1

    # flash right paddle
    elif right_powerup == 2:
        right_paddle_y = ball_y
        right_powerup = 0
        right_powerup_total -= 1
        FLASH_POWERUP_SOUND.play()

    # movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    right_paddle_y += right_paddle_speed
    left_paddle_y += left_paddle_speed

    # scoreboard rendering
    SCOREBOARD_FONT = pygame.font.SysFont("arialblack", 32)
    score_1 = SCOREBOARD_FONT.render(f"Player 1: {player_1}", True, WHITE)
    window.blit(score_1, (25, 25))
    score_2 = SCOREBOARD_FONT.render(f"Player 2: {player_2}", True, WHITE)
    window.blit(score_2, (800, 25))
    total_powerups_player_1 = SCOREBOARD_FONT.render(
        f"Powerups: {left_powerup_total}", True, WHITE)
    window.blit(total_powerups_player_1, (25, 65))
    total_powerups_player_2 = SCOREBOARD_FONT.render(
        f"Powerups: {right_powerup_total}", True, WHITE)
    window.blit(total_powerups_player_2, (770, 65))

    # OBJECTS
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(window, paddle_color, pygame.Rect(
        left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, paddle_color, pygame.Rect(
        right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    if left_powerup == 1:
        pygame.draw.circle(
            window, CYAN, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_powerup == 1:
        pygame.draw.circle(
            window, CYAN, (right_paddle_x + 10, right_paddle_y + 10), 4)
    pygame.display.update()
