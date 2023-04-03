import sys
import pygame
from bullet import Bullet
from star import Star
from ufo import UFO
from random import randint

def check_events(rocket, screen, settings, bullets, play_button, stats):
	# Watch for keyboard events.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, rocket, screen, settings, bullets)
		elif event.type == pygame.KEYUP:
			keyup_events(event, rocket)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(play_button, mouse_x, mouse_y, stats)

def check_play_button(play_button, mouse_x, mouse_y, stats):
	"""Start a new game when the player clicks the button."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.game_active = True

def keydown_events(event, rocket, screen, settings, bullets):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_SPACE:
		fire_bullet(bullets, settings, screen, rocket)
	elif event.key == pygame.K_RIGHT:
		rocket.moving_right = True
	elif event.key == pygame.K_LEFT:
		rocket.moving_left = True
	elif event.key == pygame.K_UP:
		rocket.moving_up = True
	elif event.key == pygame.K_DOWN:
		rocket.moving_down = True

def keyup_events(event, rocket):
	if event.key == pygame.K_RIGHT:
		rocket.moving_right = False
	elif event.key == pygame.K_LEFT:
		rocket.moving_left = False
	elif event.key == pygame.K_UP:
		rocket.moving_up = False
	elif event.key == pygame.K_DOWN:
		rocket.moving_down = False

def update_screen(screen, settings, bullets, stars, rocket, ufos, stats, play_button):
	# Redraw the screen during each pass through the loop.
	screen.fill(settings.bg_color)
	
	stars.draw(screen)
	
	# Redraw all bullets behind the rocket but above the stars.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	rocket.blitme()
	ufos.draw(screen)
	
	# Draw the play button to the screen if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
	
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	
def fire_bullet(bullets, settings, screen, rocket):
	"""Fire a bullet if the bullet limit has not been reached yet."""
	
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(screen, settings, rocket)
		bullets.add(new_bullet)

def update_bullets(bullets, screen, ufos, settings):
	"""Update the position of the bullets and remove old bullets."""
		
	# Update bullet positions.
	bullets.update()
	
	# Remove bullets that have disappeared.
	screen_rect = screen.get_rect()
	for bullet in bullets.copy():
		if bullet.rect.left >= screen_rect.right:
			bullets.remove(bullet)
	
	collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
	
	if len(ufos) == 0:
		bullets.empty()
		create_ufos(screen, settings, ufos)

def get_number_items_x(settings, item_width):
	# The number of columns of items that fit on the screen.
	available_space_x = settings.screen_width - 2 * item_width
	number_items_x = int(available_space_x / (2 * item_width))
	return number_items_x

def get_number_rows(settings, item_height):
	# The number of rows of items that fit on the screen.
	available_space_y = settings.screen_height - 2 * item_height
	number_rows = int(available_space_y / (2 * item_height))
	return number_rows

def create_stars(screen, settings, stars):
	star = Star(screen, settings)
	
	number_stars_x = get_number_items_x(settings, star.rect.width)
	
	number_rows = get_number_rows(settings, star.rect.height)
	
	for column_number in range(number_stars_x):
		create_star_column(number_rows, screen, settings, column_number, stars)

def create_star_column(number_rows, screen, settings, column_number, stars):
	for star_number in range(number_rows):
		create_star(screen, settings, star_number, column_number, stars)

def create_star(screen, settings, star_number, column_number, stars):
	star = Star(screen, settings)
	star_width = star.rect.width
	star_height = star.rect.height
	star.x = star_width + 5 * star_width * column_number + randint(-10, 10)
	star.rect.x = star.x
	star.y = star_height + 2 * star_height * star_number + randint(-10, 10)
	star.rect.y = star.y
	stars.add(star)

def update_stars(stars, screen, settings):
	stars.update()
	
	make_new_stars = False
	for star in stars.copy():
		if star.check_disappeared():
			stars.remove(star)
			make_new_stars = True
	
	if make_new_stars:
		star = Star(screen, settings)
		number_stars_x = get_number_stars_x(settings, star.rect.width)
		number_rows = get_number_rows(settings, star.rect.height)
		create_star_column(number_rows, screen, settings, number_stars_x, stars)

def create_ufos(screen, settings, ufos):
	ufo = UFO(screen, settings)
	
	number_ufos_x = get_number_items_x(settings, ufo.rect.width)
	
	number_rows = get_number_rows(settings, ufo.rect.height)
	
	create_ufo_column(number_rows, screen, settings, number_ufos_x, ufos)

def create_ufo_column(number_rows, screen, settings, column_number, ufos):
	for ufo_number in range(number_rows):
		create_ufo(screen, settings, ufo_number, column_number, ufos)

def create_ufo(screen, settings, ufo_number, column_number, ufos):
	ufo = UFO(screen, settings)
	ufo_width = ufo.rect.width
	ufo_height = ufo.rect.height
	ufo.x = ufo_width + 2 * ufo_width * column_number
	ufo.rect.x = ufo.x
	ufo.y = ufo_height + 2 * ufo_height * ufo_number
	ufo.rect.y = ufo.y
	ufos.add(ufo)

def update_ufos(ufos):
	ufos.update()
