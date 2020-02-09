import pygame

class Floor(pygame.sprite.Sprite):
	def __init__(self, position, image, width, height):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.image.set_alpha(128)
		self.image = pygame.transform.smoothscale(self.image, (width, height))
		self.rect = self.image.get_rect()
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.speed = 4