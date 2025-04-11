from IControl import IControl
from IPlayer import IPlayer
from nowTank import Tank
from projectile import Projectile
from environment import Environment


class Human(IPlayer):
    def __init__(self):
        self.environment = None

    def action(self, now_control: IControl, tank1: Tank, tank2: Tank, projectile: Projectile, env: Environment, state: bool) -> {Projectile, bool, Environment}:
        if projectile:
            projectile.update()
            target_tank = tank1
            if projectile.check_collision(env, target_tank):
                projectile = None
        now_events, keys = now_control.get_events()
        for now_key in keys:
            if now_key == 1:
                state = not state
                projectile = tank1.shoot()
            if now_key == 2:
                tank1.move_left()
            if now_key == 3:
                tank1.move_right()
            if now_key == 4:
                tank1.adjust_cannon_angle_down()
            if now_key == 5:
                tank1.adjust_cannon_angle_up()
        return projectile, state, env
