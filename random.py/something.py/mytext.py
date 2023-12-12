import pygame

pygame.init()

BLACK = (0,0,0)
WHITE =(255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
CORAL = (255,92,64)


SIZE = (400, 500)
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("fancy text")

clock = pygame.time.Clock()

done = False

text_rotate_degrees = 0


while not done: 
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            done = True

    screen.fill(CORAL)
    font = pygame.font.SysFont('Roboto', 25, bold = False, italic = False)

    text = font.render("._.", True, WHITE)
    screen.blit(text, (0,0))
    pygame.display.flip()
    clock.tick

pygame.quit()



