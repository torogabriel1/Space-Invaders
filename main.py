import pygame
import os
import time
import random
pygame.font.init()

Width, Height = 750, 750
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Space Invaders")

# Load images
Red_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
Green_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
Blue_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#Player ship
Yellow_Space_Ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
Red_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
Green_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
Blue_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
Yellow_Laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
Background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (Width, Height))

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("TimesNewRoman", 50)
    clock = pygame.time.Clock()

    def redraw_window():
        Window.blit(Background (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        Window.blit(lives_label, (10, 10))
        Window.blit(level_label, (Width - level_label.get_width() - 10, 10))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()