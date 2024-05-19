import pygame


class WelcomeChicken:
   def __init__(self, x, y, image):
       self.x = x
       self.y = y
       img = pygame.image.load(image)
       size = img.get_size()
       new_size = (size[0] / .8, size[1] / .8)
       img = pygame.transform.scale(img, new_size)
       self.image = img
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
