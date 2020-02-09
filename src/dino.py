import pygame
import time


class Dino(pygame.sprite.Sprite):


	def __init__(self, position, images_norm, images_down, width, height):

		pygame.sprite.Sprite.__init__(self)
		img1 = pygame.image.load(images_norm[0]).convert_alpha()
		img1.set_alpha(128)
		img2 = pygame.image.load(images_norm[1]).convert_alpha()
		img2.set_alpha(128)
		img3 = pygame.image.load(images_norm[2]).convert_alpha()
		img3.set_alpha(128)
		self.images_norm = [pygame.transform.smoothscale(img1, (width, height)),pygame.transform.smoothscale(img2, (width, height)),pygame.transform.smoothscale(img3, (width, height))]
		#self.images_down = [pygame.transform.smoothscale(pygame.image.load(picture), (width, height)) for picture in images_down]
		self.all_images = self.images_norm
		self.image_index = 0
		self.image = self.all_images[self.image_index]
		self.rect = pygame.Rect(self.image.get_rect().left, self.image.get_rect().top, 65, self.image.get_rect().height)
		self.rect.x = position[0]
		self.rect.y = position[1]
		self.direction = "norm"
		self.speed = 5
		

	def update(self):
		"""
		This should update the Sprites picture every .5 seconds
		args: None
		Return: None
		"""
		if self.direction == "norm":
			self.all_images = self.images_norm
		#elif self.direction == "down":
			#self.all_images = self.images_down
		
		if self.image_index == 2:
			self.image_index = 0
		else:
			self.image_index +=1
		self.image = self.all_images[self.image_index]
			
