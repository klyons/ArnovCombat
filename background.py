import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display PNG Image")

# Load the PNG image
image_path = "your_image.png"  # Replace with the path to your PNG file
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
    screen.fill((255, 255, 255))

    # Draw the image on the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()