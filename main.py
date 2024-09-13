import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Square")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the player square
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height // 2 - player_size // 2
player_speed = 3


# Define square properties
square_size = 30
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2
square_speed = 2

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep the player within the screen bounds
    player_x = max(0, min(player_x, width - player_size))
    player_y = max(0, min(player_y, height - player_size))



    # Define button properties
    button_size = 50
    button_colors = [(0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 0, 255)]
    button_pressed_colors = [(0, 200, 0), (200, 200, 0), (0, 0, 200), (200, 0, 200)]
    buttons = []
    # Define button positions
    button_positions = [
        (width // 2, height // 2 - button_size * 1.25),  # Up
        (width // 2, height // 2 + button_size * 1.25),  # Down
        (width // 2 - button_size * 1.25, height // 2),  # Left
        (width // 2 + button_size * 1.25, height // 2)   # Right
    ]

    for i, position in enumerate(button_positions):
        button_x, button_y = position
        buttons.append({
            'rect': pygame.Rect(button_x - button_size // 2, button_y - button_size // 2, button_size, button_size),
            'color': button_colors[i],
            'pressed_color': button_pressed_colors[i],
            'current_color': button_colors[i]
        })

    # Check if player is touching any button
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    
    for button in buttons:
        if player_rect.colliderect(button['rect']):
            button['current_color'] = button['pressed_color']
        else:
            button['current_color'] = button['color']




    # Move the square based on button presses
    for i, button in enumerate(buttons):
        if player_rect.colliderect(button['rect']):
            if i == 0:  # Up
                square_y -= square_speed
            elif i == 1:  # Down
                square_y += square_speed
            elif i == 2:  # Left
                square_x -= square_speed
            elif i == 3:  # Right
                square_x += square_speed

    # Keep the square within the screen bounds
    square_x = max(0, min(square_x, width - square_size))
    square_y = max(0, min(square_y, height - square_size))





    # Clear the screen
    screen.fill(BLACK)


    # Draw the buttons
    for button in buttons:
        pygame.draw.rect(screen, button['current_color'], button['rect'])


    # Draw the square
    pygame.draw.rect(screen, (255, 165, 0), (square_x, square_y, square_size, square_size))


    # Draw the player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
