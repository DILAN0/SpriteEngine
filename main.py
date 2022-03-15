import pygame


bgcolor = pygame.Color('black')
size = WIDTH, HEIGHT = 1280, 720
fps = 30


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


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    my_sprite = LoadSprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        screen.fill(bgcolor)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()


