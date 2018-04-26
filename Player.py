import pygame, sys
import math

#Simple player object
class Player(pygame.sprite.Sprite):
    '''In main:
    player = Player(parameters)
    player.move()
    player.update()
    screen.blit(player.image,player.rect)'''

    # Initialization
    def __init__(self, x0, y0, angle0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.original_image = pygame.image.load('./assets/car.png')
        self.image = pygame.transform.scale(self.original_image,(30,20))
        self.original_image = self.image

        #Player position
        self.rect = self.image.get_rect()
        self.rect.center = (x0,y0)

        #Direction flags
        self.up = False
        self.down = False
        self.right = False
        self.left = False

        #Movement parameters
        self.angle = angle0
        self.speed = 5
        self.dir = 0
        self.pitch = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.up = True
            if event.key == pygame.K_a:
                self.left = True
            if event.key == pygame.K_s:
                self.down = True
            if event.key == pygame.K_d:
                self.right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.up = False
            if event.key == pygame.K_a:
                self.left = False
            if event.key == pygame.K_s:
                self.down = False
            if event.key == pygame.K_d:
                self.right = False

    '''#Method to move object
    def move(self, terrain_factor):
        if self.down:
            self.y += self.speed*terrain_factor
        if self.up:
            self.y -= self.speed*terrain_factor
        if self.left:
            self.x -= self.speed*terrain_factor
        if self.right:
            self.x += self.speed*terrain_factor'''


    def move(self, terrain_factor, angle_step):
        if self.down and not self.up:
            self.dir = -1
        elif self.up and not self.down:
            self.dir = 1
        else:
            self.dir = 0
        if self.left and not self.right:
            self.angle += angle_step*math.pi/180
            self.pitch = -1
        elif self.right and not self.left:
            self.angle -= angle_step*math.pi/180
            self.pitch = +1
        self.angle %= 2*math.pi
        self.x += math.cos(self.angle) * self.speed*terrain_factor*self.dir
        self.y -= math.sin(self.angle) * self.speed*terrain_factor*self.dir

    def update_pos(self, angle_step):
        #Update image rotation. Source: https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
        self.image = pygame.transform.rotate(self.original_image, self.angle*180/math.pi+self.pitch * angle_step)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.

    def collided(self, sprite):
        return self.rect.colliderect(sprite.rect)