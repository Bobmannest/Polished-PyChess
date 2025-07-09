#Type: color-name
import pygame

piece_board = [[None for _ in range(8)] for _ in range(8)]

class Piece:
    def __init__(self, type: str, current_pos: list):
        self.type = type
        self.current_pos = current_pos
        self.rect = pygame.Rect(120+self.current_pos[1]*64, 110+self.current_pos[0]*64, 64, 64)
        piece_board[self.current_pos[0]][self.current_pos[1]] = self

    def draw(self, screen):
        image = pygame.image.load('pieces/' + self.type + '.png')
        image_resized = pygame.transform.scale(image, (64, 64))
        screen.blit(image_resized, (120+self.current_pos[1]*64, 110+self.current_pos[0]*64))

    def get_type(self):
        return self.type

    def get_rect(self):
        return self.rect



