import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position, image, width, height):
        """
        creates the obstacle class that we use for the obstacle game
        args: position: tuple (x,y), image: string with image name, width: int, height: int
        return: None
        """
        pygame.sprite.Sprite.__init__(self)

        """
        Loading image
        """
        self.image = pygame.transform.smoothscale(pygame.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
