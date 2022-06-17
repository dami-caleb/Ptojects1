
import pygame
import time
import math
from utils import scale_image, blit_rotate_center

#GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("track.png"), 0.9)

#TRACK_BORDER = scale_image(pygame.image.load("track-border.png"), 0.9)

RED_CAR = scale_image(pygame.image.load("red_car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("green_car.png"), 0.55)
WHITE_CAR = scale_image(pygame.image.load("white_car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Truck Platoon Simulation")

FPS = 60


class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200) 

class PlayerCar1(AbstractCar): 
    IMG = GREEN_CAR
    START_POS = (180, 250) 
class PlayerCar2(AbstractCar):
    IMG = WHITE_CAR
    START_POS = (180, 300) 



def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()


###start simulation
run = True
clock = pygame.time.Clock()
#images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
images = [(TRACK, (0, 0))]
player_car = PlayerCar(4, 4)
player_car1 = PlayerCar1(4, 4)
player_car2 = PlayerCar2(4, 4)

while run:
    clock.tick(FPS)

    draw(WIN, images, player_car)
    draw(WIN, images, player_car1)
    draw(WIN, images, player_car2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()


pygame.quit()




#if __name__ == "__main__":
#    action1()