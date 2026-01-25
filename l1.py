import pygame

pygame.init()

screen = pygame.display.set_mode((400,500))
done = False

background_image = pygame.transform.scale(pygame.image.load('Background.jpg').convert(), (700,500))


while not done:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()

    screen.blit(background_image, (0,0))
    pygame.display.flip()

