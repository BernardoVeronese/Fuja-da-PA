import pygame
import math


#Constants
APPROACH_CONSTANT = 4
ANGLE_STEP = 0.05
RADIUS = 60

#Simple player object
class Heli(pygame.sprite.Sprite):
    '''In main:
        heli = Heli(parameters)
        heli.follow()
        heli.update()
        screen.blit(heli.image,heli.rect)'''

    # Initialization
    def __init__(self,x0,y0,angle0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.image = pygame.image.load('./assets/heli.png')
        self.image = pygame.transform.scale(self.image, (110, 60))

        # Helicopter position
        self.rect = self.image.get_rect()
        self.rect.center = (x0, y0)

        # Movement parameters
        self.directionx = x0
        self.directiony = y0
        self.distance = x0+y0
        self.angle = angle0
        self.newangle = angle0
        self.speed = 3
        self.left_state = True

    #Method to move object (special input of dx and dy)
    def follow(self, playerx, playery):
        #Calculating new direction
        self.directionx = playerx-self.x
        self.directiony = playery-self.y
        self.distance = math.sqrt(self.directionx*self.directionx+self.directiony*self.directiony)
        self.directionx /= self.distance
        self.directiony /= self.distance
        #self.new_angle = math.atan2(self.directiony, self.directionx)
        #self.angle %= 2 * math.pi
        #Updating course
        self.x += self.speed*self.directionx
        self.y += self.speed*self.directiony

    def orientation_shift(self, playerx):
        prev_state = self.left_state
        if self.x < playerx:
            self.left_state = False
        else:
            self.left_state = True
        if not prev_state == self.left_state:
            return True

    def update_pos(self, playerx):
        # Update image rotation. Source: https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
        '''self.image = pygame.transform.rotate(self.original_image, -self.angle*180/math.pi)
        self.angle = self.new_angle
        self.angle %= 2 * math.pi'''
        if self.orientation_shift(playerx) and self.distance > APPROACH_CONSTANT:
            self.image = pygame.transform.flip(self.image, True, False)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.

    def collided(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def patrol(self, x_locus, y_locus):
        self.x = x_locus+math.cos(self.angle) * RADIUS
        self.y = y_locus+math.sin(self.angle) * RADIUS
        self.angle -= ANGLE_STEP
        self.angle %= 2 * math.pi

