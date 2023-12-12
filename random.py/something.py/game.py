
import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen_width = 100
screen_height = 400
size = (100,400)
screen = pygame.display.set_mode(size)
score = 0
done = False

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()


class block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
    
        super().__init__()
    
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()



class Player():
    def update():

        def reset_pos():
            def update(self):
                pos = pygame.mouse.get_pos()
                self.rect.x = 50

for i in range(50):
    # This is a block
    block = block("black", 20, 15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)

    while not done:

        for event in pygame.event.get():
                if event.type -- pygame.QUIT:
                    done = True

    screen.fill(WHITE) 

    all_sprites_list.update

    block_hit_list = pygame.sprite.spritecollide(Player, block, False)

    for block in block_hit_list:
        score += 1
        print(score)

        block.reset_pos()

        all_sprites_list.draw(screen)

        clock.tick(20)

        pygame.display.flip()

for i in range(50):

    random_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    block = block(random_color, 0, 255)

        
pygame.quit()