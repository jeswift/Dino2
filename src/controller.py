import pygame, time, sys, json, random
from src import button, dino, obstacle, background_image, floor


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
		self.buttons = pygame.sprite.Group()
		self.allobs = pygame.sprite.Group()
		self.env_state = "JUNGLE"


	def mainLoop(self):
		while True:
			pygame.event.get()
			if self.state == "MAINMENU":
				self.mainMenuLoop()
			elif self.state== "DINOGAME":
				self.gameLoop()


	def mainMenuLoop(self):
	
		#Put Menu Background
		self.screen.blit(self.background, (0,0))
		BackGround = background_image.Background('assets/MenuBackGround.jpg')
		self.screen.blit(BackGround.image, BackGround.rect)
		#Put title DINO 2 on
		#Create our Main menu buttons
		self.desert_button = button.Button((25, 40), "assets/buttons/DesertButton.png", "assets/buttons/DesertButtonPressed.png", 150, 80)
		self.jungle_button = button.Button((25, 160), "assets/buttons/JungleButton.png", "assets/buttons/JungleButtonPressed.png", 150, 80)
		self.water_button = button.Button((25, 280), "assets/buttons/WaterButton.png", "assets/buttons/WaterButtonPressed.png", 150, 80)
		self.bing_button = button.Button((25, 400), "assets/buttons/BingButton.png", "assets/buttons/BingButtonPressed.png", 150, 80)
		self.buttons.add(self.bing_button, self.water_button, self.desert_button, self.jungle_button)
		self.buttons.draw(self.screen)
		#Title
		myfont = pygame.font.SysFont('Gill Sans', 100)
		title = myfont.render('DINO 2', False, (255,0,0))
		self.screen.blit(title, (375, 100))
		#Flip the display
		pygame.display.flip()
		
			
			
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
					if MousePosition[0] > self.desert_button.rect.x and MousePosition[0] < self.desert_button.rect.x\
					+ self.desert_button.rect.width and MousePosition[1] > self.desert_button.rect.y and MousePosition[1] < self.desert_button.rect.y\
					+ self.desert_button.rect.height:
						self.state = "DINOGAME"
						self.env_state = "DESERT"
						
					if MousePosition[0] > self.jungle_button.rect.x and MousePosition[0] < self.jungle_button.rect.x\
					+ self.jungle_button.rect.width and MousePosition[1] > self.jungle_button.rect.y and MousePosition[1] < self.jungle_button.rect.y\
					+ self.jungle_button.rect.height:
						self.state = "DINOGAME"
						self.env_state = "JUNGLE"
						
					if MousePosition[0] > self.water_button.rect.x and MousePosition[0] < self.water_button.rect.x\
					+ self.water_button.rect.width and MousePosition[1] > self.water_button.rect.y and MousePosition[1] < self.water_button.rect.y\
					+ self.water_button.rect.height:
						self.state = "DINOGAME"
						self.env_state = "WATER"
						
					if MousePosition[0] > self.bing_button.rect.x and MousePosition[0] < self.bing_button.rect.x\
					+ self.bing_button.rect.width and MousePosition[1] > self.bing_button.rect.y and MousePosition[1] < self.bing_button.rect.y\
					+ self.bing_button.rect.height:
						self.state = "DINOGAME"
						self.env_state = "BING"
			
			self.buttons.draw(self.screen)
			pygame.display.update([self.desert_button.rect, self.jungle_button.rect, self.bing_button.rect, self.water_button.rect])

	def gameLoop(self):
		
		self.player = dino.Dino((50,350), ["assets/Dinos/JungleDino1.png","assets/Dinos/JungleDino2.png","assets/Dinos/JungleDino3.png"], \
		["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
		floorIMG = "assets/OG Dino Sprites/Dino Floor.png"
		
		self.all_sprites = pygame.sprite.Group(self.player)
		Dinolist = []
		
		if self.env_state == "JUNGLE":
			self.screen.blit(self.background, (0,0))
			BackGround = background_image.Background('assets/JungleBackGround.png')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,350), ["assets/Dinos/JungleDino1.png","assets/Dinos/JungleDino2.png","assets/Dinos/JungleDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			floorIMG = "assets/JungleDino/JungleFloor.png"
			Dinolist = ["assets/JungleDino/Flower.png","assets/JungleDino/Rock.png","assets/JungleDino/Stump.png", "assets/JungleDino/Log.png"]
			
		elif self.env_state == "DESERT":
			self.screen.blit(self.background, (0,0))
			BackGround = background_image.Background('assets/DesertBackGround.png')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,350), ["assets/Dinos/DesertDino1.png","assets/Dinos/DesertDino2.png","assets/Dinos/DesertDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			floorIMG = "assets/DesertDino/Dino Floor.png"
			Dinolist = ["assets/DesertDino/Cactus.png","assets/DesertDino/Snake.png","assets/DesertDino/SnakeBoot.png", "assets/DesertDino/Flower.png"]
			
		elif self.env_state == "WATER":
			self.screen.blit(self.background, (0,0))
			BackGround = background_image.Background('assets/WaterBackGround.png')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,350), ["assets/Dinos/WaterDino1.png","assets/Dinos/WaterDino2.png","assets/Dinos/WaterDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			floorIMG = "assets/WaterDino/WaterFloor.png"
			Dinolist = ["assets/WaterDino/Clam.png","assets/WaterDino/Starfish.png","assets/WaterDino/SeaWeed.png", "assets/WaterDino/Skull.png"]
			
		elif self.env_state == "BING":
			self.screen.blit(self.background, (0,0))
			BackGround = background_image.Background('assets/BingBackGround.png')
			self.screen.blit(BackGround.image, BackGround.rect)
			self.player = dino.Dino((50,350), ["assets/Dinos/BingDino1.png","assets/Dinos/BingDino2.png","assets/Dinos/BingDino3.png"], \
			["assets/OG Dino Sprites/duckDino1.png","assets/OG Dino Sprites/duckDino2.png"], 80, 85)
			floorIMG = "assets/BingDino/DinoFloor.png"
			Dinolist = ["assets/BingDino/Clam.png","assets/BingDino/Starfish.png","assets/BingDino/SeaWeed.png", "assets/BingDino/Skull.png"]
		
		
		pygame.display.flip()
		
		time1 = time.clock()
		timeChangeTracker = 0
		
		jumpClock1= 0
		jumping = False
		storedJumpClock = 0
		
		prevTime = 0
		
		self.floor1 = floor.Floor((0,410), floorIMG, 950, 175)
		self.floor2 = floor.Floor((950,410), floorIMG, 950, 175)
		floors = [self.floor1,self.floor2]
		obstacles = []
		
		while self.state == "DINOGAME":
		
			updateRects = []
			xloc = self.player.rect.x
			yloc = self.player.rect.y
			updateRects.append(pygame.Rect(xloc,yloc,80,85))
			self.screen.blit(BackGround.image, BackGround.rect)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if(event.key == pygame.K_UP and self.player.rect.y >= 350):
						jumpClock1 = time.clock()
						jumping = True
						
			
			self.screen.blit(BackGround.image, BackGround.rect)
			if round(time.clock()-prevTime, 2)%.10 == 0 and round(time.clock()-prevTime, 2) != 0:
				prevTime = time.clock()
				updateRects.append(pygame.Rect(xloc,yloc,80,85))
				self.player.update()
				updateRects.append(self.player.rect)
			
			#Section for floor and obstacles
			
			timeChange = round(time.clock() - time1,2)
			if timeChange != timeChangeTracker:
				timeChangeTracker = timeChange
				for ob in obstacles:
					if(ob.rect.x < -100):
						updateRects.append(ob.rect)
						self.allobs.remove(ob)
						ob.kill()
						obstacles.remove(ob)
					else:
						updateRects.append(pygame.Rect(ob.rect.x, ob.rect.y, 40, 80))
						ob.rect.x -= ob.speed
						updateRects.append(ob.rect)
						self.screen.blit(ob.image, ob.rect)
					
				for f in floors:
					if(f.rect.x > 0 and f.rect.x < 3):
						fnew = floor.Floor((950,410), floorIMG, 950, 175)
						floors.append(fnew)
						obIMG = random.choice(Dinolist)
						ob = obstacle.Obstacle((950,360), obIMG, 40, 80)
						obstacles.append(ob)
						self.allobs.add(ob)
					elif(f.rect.x < -940):
						f.kill()
						floors.remove(f)
					xFloorLoc = f.rect.x
					yFloorLoc = f.rect.y
					updateRects.append(pygame.Rect(xFloorLoc,yFloorLoc,950,468))
					f.rect.x -= f.speed
					updateRects.append(f.rect)
					self.screen.blit(f.image,f.rect)
				
			#Jumping Section
			deltaJumpTime = round(time.clock()-jumpClock1,2)
			#secondPlaceValue = 0
			#if len(str(deltaJumpTime)) >= 4:
			#	secondPlaceValue = int(str(deltaJumpTime)[3])
			if (jumping == True) and (deltaJumpTime <= .7) and (storedJumpClock != deltaJumpTime):
				storedJumpClock = deltaJumpTime
				updateRects.append(pygame.Rect(xloc,yloc,80,85))
				print(deltaJumpTime)
				if(deltaJumpTime <= .35):
					self.player.rect.y -= self.player.speed
				elif .69 >= deltaJumpTime > .35:
					self.player.rect.y += self.player.speed
				else:
					self.player.rect.y += self.player.speed
					jumping = False
					jumpClock1 = 0
					storedJumpClock = 0
				updateRects.append(self.player.rect)
			
			self.screen.blit(self.player.image, self.player.rect)
			pygame.display.update(updateRects)
			
			hitObstacle = pygame.sprite.spritecollide(self.player, self.allobs, True)
			if hitObstacle:
				myfont = pygame.font.SysFont('Elephant', 80)
				lost = myfont.render('YOU LOST', False, (0,0,0))
				self.screen.blit(lost, (200, 50))
				lost2 = myfont.render('THE GAME', False, (0,0,0))
				self.screen.blit(lost2, (200, 150))
				pygame.display.flip()
				pygame.time.wait(6000)
				self.state = "MAINMENU"
				
			
			
