import pygame
import math

#Simple player object
class Bot(pygame.sprite.Sprite):
    '''In main:
        heli = Heli(parameters)
        heli.follow()
        heli.update()
        screen.blit(player.image,player.rect)'''

    # Initialization
    def __init__(self,x0,y0,angle0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.original_image = pygame.image.load(os.path.join('assets\car.png'))#change path directory
        self.image = self.original_image

        # Helicopter position
        self.rect = self.image.get_rect()
        self.rect.center = (x0, y0)

        # Movement parameters
        self.directionx = x0
        self.directiony = y0
        self.angle = angle0
        self.newangle = angle0
        self.speed = 0.5


    #Method to draw object
    def draw(self):
        window.blit(self.image,(self.x,self.y))#mudar para load image algo


    #Method to move object (special input of dx and dy)
    def follow(self, playerx, playery):
        #Calculating new direction
        self.directionx = playerx-self.x
        self.directiony = playery-self.y
        self.new_angle = atan2(self.directionx, self.directiony)

        #Updating course
        self.x += self.speed*math.cos(self.new_angle)
        self.y += self.speed*math.sin(self.new_angle)


    def update(self,angle_step):
        # Update image rotation. Source: https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
        self.image = pygame.transform.rotate(self.original_image, self.new_angle-self.angle)
        self.angle = self.new_angle
        self.angle %= 2 * math.pi
        self.new_angle %= 2 * math.pi
        #x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.