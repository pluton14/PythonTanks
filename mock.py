import unittest
from unittest.mock import Mock, patch
#import pygame
from game import Game
from environment import Environment
from nowTank import Tank
from cannon import Cannon
from projectile import Projectile
from adapter import Adapter


class TestTank(unittest.TestCase):
    def setUp(self):
        now_adapter = Adapter()
        self.environment = Environment(640, 400, now_adapter)
        self.environment.width = 640
        self.environment.height = 400
        self.environment.is_sky = lambda x, y: y < 10
        self.tank = Tank(self.environment, 100, 0, 0)
        self.tank.y = self.environment.tanks_up_down(self.tank, self.tank.x, self.tank.y)

    def test_find_ground_level(self):
        self.assertEqual(self.tank.find_ground_level(0), 10)

    def test_move_left(self):
        #now_x = self.tank.x
        self.tank.move_left()
        #print(self.tank.x)
        self.assertEqual(self.tank.x, 95)

    def test_move_right(self):
        self.tank.move_right()
        self.assertEqual(self.tank.x, 105)

    def test_take_damage(self):
        self.tank.take_damage()
        self.assertEqual(self.tank.health, 4)
        for _ in range(4):
            self.tank.take_damage()
        self.assertEqual(self.tank.health, 0)