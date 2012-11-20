#!/usr/bin/env python

from sys import stdin, stdout

def prompt (pre):
    stdout.write (pre);
    out = stdin.readline().strip()
    return out

class Game (object):
    '''An implementation of the game 'Tic-Tac-Toe' '''

    def __init__ (self, players=1, boardsize=3):
        self.players = players
        self.playerlist = []
        self.Board = Board(boardsize)

    def check_game (self):
        '''Fill this in'''

        diag1 = []
        diag2 = []
        stalecount = 0
        stalemate = lambda noncon: int(0 not in noncon and \
                    len (set (noncon)) > 1)
        winner = lambda fill: fill[0] > 0 and \
                 fill.count(fill[0]) is self.grid.grid_x and \
                 self.endgame (1, fill[0])

        for i in range(self.grid.grid_x):
            row = self.grid.tiles[self.grid.grid_x * (i):self.grid.grid_x * (i + 1)]
            col = self.grid.tiles[i::self.grid.grid_x]
            diag1.append (self.grid.tiles[i + (i * self.grid.grid_x)])
            diag2.append (self.grid.tiles[(self.grid.grid_x * (i + 1)) - (i + 1)])

            winner (row)
            winner (col)
            stalecount += stalemate (row) + stalemate (col)

        winner (diag1)
        winner (diag2)
        stalecount += stalemate (diag1) + stalemate (diag2)
        if stalecount is (i + i + 4): self.endgame (2)

    def endgame (self, state, player = 0):
        '''Declares the winner of the game, ends the game'''

        if (state is 1):
            print "You are a winner, Player " + str(player)
        else:
            print "A stalemate has been drawn."

    def turn (self, player):
        move = player.move (self.grid.board[:])
        pass

    def loop (self):
        for player in self.playerlist:
            if player is not self.Robot: self.draw_grid()
            self.turn (player)

    def draw_grid (self):
        if self.grid_v is None: self.grid_v = len (str (self.grid.grid_x))
        zerofill = "{0:0>" + self.grid_v  + "}"
        for tilenum in range (1, len (self.grid.tiles)+1):
            stdout.write (zerofill.format(tilenum))

            if tilenum % self.grid.grid_x is 0:
                stdout.write ("\n")
                # Draw a line that spans the width of the grid
                # Using a lambda or urwid
                stdout.write ("\n")
            else: stdout.write (" | ")

    class Board (object):
        '''Dimensions and grid objects'''
        def __init__ (self, grid_x=3, grid_y=0):
            self.tiles = None
            self.grid_x = grid_x
            if grid_y == 0:
                self.grid_y = grid_x

        def generate (self):
            '''Fill this in'''
            self.tiles = [[0 * grid_x] * grid_y]

    class Player (object):
        '''Info about the player'''
        def __init__(self, name):
            self.name = name

    class Robot (Player):
        '''Info about the bot'''
        def botname (self):
            '''Fill this in'''
            pass

        def strategy (self):
            '''Fill this in'''
            pass

ttt = Game(1)
ttt.interactive()
