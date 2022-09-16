import pygame
from pygame.math import Vector2
from math import degrees


class View:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car Simulator")
        screen_size = (1280, 720)
        self.screen = pygame.display.set_mode(screen_size)
        self.car_image = pygame.image.load("car.png")


    # update the scene
    def draw_car(self, x, y , theta):

        # fill screen with gray background
        self.screen.fill((127, 127, 127))

        # draw the car 
        rotated = pygame.transform.rotate(self.car_image, degrees(theta))
        rect = rotated.get_rect()
        offset = (rect.width/2, rect.height/2)
        position = Vector2(x, y)
        self.screen.blit(rotated, position-offset)

        # update the display
        pygame.display.flip()


