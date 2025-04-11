import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from game import Game
from adapter import Adapter
from human import Human
from bot import Bot


def main():
    now_adapter = Adapter()
    player1 = Human()
    player2 = Human()
    game = Game(now_adapter, now_adapter, player1, player2)

    game.run()


if __name__ == "__main__":
    main()
