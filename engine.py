import pygame

class LoadSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(LoadSprite, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('img/1.png'))
        self.images.append(pygame.image.load('img/2.png'))
        self.images.append(pygame.image.load('img/3.png'))
        self.images.append(pygame.image.load('img/4.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(2, 2, 50, 98)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]


