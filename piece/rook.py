import piece
import pygame
import constants
from piece.imageFigures import ImageFigures


class Rook(ImageFigures):
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_rook.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_rook.png")
        self.pos = pos
        self.type = "rook"

    def get_all_moves(self):
        ret = []
        for x in range(0, 8):
            if x != self.pos[0]:
                ret.append([x, self.pos[1]])
        for y in range(0, 8):
            if y != self.pos[1]:
                ret.append([self.pos[0], y])
        return ret

    def remove_blocked_moves(self, pieces):
        moves = self.get_all_moves()
        if pieces != None:
            blocked_moves = []
            for move in moves:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        if piece.white == self.white:
                            blocked_moves.append(move)
                        if piece.pos[0] < self.pos[0]:
                            self.remove_left(blocked_moves, piece)
                        if piece.pos[0] > self.pos[0]:
                            self.remove_right(blocked_moves, piece)
                        if piece.pos[1] < self.pos[1]:
                            self.remove_up(blocked_moves, piece)
                        if piece.pos[1] > self.pos[1]:
                            self.remove_down(blocked_moves, piece)
            for move in blocked_moves:
                if moves.count(move) == 1:
                    moves.remove(move)


        return moves

    def remove_left(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[0] < piece.pos[0]:
                blocked_moves.append(move)

    def remove_right(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[0] > piece.pos[0]:
                blocked_moves.append(move)

    def remove_up(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[1] < piece.pos[1]:
                blocked_moves.append(move)

    def remove_down(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[1] > piece.pos[1]:
                blocked_moves.append(move)