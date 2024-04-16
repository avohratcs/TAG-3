import pygame
double_jump_status = True
gravity = 0.011
WIDTH = 1280
HEIGHT = 750
GREEN = (101, 190, 65)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BRWON = (56, 36, 21)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
pygame.font.init()
font_2 = pygame.font.Font("RubikBubbles-Regular.ttf", 70)
font_1 = pygame.font.Font("RubikBubbles-Regular.ttf", 100)
font = pygame.font.Font("PressStart2P-Regular.ttf", 45)
font_3 = pygame.font.Font("PressStart2P-Regular.ttf", 30)
red_man = pygame.image.load("Red.png").convert_alpha()
blue_man = pygame.image.load("Blue.png").convert_alpha()
blue_man = pygame.transform.flip(blue_man, True, False) 
yellow_man = pygame.image.load("Yellow.png").convert_alpha()
purple_man = pygame.image.load("Purple.png").convert_alpha()
explosion = pygame.image.load("Explosion.png").convert_alpha()
explosion = pygame.transform.scale(explosion, (300,115))
arrow_image = pygame.image.load("arrow.png").convert_alpha()
arrow_image = pygame.transform.scale(arrow_image, (200, 200))
WASD_image = pygame.image.load("WASD.png").convert_alpha()
WASD_image = pygame.transform.scale(WASD_image, (200, 200))
WASD_image = pygame.transform.rotate(WASD_image, -20)
class Player:
    def __init__(self, x, y, image):
        self.x = x #Set position on starting platform
        self.y = y
        self.image = image
        self.vx = 0
        self.vy = 0
    def update(self):
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy
    def draw(self):
        player_transformed = pygame.transform.scale(self.image, (50,50))
        screen.blit(player_transformed, (self.x, self.y))
