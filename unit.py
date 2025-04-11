import unittest
from unittest.mock import Mock, patch
from game import Game
from environment import Environment
from nowTank import Tank
from cannon import Cannon
from projectile import Projectile
from adapter import Adapter
from human import Human


class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 400
        now_adapter = Adapter()
        self.environment = Environment(self.width, self.height, now_adapter)

    def test_is_earth(self):
        with patch.object(self.environment, 'is_sky', return_value=False):
            self.assertTrue(self.environment.is_earth(10, 10))
        with patch.object(self.environment, 'is_sky', return_value=True):
            self.assertFalse(self.environment.is_earth(10, 10))


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


class TestCannon(unittest.TestCase):
    def setUp(self):
        now_adapter = Adapter()
        self.environment = Environment(640, 400, now_adapter)
        self.environment.width = 640
        self.environment.height = 400
        self.environment.is_sky = lambda x, y: y < 10
        self.tank = Tank(self.environment, 100, 0, 0)
        self.cannon = Cannon(self.tank)

    def test_move_up(self):
        self.cannon.rotate_up()
        self.assertEqual(self.cannon.rotation, 355)

    def test_move_down(self):
        self.cannon.rotate_down()
        self.assertEqual(self.cannon.rotation, 5)


class TestProjectile(unittest.TestCase):
    def setUp(self):
        now_adapter = Adapter()
        self.environment = Environment(640, 400, now_adapter)
        self.tank = Tank(self.environment, 100, 0, 0)
        self.projectile = Projectile(50, 50, 45, 10)

    def test_update(self):
        old_x, old_y = self.projectile.x, self.projectile.y
        self.projectile.update()
        self.assertNotEqual((self.projectile.x, self.projectile.y), (old_x, old_y))

    def test_check_collision(self):
        self.environment.is_earth = lambda x, y: True
        self.assertTrue(self.projectile.check_collision(self.environment, self.tank))


class TestGame(unittest.TestCase):
    @patch('pygame.display.set_mode')
    def setUp(self, mock_set_mode):
        now_adapter = Adapter()
        player1 = Human()
        player2 = Human()
        self.game = Game(now_adapter, now_adapter, player1, player2)

    def test_tank_generation(self):
        self.assertGreaterEqual(self.game.tank1.y, 0)
        self.assertGreaterEqual(self.game.tank2.y, 0)


if __name__ == '__main__':
    unittest.main()
