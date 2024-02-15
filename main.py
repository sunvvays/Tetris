import pygame

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
FPS = 60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

while True:
    game_sc.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(FPS)
