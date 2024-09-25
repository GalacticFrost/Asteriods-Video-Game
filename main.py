import pygame
from constants import *
from player import Player

def main():

	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))		#Generate a game window
	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)					#Generate the player 

	#Infinite loop - Generate gaming window.
	while True:
		
		screen.fill('black')					#Fill Screen Background
		player.draw(screen)						#Draw player sprite every frame
		pygame.display.flip()					#Refresh the display

		for event in pygame.event.get():
			if event.type == pygame.QUIT:		#Close window - 'x' button	
				return
			
		dt = clock.tick(60)/1000				#Set FPS to 60


	print('Starting asteroids!')
	print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
	main()
