import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, position, img, image_when_hovered_over, image_when_pressed):
        """
        initializes the button class that we use to go between the different screens when pressed
        args: position: tuple (x,y), image: string with image name, image_when_hovered_over: string with image name, image_when_pressed: string with image name
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.normal = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(), (240, 180))
        self.hovered = pygame.transform.smoothscale(pygame.image.load(image_when_hovered_over).convert_alpha(), (240, 180))
        self.pressed = pygame.transform.smoothscale(pygame.image.load(image_when_pressed).convert_alpha(), (240, 180))
        """
        Loading image
        """
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def hoveredOn(self, MousePosition):
        """
        Checks if the mouse is hovering over the button object and changes the picture accordingly
        args: MousePosition: tuple (x,y)
        return: None
        """
        if MousePosition[0] > self.rect.x and MousePosition[0] < self.rect.x + self.rect.width and MousePosition[1] > self.rect.y and MousePosition[1] < self.rect.y + self.rect.height - 60:
             if self.image != self.hovered:
                 self.image = self.hovered
             return True
        else:
             if self.image != self.normal:
                 self.image = self.normal
             return False

    def clickButton(self, MousePosition):
        """
        Checks if the mouse has clicked over the button object and changes the picture accordingly
        args: MousePosition: tuple (x,y)
        return: None
        """
        if MousePosition[0] > self.rect.x and MousePosition[0] < self.rect.x + self.rect.width and MousePosition[1] > self.rect.y and MousePosition[1] < self.rect.y + self.rect.height - 60:
            if self.image != self.pressed:
                self.image = self.pressed
            return True
        else:
            if self.image != self.normal:
                self.image = self.normal
            return False
