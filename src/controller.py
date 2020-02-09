import pygame, time, sys, json, random
from src import dino, obstacle, background_image


class Controller:
    def __init__(self, width=950, height=500):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Dino2')
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state = "MAINMENU"
        self.player = dino.Dino((50,400), )
        self.won = False
        self.obstacle = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()


    def mainLoop(self):
        """
        calls different Controller methods based on the current state
        args: None
        return: none
        """
        while True:
            pygame.event.get()
            if self.state == "MAINMENU":
                self.mainMenuLoop()
            elif self.state == "HIGHSCORES":
                self.highScoreLoop()
            elif self.state== "DINOGAME":
                self.gameLoop()


    def mainMenuLoop(self):
        
		self.desert_button = button.Button((25, 40), "assets/buttons/DesertButton.png", "assets/buttons/DesertButtonPressed.png", 150, 80)
        self.jungle_button = button.Button((25, 160), "assets/buttons/JungleButton.png", "assets/buttons/JungleButtonPressed.png", 150, 80)
        self.water_button = button.Button((25, 280), "assets/buttons/WaterButton.png", "assets/buttons/WaterButtonPressed.png", 150, 80)
        self.bing_button = button.Button((25, 300), "assets/buttons/BingButton.png", "assets/buttons/BingButtonPressed.png", 150, 80)
		

        while self.state == "MAINMENU":
            
			
			MousePosition = pygame.mouse.get_pos()
            self.coin_button.hoveredOn(MousePosition)
            self.obstacle_button.hoveredOn(MousePosition)
            self.race_button.hoveredOn(MousePosition)
            self.highscores_button.hoveredOn(MousePosition)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.highScoreWrite(self.name, self.player.skill)
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.coin_button.clickButton(MousePosition):
                        self.state = "COIN"
                    if self.obstacle_button.clickButton(MousePosition):
                        self.state = "OBSTACLE"
                    if self.race_button.clickButton(MousePosition):
                        self.state = "RACE"
                    if self.highscores_button.clickButton(MousePosition):
                        self.state = "HIGHSCORES"
            self.buttons.add(self.coin_button, self.obstacle_button, self.race_button, self.highscores_button)
            self.screen.blit(self.background, (0,0))
            BackGround = background_image.Background('assets/Background pictures/4_game_background/4_game_background.png')
            self.screen.fill([255, 255, 255])
            self.screen.blit(BackGround.image, BackGround.rect)
            myfont = pygame.font.SysFont('Algerian', 100)
            message = myfont.render('Fish Fun', False, (0,0,0))
            self.screen.blit(message, (100, 150))
            myfont2 = pygame.font.SysFont('Ariel', 40)
            skill_message = myfont2.render('Skill Level: ' + str(self.player.skill), False, (0,0,0))
            if self.won:
                winner = myfont2.render('RACE WINNER! ', False, (0,0,0))
                self.screen.blit(winner, (70, 470 - skill_message.get_height()- 5))
            self.screen.blit(skill_message, (70, 470))
            self.buttons.draw(self.screen)
            pygame.display.flip()


    def gameLoop(self):
        while self.state == "DINOGAME"
