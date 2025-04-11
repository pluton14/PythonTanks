import pygame
import random
from adapter import Adapter
class Environment:
    def __init__(self, width, height, env_adapter):
        self.width = width
        self.height = height
        self.env_adapter = env_adapter
        self.sky = env_adapter.set_image('sky.png')
        self.earth = env_adapter.set_image('earth' + str(random.randint(1, 21)) + '.png')

    def is_sky(self, x, y):
        if 0 <= x < self.earth.get_width() and 0 <= y < self.earth.get_height():
            return self.earth.get_at((int(x), int(y))) == (255, 255, 255, 0)
        return False

    def is_earth(self, x, y):
        return not self.is_sky(x, y)

    def only_sky_in_row(self, t1x, row):
        sky_counter = 0
        for i in range(8, 24):
            if self.is_earth(t1x + i, row):
                sky_counter += 1
        if sky_counter > 2:
            return False
        return True

    def only_sky_in_column(self, column, t1y):
        answer = True
        for i in range(0, 5):
            if self.is_earth(column, t1y + i):
                answer = False
        return answer

    def tanks_up_down(self, tank, x, t1y):
        c1y = 0
        height = 400
        width = 640
        tankheight = 16
        row_below_tank1 = t1y + tankheight
        # Falling down:
        falling1 = 0
        while (row_below_tank1 < height + 2 * tankheight) and self.only_sky_in_row(x, row_below_tank1):

            if self.only_sky_in_row(x, row_below_tank1) and row_below_tank1 < height + 2 * tankheight:
                t1y += 1
                c1y += 1
                falling1 += 1
                row_below_tank1 += 1

            #redraw(False, False)
        may_lift_up = 4
        tank1_last_row = row_below_tank1 - 1
        while may_lift_up >= 0:
            may_lift_up -= 1
            while not self.only_sky_in_row(x, tank1_last_row):
                t1y -= 1
                c1y -= 1
                tank1_last_row -= 1
        return t1y
    def show_explosion(self, x, y):
        for i in range(17):
            self.env_adapter.set_circle(self.earth, x, y, i, (255, 255, 255, 0))
            #pygame.draw.circle(now_screen, color, (x, y), i)