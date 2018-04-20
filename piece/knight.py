import piece
import pygame
import constants
from piece.imageFigures import ImageFigures


class Knight(ImageFigures):
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_knight.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_knight.png")
        self.pos = pos
        self.type = "knight"

    def get_all_moves(self):
        ret = []
        for x in range(-2, 3):
            for y in range(-2, 3):
                if self.pos[0] + x >= 0 and self.pos[0] + x <= 7 and self.pos[1] + y >= 0 and self.pos[1] + y <= 7:
                    if abs(x)+abs(y) == 3:
                        ret.append([self.pos[0]+x, self.pos[1]+y])
        return ret

    def remove_blocked_moves(self, pieces):
        ret = []
        moves_with_piece = self.get_moves_containing_piece(pieces)
        moves_without_piece = self.get_moves_not_containing_piece(pieces)
        for move in moves_without_piece:
            ret.append(move)
        for move in moves_with_piece:
            for piece in pieces:
                if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                    if piece.white != self.white:
                        ret.append(move)

        return ret

    def get_moves_containing_piece(self, pieces):
        moves = self.get_all_moves()
        moves_containing_piece = []
        if pieces != None:
            for move in moves:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        moves_containing_piece.append(move)
        return moves_containing_piece

    def get_moves_not_containing_piece(self, pieces):
        moves = self.get_all_moves()
        moves_not_containing_piece = moves[:]
        for piece in pieces:
            for move in moves:
                if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                    moves_not_containing_piece.remove(move)
        return moves_not_containing_piece