
import pygame, os
from pygame.locals import *

pygame.init()

#Center the Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

y1 = 0
y2 = 0
y3 = 0
x1 = 0
speed1 = 0.5
speed2 = 0.55
speed3 = 0.6
speed4 = 0.6
bgColor = 0, 0, 0
barHeight = 75
barWidth = 25
screen_width = 800
screen_height = 600
display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Simple Animation")
progress = True
barcolor1 = (255, 0, 0)
barcolor2 = (0, 255, 0)
barcolor3 = (0, 0, 255)
barcolor4 = (255, 255, 255)

display.fill(bgColor)

for i in range(0, barHeight):
        pygame.draw.line(display, barcolor1, (0, y1+i), (screen_width-1, y1+i))

        y1 += speed1

        if y1 + barHeight > screen_height-1 or y1 <0:i

while progress: type
event = pygame.event.poll()
if event.type == pygame.QUIT:
        progress = False
        pygame.quit()
        quit()
