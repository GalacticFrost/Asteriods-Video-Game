import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot

def main():

	pygame.init()

	#Generate a game window
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#Create a clock instance - used for FPS later	
	clock = pygame.time.Clock()
	#Delta time
	dt = 0

	#Create sprite groups - DRY + CLEAN code
	updatable = pygame.sprite.Group() 									
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	#Add sprite groups to Player class
	Player.containers = (updatable, drawable)
	#Generate player sprite at center of window
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	#Generate player bullets
	Shot.containers = (bullets, updatable, drawable)

	#Add sprite groups to Asteroid class
	Asteroid.containers = (asteroids, updatable, drawable)

	#Add sprite group to AsteroidField
	AsteroidField.containers = (updatable)
	#Generate AsteroidField
	asteroidfield = AsteroidField()

	#Infinite loop - Generate gaming window.
	while True:
		
		#Fill the game window black - Background
		screen.fill('black')
		
		#Loop over objects in groups and apply relevant object method
		for obj in updatable:
			obj.update(dt)

		#Loop over asteroids, check for collision between player and or bullets
		for obj in asteroids:

			for bullet in bullets:
				if obj.collision(bullet):
					bullet.kill()
					obj.split()
	
			if obj.collision(player):
				print('Game over!')
				sys.exit()

		for obj in drawable:
			obj.draw(screen)

		#Links the close window button ('x') to terminate the game window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				return

		#Update the display with the above code	
		pygame.display.flip()
		#Set the games FPS to 60
		dt = clock.tick(60)/1000

	# print('Starting asteroids!')
	# print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
	main()
