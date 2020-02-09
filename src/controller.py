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
        self.obstacle = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
		self.env_state = "JUNGLE"


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
            elif self.state== "DINOGAME":
                self.gameLoop()


    def mainMenuLoop(self):
        #Create our Main menu buttons
		self.desert_button = button.Button((25, 40), "assets/buttons/DesertButton.png", "assets/buttons/DesertButtonPressed.png", 150, 80)
        self.jungle_button = button.Button((25, 160), "assets/buttons/JungleButton.png", "assets/buttons/JungleButtonPressed.png", 150, 80)
        self.water_button = button.Button((25, 280), "assets/buttons/WaterButton.png", "assets/buttons/WaterButtonPressed.png", 150, 80)
        self.bing_button = button.Button((25, 300), "assets/buttons/BingButton.png", "assets/buttons/BingButtonPressed.png", 150, 80)
		self.buttons.add(self.bing_button, self.water_button, self.desert_button, self.jungle_button)
		self.buttons.draw(self.screen)
		
		#Put Menu Background
		self.screen.blit(self.background, (0,0))
		BackGround = background_image.Background('assets/MenuBackGround.jpg')
		self.screen.blit(BackGround.image, BackGround.rect)
		#Put title DINO 2 on
		myfont = pygame.font.SysFont('Algerian', 100)
		title = myfont.render('DINO 2', False, (0,0,0))
		self.screen.blit(title, (100, 150))
		#Flip the display
		self.display.flip()
			
			
        while self.state == "MAINMENU":
			#Change button if hovered
			MousePosition = pygame.mouse.get_pos()
            self.desert_button.hoveredOn(MousePosition)
            self.jungle_button.hoveredOn(MousePosition)
            self.water_button.hoveredOn(MousePosition)
            self.bing_button.hoveredOn(MousePosition)
			
			
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #ADD SCORING ELEMENT HERE??
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.desert_button.clickButton(MousePosition):
                        self.state = "DINOGAME"
						self.env_state = "DESERT"
						self.update(self.desert_button.rect)
                    if self.jungle_button.clickButton(MousePosition):
                        self.state = "DINOGAME"
						self.env_state = "JUNGLE"
						self.update(self.jungle_button.rect)
                    if self.water_button.clickButton(MousePosition):
                        self.state = "DINOGAME"
						self.env_state = "WATER"
						self.update(self.water_button.rect)
                    if self.bing_button.clickButton(MousePosition):
                        self.state = "DINOGAME"
						self.env_state = "BING"
						self.update(self.bing_button.rect)
            


    def gameLoop(self):
		
		self.player = dino.Dino((50,400), ["assets/Dinos/JungleDino1.png","assets/Dinos/JungleDino2.png","assets/Dinos/JungleDino3.png"], \
		["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
		
		
		if self.env_state == "JUNGLE":
			self.screen.blit(self.background, (0,0))
            BackGround = background_image.Background('assets/JungleBackGround.jpg')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,400), ["assets/Dinos/JungleDino1.png","assets/Dinos/JungleDino2.png","assets/Dinos/JungleDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			
		else if self.env_state == "DESERT":
			self.screen.blit(self.background, (0,0))
            BackGround = background_image.Background('assets/DesertBackGround.jpg')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,400), ["assets/Dinos/DesertDino1.png","assets/Dinos/DesertDino2.png","assets/Dinos/DesertDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			
		else if self.env_state == "WATER":
			self.screen.blit(self.background, (0,0))
            BackGround = background_image.Background('assets/WaterBackGround.jpg')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,400), ["assets/Dinos/WaterDino1.png","assets/Dinos/WaterDino2.png","assets/Dinos/WaterDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			
		else if self.env_state == "BING":
			self.screen.blit(self.background, (0,0))
            BackGround = background_image.Background('assets/BingBackGround.jpg')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,400), ["assets/Dinos/BingDino1.png","assets/Dinos/BingDino2.png","assets/Dinos/BingDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
		
		
		pygame.display.flip()
		
		
        while self.state == "DINOGAME":
			updateRects = []
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_UP and self.rect.y > 400:
						self.player.move("up")
					elif(event.key == pygame.K_DOWN and self.rect.y > 400:
						self.player.move("down")
						
						
			self.player.update()
			updateRects.add(self.player.rect)
			pygame.display.update(updateRects)
			
			
