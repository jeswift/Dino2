import pygame
from src import controller

def main():
	pygame.init()
	main_window = controller.Controller()
	main_window.mainLoop()
main()