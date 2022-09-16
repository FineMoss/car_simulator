import pygame
from pygame.math import Vector2


class Control:

    def __init__(self, sim, view):
        
        # initialize the simulator
        self.sim = sim
        self.sim.wheelbase = 10
        self.sim.x = 640
        self.sim.y = 360
       
        # updated through W,A,S,D keys
        # used by the simulator
        self.wheel_angle = 0
        self.acceleration = 0

        # create reference to the view
        self.view = view


    # event handler for the game
    def process_events(self):

        self.acceleration = 0
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.acceleration += 10
                if event.key == pygame.K_a:
                    self.wheel_angle += 0.1
                if event.key == pygame.K_s:
                    self.acceleration -= 10
                if event.key == pygame.K_d:
                    self.wheel_angle -= 0.1
                if event.key == pygame.K_ESCAPE:
                    self.done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sim.x = event.pos[0]
                self.sim.y = event.pos[1]
                self.sim.v = 0
                self.sim.theta = 0
                self.wheel_angle = 0


    def run(self):
        
        # start the game clock
        clock = pygame.time.Clock()
        
        # 40 ticks per second
        tick_rate = 40

        # time in seconds for each frame
        dt = 10/tick_rate

        self.done = False
        while not self.done:

            # process key inputs and app closure events
            # and update data for the simulator
            self.process_events()

            # update the simulator by 1 epoch
            self.sim.simulatorStep(self.acceleration, self.wheel_angle, dt)

            # update the view with the new data model
            self.view.draw_car(self.sim.x, self.sim.y, self.sim.theta)
            
            # wait for next frame
            clock.tick(tick_rate)

        pygame.quit()



