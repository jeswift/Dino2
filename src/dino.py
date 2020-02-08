import pygame


class Dino(pygame.sprite.Sprite)
    def __init__(self, position, images, width, height):
        """
        initializes the dino class that we use for our main player
        args: name: string, position: tuple (x,y), images: list containing string names of images, skill: int, width: int, height: int
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.power_up_state = "None"
        self.all_images = [pygame.transform.smoothscale(pygame.image.load(picture), (width, height)) for picture in images]
        self.images_down = [pygame.transform.smoothscale(pygame.image.load(picture), (width, height)) for picture in images]
        self.images_right = [pygame.transform.flip(image, True, False) for image in self.images_left]
        self.image_index = 0
        self.image = self.all_images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direction = "right"


        def update(self):
            """
            This should update the Sprites picture every .5 seconds
            args: None
            Return: None
            """
            if self.direction == "right":
                self.all_images = self.images_right
            elif self.direction == "down":
                self.all_images = self.images_down

            time.sleep(.2)
            self.image_index += 1
            self.image = self.all_images[self.image_index]
            if self.image_index == (len(self.all_images) - 1):
                self.image_index = 0

        #    if self.racing:
        #        self.rect.x += self.speed
