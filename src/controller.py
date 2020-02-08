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
        self.won = False
        self.obstacle = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
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
        """
        Displays the main menu screen. Blitz the background image, Fish Fun, skill level, and buttons.
        Calls button methods based on mouse position for changing button images
        args: None
        returns: None
        """

        """ MAIN MENU BUTTONS ADD HERE

        self.coin_button = button.Button((650, 10), "assets/buttons/catchcoins1.png", "assets/buttons/catchcoins2.png", "assets/buttons/catchcoins3.png")
        self.obstacle_button = button.Button((650, 130), "assets/buttons/obstacle1.png", "assets/buttons/obstacle2.png", "assets/buttons/obstacle3.png")
        self.race_button = button.Button((650, 250), "assets/buttons/race1.png", "assets/buttons/race2.png", "assets/buttons/race3.png")"""

        while self.state == "MAINMENU":
            self.highscores_button = button.Button((650, 370), "assets/buttons/highscores.png", "assets/buttons/highscores2.png", "assets/buttons/highscores3.png")
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
            
