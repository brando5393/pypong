import pygame

pygame.init()

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
MAGENTA = (255, 0, 255)
TEAL = (0, 128, 128)
LIGHT_CORAL = (240, 128, 128)
DARK_ORANGE = (255, 140, 0)
CORN_FLOWER_BLUE = (100, 149, 237)
DOGER_BLUE = (123, 104, 238)
ROYAL_BLUE = (65, 105, 225)
BLUE_VIOLET = (138, 43, 226)
DARK_MAGENTA = (139, 0, 139)
DARK_VIOLET = (148, 0, 211)
DEEP_PINK = (255, 20, 147)
LAVENDER = (230, 230, 250)
MINT_CREAM = (245, 255, 250)

# Create the screen
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("pyPong")
ball_color = WHITE
paddle_color = WHITE
game_is_running = True

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
            if event.key == pygame.K_w:
                left_paddle_speed = -0.9
            if event.key == pygame.K_s:
                left_paddle_speed = 0.9

        if event.type == pygame.KEYUP:
            right_paddle_speed = 0
            left_paddle_speed = 0

    # ball movement conditions
    if ball_y <= 0 + ball_radius or ball_y >= WINDOW_HEIGHT - ball_radius:
        ball_speed_y *= -1
    if ball_x >= WINDOW_WIDTH - ball_radius:
        ball_x, ball_y = WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius
        ball_speed_x *= -1
        ball_speed_y *= -1
    if ball_x <= 0 + ball_radius:
        ball_x, ball_y = WINDOW_WIDTH // 2 - ball_radius, WINDOW_HEIGHT // 2 - ball_radius
        ball_speed_x, ball_speed_y = 0.7, 0.7
    # movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    right_paddle_y += right_paddle_speed
    left_paddle_y += left_paddle_speed

    # paddle movement controls
    if left_paddle_y >= WINDOW_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= WINDOW_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = WINDOW_HEIGHT - PADDLE_HEIGHT
    if right_paddle_y <= 0:
        right_paddle_y = 0
    # OBJECTS
    pygame.draw.circle(window, ball_color, (ball_x, ball_y), ball_radius)
    pygame.draw.rect(window, paddle_color, pygame.Rect(
        left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, paddle_color, pygame.Rect(
        right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()
