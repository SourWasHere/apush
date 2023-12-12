import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption = "turbo ._."
window_surface = pygame.display.set_mode((800, 600))


background = pygame.Surface((800, 600))
background.fill("#ffffff")


class Background:
    def bg_image(self, image, size_x, size_y):
        size_x = self.size_x
        size_y = self.size_y
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, (size_x, size_y))

class Sprite:
    def __init__(self, image, size_x, size_y):
        self.location_x = 0
        self.location_y = 0
        imp = pygame.image.load(self.image)
        size_x = self.size_x
        size_y = self.size_y
        imp = pygame.transform.scale(imp, (size_x, size_y))
        def move(move_x, move_y):
            self.location_x += move_x
            self.location_y += move_y

img = Background.bg_image("face.png", 356, 245)
imp = Sprite.image("fish.jpg", 100, 100)

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 500), (100, 50)), text="Start", manager=manager)


clock = pygame.time.Clock()
time_cumulative = 0
running = True

while running: 
    time_delta = clock.tick(60) / 1000.0
    time_cumulative += time_delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                if img.location_y < 600:
                    img.move(10, 10)
                else:
                    img.location_x = -100
                    img.location_y = -100
                print(time_delta)
                print(time_cumulative)
                print("._.")
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0,0))
    window_surface.blit(img, (0, 0))
    window_surface.blit(imp, (img.location_x, img.location_y))
    manager.draw_ui(window_surface)
    pygame.display.update()

pygame.quit()









