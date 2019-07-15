import sys
import pygame

def check_events(ship):
	"""Respond to key presses and mouse events"""
	for event in pygame.event.get():
		if event.type ==  pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				# Move the ship to the right on key down
				ship.moving_right = True
			if event.key == pygame.K_LEFT:
				# Move the ship to the left on key down
				ship.moving_left = True
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				# Stop moving ship right on key up
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				# Stop moving ship left on key up
				ship.moving_left = False
			
def update_screen(ai_settings,screen,ship):
        """ Update images on the screen and flip to the new screen"""
        # Redraw the screen with each pass through the loop	
        screen.fill(ai_settings.bg_color)	
        ship.blitme()
        
        # Make the most recently drawn screen visible
        pygame.display.flip()