import pygame
from pygame import*
from random import randint
pygame.init()

clock = time.Clock()


window_width = 1100

window_height = 600

window_res = (window_width,window_height)

character_width = 100
character_height = 100

width = 100
height = 100

spawn_rate = 360
frame_rate = 60

starting_bucks = 15
buck_rate = 120
starting_buck_booster = 1

max_bad_reviews = 3
win_time = frame_rate * 60 * 1

reg_speed = 2

slow_speed = 1

white = (255,255,255)

GAME_WINDOW = display.set_mode(window_res)

display.set_caption("._.")

#character = pizza

background_img = image.load('restaurant.jpg').convert()
background_surf = Surface.convert_alpha(background_img) 
BACKGROUND = transform.scale(background_surf, window_res) 
 
character_img = image.load('vampire.png').convert_alpha()
character_surf = Surface.convert_alpha(character_img)
CHARACTER = transform.scale(character_surf, (character_width, character_height))

garlic_img = image.load("garlic.png")
garlic_surf = Surface.convert_alpha(garlic_img)
garlic = transform.scale(garlic_surf,(character_width, character_height))

cutter_img = image.load("pizzacutter.png")
cutter_surf = Surface.convert_alpha(cutter_img)
cutter = transform.scale(cutter_surf,(character_width, character_height))

pepperoni_img = image.load("pepperoni.png")
pepperoni_surf = Surface.convert_alpha(pepperoni_img)
pepperoni = transform.scale(pepperoni_surf,(character_width, character_height))

class vampiresprite(sprite.Sprite):
        def __init__(self):
                super().__init__()
                self.speed = reg_speed
                self.lane = randint(0, 4)
                all_vampires.add(self)
                self.image = CHARACTER.copy()
                y = 50 + self.lane * 100
                self.rect = self.image.get_rect(center = (1100, y))
                self.health = 100

        def update(self, game_window, counters):
                game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
                self.rect.x -= self.speed
                if self.health <= 0 or self.rect.x <= 100:
                        self.kill()
                        if self.rect.x <= 100:
                                counters.bad_reviews += 1
                else:
                        game_window.blit(self.image, (self.rect.x, self.rect.y))
        def attack(self, tile):
                if tile.trap == slow:
                        self.speed = slow_speed
                if tile.trap == damage:
                        self.health -= 1 

