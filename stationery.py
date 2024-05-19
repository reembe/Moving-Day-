import pygame


class Stationery:
   def __init__(self, x, y, image, Small):
       self.x = x
       self.y = y
       img = pygame.image.load(image)
       size = img.get_size()
       if Small == True:
           new_size = (size[0] / 2.5, size[1] / 2.5)
       else:
           new_size = (size[0] / 3.25, size[1] / 3.25)
       img = pygame.transform.scale(img, new_size)
       self.image = img
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


   def move(self, new_x, new_y):
       self.x = new_x
       self.y = new_y
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

