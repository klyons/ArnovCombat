import pdb
import time
import pygame

warrior_S = r'C:\arnavws\ArnovCombat\warrior\Knight_1\Attack 1.png'
wizard_S = r'C:\arnavws\ArnovCombat\wizard\Fire vizard\Attack_1.png'
archer_S = r'C:\arnavws\ArnovCombat\archer\Archer\Attack_1.png'
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Warrior Attack Animation")

# Load sprite sheet
warriorAttack1 = pygame.image.load(warrior_S).convert_alpha()

# Extract frames from the sprite sheet
def extract_frames(sprite_sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

# Animation frames
frame_width = 86
frame_height = 86
num_frames = 5
attack_frames = extract_frames(warriorAttack1, frame_width, frame_height, num_frames)

# Animation variables
frame_index = 0
frame_rate = 10  # Frames per second
animation_timer = 0  # Tracks time between frames
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Update frame index based on frame rate
    animation_timer += clock.get_time()
    if animation_timer >= 1000 // frame_rate:
        animation_timer = 0
        frame_index = (frame_index + 1) % len(attack_frames)

    # Draw current frame
    screen.blit(attack_frames[frame_index], (100, 100))

    # Update display
    pygame.display.flip()

    # Control overall frame rate
    clock.tick(60)

pygame.init()

# Load the sprite sheet
archerAttack1 = pygame.image.load(archer_S).convert_alpha()

def extract_frames(sprite_sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames


# Load sprite sheet
sprite_sheet = pygame.image.load(archer_S)

# Get sheet dimensions
sheet_width, sheet_height = sprite_sheet.get_size()

# Assume fixed number of frames per row
frames_per_row = 4  # Adjust based on your sprite sheet
frames_per_col = 1  # Adjust based on your sprite sheet

frame_width = sheet_width // frames_per_row
frame_height = sheet_height // frames_per_col

print(f"Frame size: {frame_width}x{frame_height}")

num_frames = 4

attack_frames = extract_frames(archerAttack1, frame_width, frame_height, num_frames)

def animate_attack(screen, attack_frames, x, y, frame_rate):
    clock = pygame.time.Clock()
    for frame in attack_frames:
        screen.blit(frame, (x, y))
        pygame.display.flip()
        clock.tick(frame_rate)

screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    animate_attack(screen, attack_frames, 100, 100, 10)

    pygame.display.flip()

pygame.init()

# Load the sprite sheet
wizardAttack1 = pygame.image.load(wizard_S).convert_alpha()

def extract_frames(sprite_sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

frame_width = 64
frame_height = 64
num_frames = 4

attack_frames = extract_frames(wizardAttack1, frame_width, frame_height, num_frames)

def animate_attack(screen, attack_frames, x, y, frame_rate):
    clock = pygame.time.Clock()
    for frame in attack_frames:
        screen.blit(frame, (x, y))
        pygame.display.flip()
        clock.tick(frame_rate)

screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    animate_attack(screen, attack_frames, 100, 100, 10)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

if userClass == "Warrior":
    pygame.image.load('assets/Knight_1')

if userClass == "Wizard":
    pygame.image.load('assets/wizard')

if userClass == "Archer":
    pygame.image.load('assets/archer')
