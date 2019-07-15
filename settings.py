class Settings():
	""" A class to store all settings for Alien Invasion """
	def __init__(self):
		"""Initialise the game's settings"""
		# Screen
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (102,196,225)

		# Ship settings
		self.ship_speed_factor = 1.5
