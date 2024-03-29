import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
	#Initialise pygame, settings, and create screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion")
	
	# Make ship
	ship = Ship(ai_settings,screen)
	
	# Start the main loop for the game
	while True:
		#Watch for kybd and mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)
		

		
run_game()