class Counters(object):
        def __init__(self, pizza_bucks, buck_rate, buck_booster, timer):
                self.loop_count = 0
                self.display_font = font.Font("pizza_font.ttf", 25)
                self.pizza_bucks = pizza_bucks
                self.buck_rate = buck_rate
                self.buck_booster = buck_booster
                self.bucks_rect = None
                self.timer = timer
                self.timer_rect = None
                self.bad_reviews = 0
                self.bad_rev_rect = None
        def increment_bucks(self):
                if self.loop_count % self.buck_rate == 0:
                        self.pizza_bucks += self.buck_booster
        def draw_bucks(self, game_window):
                if bool(self.bucks_rect):
                        game_window.blit(BACKGROUND, (self.bucks_rect.x,self.bucks_rect.y), self.bucks_rect)
                bucks_surf = self.display_font.render(str(self.pizza_bucks), True, white)
                self.bucks_rect = bucks_surf.get_rect()
                self.bucks_rect.x = window_width - 50
                self.bucks_rect.y = window_height - 50
                game_window.blit(bucks_surf, self.bucks_rect)
        def draw_bad_reviews(self, game_window): 
                if bool(self.bad_rev_rect): 
                        game_window.blit(BACKGROUND, (self.bad_rev_rect.x, self.bad_rev_rect.y), self.bad_rev_rect) 
                bad_rev_surf = self.display_font.render(str(self.bad_reviews), True, white) 
                self.bad_rev_rect = bad_rev_surf.get_rect() 
                self.bad_rev_rect.x = window_width - 150 
                self.bad_rev_rect.y = window_height - 50 
                game_window.blit(bad_rev_surf, self.bad_rev_rect) 
        def draw_timer(self, game_window): 
                if bool(self.timer_rect): 
                    game_window.blit(BACKGROUND, 
(self.timer_rect.x,self.timer_rect.y), self.timer_rect) 
        timer_surf = self.display_font.render(str((win_time - self.loop_count) // frame_rate), True, white) 
        self.timer_rect = timer_surf.get_rect() 
        self.timer_rect.x = window_width - 250 
        self.timer_rect.y = window_height - 50
        game_window.blit(timer_surf, self.timer_rect)

        def update(self, game_window):
                self.loop_count += 1
                self.increment_bucks()
                self.draw_bucks(game_window)
                self.draw_bad_reviews(game_window)
                self.draw_timer(game_window)
class trap(object):
        def __init__(self, trap_kind, cost, trap_img):
                self.cost = cost
                self.trap_img = trap_img

class trapapplicator(object):
        def __init__(self):
                self.selected = None
        def select_trap(self, trap):
                if trap.cost <= counters.pizza_bucks:
                        self.selected = trap
        def select_tile(self, tile, counters):
                self.selected = tile.set_trap(self.selected, counters)
                                

class backgroundtile(sprite.Sprite):
        def __init__(self, rect):
                super().__init__()
                self.trap = None
                self.rect = rect

class playtile(backgroundtile):
        def set_trap(self, trap, counters):
                if bool(trap) and not bool(self.trap):
                        counters.pizza_bucks -= trap.cost
                        self.trap = trap
                        if trap == earn:
                                counters.buck_booster += 1
                return None
        def draw_trap(self, game_window, trap_applicator):
                if bool(self.trap):
                        game_window.blit(self.trap.trap_img, (self.rect.x, self.rect.y))

class buttontile(backgroundtile):   
        def set_trap(self, trap, counters): 
                if counters.pizza_bucks >= self.trap.cost: 
                        return self.trap 
                else:
                        return None 
        def draw_trap(self, game_window, trap_applicator): 
                if bool(trap_applicator.selected): 
                    if trap_applicator.selected == self.trap: 
                        draw.rect(game_window, (238, 190, 47), (self.rect.x, self.rect.y, width, height), 5) 
 
class inactivetile(backgroundtile): 
    def set_trap(self, trap, counters): 
        return None 
    def draw_trap(self, game_window, trap_applicator): 
        pass

all_vampires = sprite.Group()

counters = Counters(starting_bucks, buck_rate, starting_buck_booster, win_time)

slow = trap("slow", 5, garlic)
damage = trap("damage", 3, cutter)
earn = trap("earn", 7, pepperoni)
        

trap_applicator = trapapplicator()

tile_grid = []


tile_color = white
for row in range(6):
        row_of_tiles = []
        tile_grid.append(row_of_tiles)
        for column in range(11):
                tile_rect = Rect(width * column, height * row, width, height)
                if column <= 1:
                        new_tile = inactivetile(tile_rect)
                else:
                        if row == 5:
                                if 2<= column <= 4:
                                        new_tile = buttontile(tile_rect)
                                        new_tile.trap = [slow, damage, earn][column - 2]
                                else:
                                        new_tile = inactivetile(tile_rect)
                        else:
                                new_tile = playtile(tile_rect)
                row_of_tiles.append(new_tile)

                if row == 5 and 2<= column <= 4:
                                BACKGROUND.blit(new_tile.trap.trap_img, (new_tile.rect.x, new_tile.rect.y))
                if column != 0 and row != 5:
                        if column != 1:
                                draw.rect(BACKGROUND, tile_color, (width * column, height * row, width, height), 1)

 
GAME_WINDOW.blit(BACKGROUND, (0, 0))


game_running = True
program_running = True
while game_running:
        
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            game_running = False
            program_running = False

        elif event.type == MOUSEBUTTONDOWN:
                coordinates = mouse.get_pos()
                x = coordinates[0]
                y = coordinates[1]

                tile_y = y // 100
                tile_x = x // 100
                trap_applicator.select_tile(tile_grid[tile_y][tile_x], counters)
                
        if randint(1, spawn_rate) == 1:
                vampiresprite()

        for tile_row in tile_grid:
                for tile in tile_row:
                        if bool(tile.trap):
                                GAME_WINDOW.blit(BACKGROUND, (tile.rect.x, tile.rect.y), tile.rect)

        for vampire in all_vampires:
                tile_row = tile_grid[vampire.rect.y // 100]
                vampire_left_side = vampire.rect.x // 100
                vampire_right_side = (vampire.rect.x + vampire.rect.width)//100
                if 0 <= vampire_left_side <= 10:
                        left_tile = tile_row[vampire_left_side]
                else:
                        left_tile = None
                if 0<= vampire_right_side <= 10:
                        right_tile = tile_row[vampire_right_side]
                else:
                        right_tile = None
                if bool(left_tile):
                        vampire.attack(left_tile)
                if bool (right_tile):
                        if right_tile != left_tile:
                                vampire.attack(right_tile)

        if counters.bad_reviews >= max_bad_reviews:
                game_running = False
        if counters.loop_count > win_time:
                game_running = False
                                                  

        for vampire in all_vampires:
                vampire.update(GAME_WINDOW, counters)
        for tile_row in tile_grid:
                for tile in tile_row:
                        tile.draw_trap(GAME_WINDOW, trap_applicator)

        counters.update(GAME_WINDOW)
             
        display.update()

        clock.tick(frame_rate)

end_font = font.Font('pizza_font.ttf',50)  
if program_running: 
    if counters.bad_reviews >= max_bad_reviews: 
        end_surf = end_font.render('lose ._.', True, white) 
    else: 
        end_surf = end_font.render('win', True, white) 
    GAME_WINDOW.blit(end_surf, (350, 200)) 
    display.update() 
 
while program_running: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            program_running = False 
    clock.tick(frame_rate)
    
pygame.quit()