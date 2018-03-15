import pygame

#Simple player object
class Bot(object):

    # Initialization
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = image
        #self.angle = angle
        #self.speed = speed

    #Method to draw object
    def draw(self):
        window.blit(self.image,(self.x,self.y))#mudar para load image algo

    #Method to move object (special input of dx and dy)
    def follow(self):
        


    #def move(self, speed, angle)
        #self.x += math.sin(self.angle) * self.speed
        #self.y -= math.cos(self.angle) * self.speed