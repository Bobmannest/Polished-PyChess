import pygame
def events_setup():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.set_visible(0)
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.mouse.set_visible(1)