import pygame
import constants

class ImageFigures:
    yellow = (255, 255, 0)

    def __init__(self, pos, white):
        self.pos = pos
        self.image = None
        self.white = white
        self.type = "piece"

    def draw(self, surface):
        pixel_pos = [0, 0]
        if self.image == None:
            pixel_pos[0] = self.pos[0]*constants.SQUARE_SIZE + constants.SQUARE_SIZE/2
            pixel_pos[1] = self.pos[1]*constants.SQUARE_SIZE + constants.SQUARE_SIZE/2
            pygame.draw.circle(surface, self.yellow, pixel_pos, constants.SQUARE_SIZE/3)
        else:
            pixel_pos[0] = self.pos[0]*constants.SQUARE_SIZE
            pixel_pos[1] = self.pos[1]*constants.SQUARE_SIZE
            rect = pygame.Rect(pixel_pos[0], pixel_pos[1], constants.SQUARE_SIZE, constants.SQUARE_SIZE)
            surface.blit(self.image, rect)

    def get_all_moves(self):
        moves = []
        return moves

    def remove_blocked_moves(self, pieces):
        moves = []
        return moves

    def move(self, pos):
        self.pos = pos