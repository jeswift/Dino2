import pygame

class Background(pygame.sprite.Sprite):
		def __init__(self, img, position=(0,0)):
			"""
			Initializes the background class that we use for the image backgrounds
			args: img: string with file name, position: tuple (x,y)
			return: None
			"""
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.transform.smoothscale(pygame.image.load(img).convert(), (950, 500))
			self.rect = self.image.get_rect()
			self.rect.x = position[0]
			self.rect.y = position[1]
