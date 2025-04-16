import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display PNG Image")

#background = pygame.image.load("background.jpg") 

# Scale the image to fit the window (optional)
#background = pygame.transform.scale(background, (screen_width, screen_height))
background = pygame.image.load(r"C:\Users\17079\Desktop\Family docs\Arnav games\Arnav-Combat\Arnav Code\mwerty.jpg").convert()

# Load the PNG image
image_path = r"C:\Users\17079\Desktop\Family docs\Arnav games\Arnav-Combat\Arnav Code\mwerty.jpg"



try:
    image = pygame.image.load(image_path)
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
    sys.exit()
# Get the image's dimensions
image_rect = image.get_rect()

# Center the image on the screen
image_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen (fill with white)
    screen.fill((254, 254, 0))

    # Draw the image on the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()