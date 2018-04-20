import piece
import pygame
import constants
from piece.imageFigures import ImageFigures


class Pawn(ImageFigures):
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_pawn.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_pawn.png")
        self.pos = pos
        self.type = "pawn"

    def get_all_moves(self):
        ret = []
        if self.white == True:
            if self.pos[1]-1 >= 0:
                ret.append([self.pos[0], self.pos[1]-1])
                ret.append([self.pos[0]-1, self.pos[1]-1])
                ret.append([self.pos[0]+1, self.pos[1]-1])
            if self.pos[1] == 6:
                ret.append([self.pos[0], self.pos[1]-2])
        if self.white == False:
            if self.pos[1]+1 <= 7:
                ret.append([self.pos[0], self.pos[1]+1])
                ret.append([self.pos[0]-1, self.pos[1]+1])
                ret.append([self.pos[0]+1, self.pos[1]+1])
            if self.pos[1] == 1:
                ret.append([self.pos[0], self.pos[1]+2])
        return ret


    def remove_blocked_moves(self, pieces):
        moves_containing_piece = self.get_moves_containing_piece(pieces)
        moves_without_piece = self.get_moves_not_containing_piece(pieces)
        possible_moves = []

        for move in moves_containing_piece:
            if move[0] == self.pos[0]:
                pass
            else:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        if piece.white != self.white:
                            possible_moves.append(move)

        for move in moves_without_piece:
            if move[0] == self.pos[0]:
                possible_moves.append(move)
            else:
                pass

        if len(possible_moves) == 1:
            if abs(possible_moves[0][1] - self.pos[1]) == 2:
                return []
        return possible_moves

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