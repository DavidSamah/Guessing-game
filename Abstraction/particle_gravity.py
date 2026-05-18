import pygame
import random
import math
import numpy as np

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle gravity accelerator")

clock = pygame.time.Clock()

PEACH = (255, 229, 180)
BLUE = (0, 0, 255)
WHITE = (0, 0, 0)
class Particle_B:
    def __init__(self):
        self.x = random.uniform(0, 400)
        self.y = random.uniform(0, 500)
        sine = np.tan(90)

        self.vx = random.uniform(-1, sine)
        self.vy = random.uniform(-1, 1)

        self.mass = random.uniform(1, 5)

    def update(self, particles):
        for p in particles:
            if p != self:
                dx = p.x - self.x
                dy = p.y - self.y

                dist_sq2 = dx * dx + dy * dy + 30
                dist_2 = math.sqrt(dist_sq2)

                force = (p.mass * self.mass) / dist_2

                self.vx += force * dx / dist_2 * 0.01
                self.vy += force * dy / dist_2 * 0.01
        
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -1
        
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy *= -1
    def draw(self):
        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.x), int(self.y)),
            int(self.mass)

        )

                                
class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)

        self.vx = random.uniform(1, -1)
        self.vy = random.uniform(1, -1)

        self.mass = random.uniform(1, 4)

    def update(self, particles):
        for p in particles:
            if p != self:
                dx = p.x - self.x
                dy = p.y - self.y

                dist_sq = dx * dx + dy * dy + 25
                dist = math.sqrt(dist_sq)

                force = (self.mass * p.mass) / dist_sq

                self.vx += force * dx / dist * 0.01
                self.vy += force * dy / dist * 0.01

        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(
            screen,
            BLUE,
            (int(self.x), int(self.y)),
            int(self.mass)
        )

particles = [Particle_B() for _ in range(2)] + [Particle() for _ in range(2)]
                                       
                   

running = True

while running:
    screen.fill(PEACH)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        particle.update(particles)
        particle.draw()

    pygame.display.flip()
    clock.tick(100)