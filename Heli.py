import pygame
import math

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
        self.original_image = pygame.image.load('./assets/car.png')
        self.image = pygame.transform.scale(self.original_image, (30, 20))
        self.original_image = self.image

        # Helicopter position
        self.rect = self.image.get_rect()
        self.rect.center = (x0, y0)

        # Movement parameters
        self.directionx = x0
        self.directiony = y0
        self.angle = angle0
        self.newangle = angle0
        self.speed = 3

    #Method to move object (special input of dx and dy)
    def follow(self, playerx, playery):
        #Calculating new direction
        self.directionx = playerx-self.x
        self.directiony = playery-self.y
        distance = math.sqrt(self.directionx*self.directionx+self.directiony*self.directiony)
        self.directionx /= distance
        self.directiony /= distance
        self.new_angle = math.atan2(self.directiony, self.directionx)

        #Updating course
        self.x += self.speed*self.directionx
        self.y += self.speed*self.directiony

    def update_pos(self):
        # Update image rotation. Source: https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
        self.image = pygame.transform.rotate(self.original_image, -self.new_angle*180/math.pi+self.angle*180/math.pi)
        self.angle = self.new_angle
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.

    def collided(self, sprite):
        return self.rect.colliderect(sprite.rect)