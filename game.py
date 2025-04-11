import random
from time import sleep
from environment import Environment
from nowTank import Tank
from IView import IView
from IControl import IControl
from IPlayer import IPlayer


class Game:
    def __init__(self, now_adapter: IView, now_control: IControl, player1: IPlayer, player2: IPlayer):
        self.width = 640
        self.height = 400
        self.now_adapter = now_adapter
        self.now_control = now_control
        self.Player1 = player1
        self.Player2 = player2
        self.screen = self.now_adapter.set_screen(self.width, self.height)
        self.clock = now_adapter.set_clock()
        self.running = True
        self.turn = "1"
        self.state = True
        self.environment = Environment(self.width, self.height, self.now_adapter)
        t1x = self.width / 6 + random.randint(0, int(self.width / 6))
        t1y = 0
        while self.only_sky_in_row1(t1x, t1y) and t1y + 16 < self.height:
            t1y += 1

        t2x = self.width / 6 * 4 + random.randint(0, int(self.width / 6))
        t2y = 0
        while self.only_sky_in_row2(t2x, t2y) and t2y + 16 < self.height:
            t2y += 1

        rot1 = 0
        rot2 = 180
        self.tank1 = Tank(self.environment, x=t1x, y=t1y, rotation=rot1)
        self.tank2 = Tank(self.environment, x=t2x, y=t2y, rotation=rot2)
        self.projectile = None
        #pygame.init()

    def only_sky_in_row1(self, t1x, row):
        sky_counter = 0
        for i in range(8, 24):
            if self.environment.is_earth(t1x + i, row):
                sky_counter += 1
        if sky_counter > 2:
            return False

    def only_sky_in_row2(self, t2x, row):
        sky_counter = 0
        for i in range(8, 24):
            if self.environment.is_earth(t2x + i, row):
                sky_counter += 1
        if sky_counter > 2:
            return False
        return True

    def run(self):
        self.tank1.y = self.environment.tanks_up_down(self.tank1, self.tank1.x, self.tank1.y)
        self.tank2.y = self.environment.tanks_up_down(self.tank2, self.tank2.x, self.tank2.y)
        now_tank = self.tank1
        while self.running:
            #self.handle_events() #--
            now_tank = self.update_game_state(now_tank)
            self.draw()
            #self.clock.tick(30)

    def update_game_state(self, target_tank):
        self.tank1.y = self.environment.tanks_up_down(self.tank1, self.tank1.x, self.tank1.y)
        self.tank2.y = self.environment.tanks_up_down(self.tank2, self.tank2.x, self.tank2.y)
        self.tank1.hitbox_update()
        self.tank2.hitbox_update()
        if self.state:
            self.projectile, self.state, self.environment = self.Player1.action(self.now_control, self.tank1,
                                                                                self.tank2,
                                                                                self.projectile, self.environment,
                                                                                self.state)

        self.tank1.y = self.environment.tanks_up_down(self.tank1, self.tank1.x, self.tank1.y)
        self.tank2.y = self.environment.tanks_up_down(self.tank2, self.tank2.x, self.tank2.y)
        self.tank1.hitbox_update()
        self.tank2.hitbox_update()
        if not self.state:
            self.projectile, self.state, self.environment = self.Player2.action(self.now_control, self.tank2,
                                                                                self.tank1,
                                                                                self.projectile, self.environment,
                                                                                self.state)
        return target_tank

    def draw(self):
        self.screen.blit(self.environment.sky, (0, 0))
        self.screen.blit(self.environment.earth, (0, 0))
        self.tank1.draw(self.screen)
        self.tank2.draw(self.screen)
        if self.projectile:
            self.projectile.draw(self.screen, self.now_adapter)
        self.now_adapter.my_flip()
