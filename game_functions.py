import sys
import pygame
from bullet import Bullet
from star import Star
from ufo import UFO
from random import randint
from time import sleep
from asteroid import Asteroid

def check_events(rocket, screen, settings, bullets, play_button, stats, scoreboard, ufos, asteroids):
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
			check_play_button(play_button, mouse_x, mouse_y, stats, scoreboard, rocket, ufos, asteroids, bullets, screen, settings)

def check_play_button(play_button, mouse_x, mouse_y, stats, scoreboard, rocket, ufos, asteroids, bullets, screen, settings):
	# Start a new game when the player clicks the play button.
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.reset_stats()
		scoreboard.prep_health()
		scoreboard.prep_score()
		stats.game_active = True
		
		rocket.center_rocket()
		
		ufos.empty()
		asteroids.empty()
		bullets.empty()
		
		create_fleet(screen, settings, ufos)
		create_asteroid(screen, settings, asteroids)

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

def update_screen(screen, settings, bullets, stars, rocket, asteroids, ufos, scoreboard, stats, play_button):
	# Redraw the screen during each pass through the loop.
	screen.fill(settings.bg_color)
	
	stars.draw(screen)
	
	# Redraw all bullets behind the rocket but above the stars.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	rocket.blitme()
	asteroids.draw(screen)
	ufos.draw(screen)
	
	scoreboard.show_health()
	scoreboard.show_score()
	
	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
	
	if stats.game_over:
		scoreboard.show_game_over()
	
	# Make the most recently drawn screen visible.
	pygame.display.flip()
	
def fire_bullet(bullets, settings, screen, rocket):
	"""Fire a bullet if the bullet limit has not been reached yet."""
	
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < settings.bullets_allowed:
		new_bullet = Bullet(screen, settings, rocket)
		bullets.add(new_bullet)

def update_bullets(bullets, screen, ufos, asteroids, stats, settings, scoreboard):
	"""Update the position of the bullets and remove old bullets."""
		
	# Update bullet positions.
	bullets.update()
	
	# Remove bullets that have disappeared.
	screen_rect = screen.get_rect()
	for bullet in bullets.copy():
		if bullet.rect.left >= screen_rect.right:
			bullets.remove(bullet)
	
	check_for_collisions(bullets, ufos, asteroids, stats, settings, scoreboard, screen)

def check_for_collisions(bullets, ufos, asteroids, stats, settings, scoreboard, screen):
	collisions_ufos = pygame.sprite.groupcollide(bullets, ufos, True, True)
	
	collisions_asteroids = pygame.sprite.groupcollide(bullets, asteroids, True, True)
	
	if collisions_ufos:
		stats.score += settings.ufo_points
		scoreboard.prep_score()

	if len(ufos) == 0:
		bullets.empty()
		create_fleet(screen, settings, ufos)

def get_number_items_x(settings, item_width):
	# The number of columns of items that fit on the screen.
	available_space_x = settings.screen_width - (2 * item_width)
	number_items_x = int(available_space_x / (2 * item_width))
	return number_items_x

def get_number_rows(settings, item_height):
	# The number of rows of items that fit on the screen.
	available_space_y = settings.screen_height - (2 * item_height)
	number_rows = int(available_space_y / (2 * item_height))
	return number_rows

# Create stars.
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

def create_fleet(screen, settings, ufos):
	ufo = UFO(screen, settings)
	number_ufos_x = get_number_items_x(settings, ufo.rect.width)
	number_rows = get_number_rows(settings, ufo.rect.height)
	
	for row_number in range(number_rows):
		for ufo_number in range(number_ufos_x):
			screen_rect = screen.get_rect()
			ufo = UFO(screen, settings)
			ufo_width = ufo.rect.width
			ufo.x = screen_rect.right + ufo_width + 2 * ufo_width * ufo_number
			ufo.rect.x = ufo.x
			ufo.rect.y = ufo.rect.height + 2 * ufo.rect.height * row_number
			ufos.add(ufo)

def create_asteroid(screen, settings, asteroids):
	screen_rect = screen.get_rect()
	asteroid = Asteroid(screen, settings)
	asteroid.rect.x = screen_rect.right - 50
	asteroid.rect.y = screen_rect.top + 50
	asteroids.add(asteroid)

def rocket_hit(stats, scoreboard):
	"""Respond to the rocket being hit by a UFO."""
	if stats.rocket_health_remaining > 0:
		stats.rocket_health_remaining -= 10
		scoreboard.prep_health()
		sleep(0.5)
	else:
		stats.game_active = False
		stats.game_over = True
		pygame.mouse.set_visible(True)

def update_ufos(ufos, rocket, stats, scoreboard):
	ufos.update()
	
	if pygame.sprite.spritecollideany(rocket, ufos):
		rocket_hit(stats, scoreboard)

def update_asteroid(asteroids, rocket, stats, scoreboard):
	asteroids.update()
	
	if pygame.sprite.spritecollideany(rocket, asteroids):
		rocket_hit(stats, scoreboard)
