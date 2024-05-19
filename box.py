import pygame


class Box:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       img = pygame.image.load("box.png")
       size = img.get_size()
       new_size = (size[0] / 3.75, size[1] / 3.75)
       img = pygame.transform.scale(img, new_size)
       self.image = img
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.delta = .64


   def move_direction(self, direction):
       if direction == "right":
           self.x = self.x + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "up":
           self.y = self.y - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "left":
           self.x = self.x - self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       if direction == "down":
           self.y = self.y + self.delta
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


   def move(self, new_x, new_y):
       self.x = new_x
       self.y = new_y
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

   def get_x(self):
       return self.x

   def get_y(self):
       return self.y

