import pygame


class Dino(pygame.sprite.Sprite)
    def __init__(self, position, images_norm, images_down, width, height):

        pygame.sprite.Sprite.__init__(self)
        self.all_images = []
        self.images_norm = [pygame.transform.smoothscale(pygame.image.load(picture), (width, height)) for picture in images_norm]
        #self.images_down = [pygame.transform.smoothscale(pygame.image.load(picture), (width, height)) for picture in images_down]
        self.image_index = 0
        self.image = self.all_images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direction = "norm"
		self.speed = 10


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
				self.all_images = self.images_norm
            time.sleep(.2)
            self.image_index += 1
            self.image = self.all_images[self.image_index]
            if self.image_index == (len(self.all_images) - 1):
                self.image_index = 0
				
		def move(self, direction):
			
			if(direction == "up"):
				self.rect.y -= self.speed
			#if(direction == "down"):
				# Do image thing with down
				
