import piece
import pygame
import constants
from piece.imageFigures import ImageFigures


class King(ImageFigures):

    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_king.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_king.png")
        self.pos = pos
        self.type = "king"

    def get_all_moves(self):
        ret = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if abs(x)+abs(y) != 0 and self.pos[0]+x >= 0 and self.pos[0]+x < 8 and self.pos[1]+y >= 0 and self.pos[1]+y < 8:
                    ret.append([self.pos[0]+x, self.pos[1]+y])
        return ret

    def remove_blocked_moves(self, pieces):
        ret = self.get_all_moves()

        for piece in pieces:
            if piece.white == self.white:
                ret.remove([piece.pos[0], piece.pos[1]])

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

    def get_blocked_moves(self, all_moves, piece_move):
        ret = []
        if piece_move[0] < self.pos[0] and piece_move[1] == self.pos[1]:
            ret = self.left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] == self.pos[1]:
            ret = self.right_blocked(all_moves, piece_move)
        if piece_move[1] < self.pos[1] and piece_move[0] == self.pos[0]:
            ret = self.above_blocked(all_moves, piece_move)
        if piece_move[1] > self.pos[1] and piece_move[0] == self.pos[0]:
            ret = self.below_blocked(all_moves, piece_move)
        if piece_move[0] < self.pos[0] and piece_move[1] < self.pos[1]:
            ret = self.above_left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] < self.pos[1]:
            ret = self.above_right_blocked(all_moves, piece_move)
        if piece_move[0] < self.pos[0] and piece_move[1] > self.pos[1]:
            ret = self.below_left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] > self.pos[1]:
            ret = self.below_right_blocked(all_moves, piece_move)
        return ret


    def left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] == piece_move[1]:
                ret.append(move)
        return ret

    def right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] == piece_move[1]:
                ret.append(move)
        return ret

    def above_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[1] < piece_move[1] and move[0] == piece_move[0]:
                ret.append(move)
        return ret

    def below_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[1] > piece_move[1] and move[0] == piece_move[0]:
                ret.append(move)
        return ret

    def above_left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] < piece_move[1]:
                ret.append(move)
                print("Removing: " + str(move[0]) + ", " + str(move[1]))
        return ret

    def below_left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] > piece_move[1]:
                ret.append(move)
        return ret

    def above_right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] < piece_move[1]:
                ret.append(move)
        return ret

    def below_right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] > piece_move[1]:
                ret.append(move)
        return ret