screen_name = "main"#main screen, single screen, multi screen, race mode, bounty mode, controls
options = ["Player Select", "Duration: ", "Double Jump: ", "Controls", "Game Mode: "]
game_modes = ["Lava", "Regular", "Race", "Bounty"]
lava_durs = ["100", "200", "300", "Infinite"]
regular_durs = ["100", "200", "300"]
race_durs = ["1 lap", "3 laps", "5 laps"]
bounty_durs = ["100", "200", "300"]
cur_select_duration = 0
cur_select_mode = 0
cur_select = 0
player_select_mode = False
red_join = False
blue_join = False
red_player = Player(700, 600, red_man)
blue_player = Player(350, 600, blue_man)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if screen_name == "main":
                if cur_select == 1: #TIME
                    if cur_select_mode == 0:
                        if event.key == pygame.K_RIGHT:
                            cur_select_duration += 1
                            if cur_select_duration == 4:
                                cur_select_duration = 0
                        elif event.key == pygame.K_LEFT:
                            cur_select_duration -= 1
                            if cur_select_duration == -1:
                                cur_select_duration = 3
                    else:
                        if event.key == pygame.K_RIGHT:
                            cur_select_duration += 1
                            if cur_select_duration == 3:
                                cur_select_duration = 0
                        elif event.key == pygame.K_LEFT:
                            cur_select_duration -= 1
                            if cur_select_duration == -1:
                                cur_select_duration = 2
                    
                if event.key == pygame.K_RETURN:
                    if cur_select == 0: #Player Select
                        player_select_mode = True
                    elif cur_select == 2: #Double jump
                        double_jump_status = not double_jump_status
                    elif cur_select == 3: #Controls
                        screen_name = "Controls"
                if cur_select == 4:
                    if event.key == pygame.K_RIGHT:
                        cur_select_duration = 0
                        cur_select_mode += 1
                        if cur_select_mode == 4:
                            cur_select_mode = 0
                    elif event.key == pygame.K_LEFT:
                        cur_select_duration = 0
                        cur_select_mode -= 1
                        if cur_select_mode == -1:
                            cur_select_mode = 3
                if event.key == pygame.K_DOWN:
                    cur_select += 1
                    if cur_select == 5:
                        cur_select -= 1
                elif event.key == pygame.K_UP:
                    cur_select -= 1
                    if cur_select == -1:
                        cur_select += 1
                elif event.key == pygame.K_BACKSPACE:
                        if player_select_mode == True:
                            cur_select = 0
                        blue_join = False
                        red_join = False
                        player_select_mode = False
                if player_select_mode == True:
                    if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                        blue_join = not blue_join
                    elif event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                        red_join = not red_join
                    if blue_join == True and red_join == True:
                        if event.key == pygame.K_RETURN:
                            screen_name = "game"
                            #Startup for game
            if screen_name == "Controls":
                if event.key == pygame.K_BACKSPACE:
                    screen_name = "main"

    screen.fill(GREEN)
    if screen_name == "main":
        screen.blit(red_man, (375, 30))
        screen.blit(blue_man, (780, 30))
        screen.blit(explosion, (475,5))
        if blue_join == True:
            screen.blit(arrow_image, (800, 50))
        if red_join == True:
            screen.blit(WASD_image, (225, 30))
        title_text = font_1.render("Tag 3", True, BLUE)
        VS_text = font_1.render("VS.", True, WHITE)
        TEAM_text = font_1.render("TEAM", True, WHITE)
        border_1 = font_1.render("Tag 3", True, BLACK)
        SELF_text = font_1.render("SOLO", True, WHITE)
        screen.blit(border_1, (465, 10))
        screen.blit(title_text, (475, 5))
        y = 300
        for option in options:
            option_text = font.render(option, True, WHITE)
            if option == options[cur_select]:
                if player_select_mode == False:
                    option_text = font.render(option, True, RED)
            screen.blit(option_text, (350, y))
            y += 85
        if player_select_mode == True:
            backspace_text = font_3.render("Backspace = Menu", True, WHITE)
            start_text = font_3.render("Start = Enter", True, WHITE)
            screen.blit(backspace_text, (0,0))
            screen.blit(start_text, (0, 30))
        game_mode = game_modes[cur_select_mode]
        game_mode_text = font.render(game_mode, True, WHITE)
        screen.blit(game_mode_text, (800, 640))
        if cur_select_mode == 0:
           if blue_join == True and red_join == True:
            screen.blit(TEAM_text, (450, 120))
           duration = lava_durs[cur_select_duration]
           duration_text = font.render(duration, True, WHITE) 
           screen.blit(duration_text, (750, 385))
        if cur_select_mode == 0:
           if (blue_join == True or red_join == True) and not (blue_join == True and red_join == True):
            screen.blit(SELF_text, (450, 120))
           duration = lava_durs[cur_select_duration]
           duration_text = font.render(duration, True, WHITE) 
           screen.blit(duration_text, (750, 385))
           
        elif cur_select_mode == 1:
           if blue_join == True and red_join == True:
            screen.blit(VS_text, (550, 120))
           duration = regular_durs[cur_select_duration]
           duration_text = font.render(duration, True, WHITE) 
           screen.blit(duration_text, (750, 385))
        elif cur_select_mode == 2:
           if blue_join == True and red_join == True:
            screen.blit(VS_text, (550, 120))
           duration = race_durs[cur_select_duration]
           duration_text = font.render(duration, True, WHITE) 
           screen.blit(duration_text, (750, 385))
        elif cur_select_mode == 3:
           if blue_join == True and red_join == True:
            screen.blit(VS_text, (550, 120))
           duration = bounty_durs[cur_select_duration]
           duration_text = font.render(duration, True, WHITE) 
           screen.blit(duration_text, (750, 385))
        if double_jump_status == False:
            double_jump_status_text_no = font.render("NO", True, WHITE)
            screen.blit(double_jump_status_text_no, (900, 470))
        else:
            double_jump_status_text_yes = font.render("YES", True, WHITE)
            screen.blit(double_jump_status_text_yes, (900, 470))  
    if screen_name == "Controls":
        control_title = font_1.render("Controls", True, WHITE)
        screen.blit(control_title, (400, 5)) 
        split_control_section_1 = pygame.draw.rect(screen, BLACK, pygame.Rect(350, 0, 30, 1000))  
        split_control_section_2 = pygame.draw.rect(screen, BLACK, pygame.Rect(875, 0, 30, 1000)) 
        split_control_section_3 = pygame.draw.rect(screen, BLACK, pygame.Rect(350, 110, 525, 30))
    if screen_name == "game":
        ground = pygame.draw.rect(screen, BRWON, pygame.Rect(0, 700, 1920,300))
        red_player.draw()
        blue_player.draw()
        red_player.update()
        blue_player.update()
    pygame.display.flip()
pygame.quit()