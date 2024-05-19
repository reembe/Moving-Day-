import pygame


class Toys:
   def __init__(self, x, y, image, Small, Big):
       self.x = x
       self.y = y
       img = pygame.image.load(image)
       size = img.get_size()
       if Small == True:
           new_size = (size[0] / 4.75, size[1] / 4.75)
       elif Big == True:
           new_size = (size[0] / 3.25, size[1] / 3.25)
       else:
           new_size = (size[0] / 5.25, size[1] / 5.25)
       img = pygame.transform.scale(img, new_size)
       self.image = img
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


   def move(self, new_x, new_y):
       self.x = new_x
       self.y = new_y
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])