from IControl import IControl
from IPlayer import IPlayer
from nowTank import Tank
from projectile import Projectile
from environment import Environment


class Bot(IPlayer):
    def action(self, now_control: IControl, tank1: Tank, tank2: Tank, projectile: Projectile, env: Environment, state: bool) -> {Projectile, bool, Environment}:
        if projectile:
            projectile.update()
            target_tank = tank1
            if projectile.check_collision(env, target_tank):
                projectile = None
        if not projectile:
            import random
            steps = random.randint(1, 5)
            if random.choice([True, False]):
                for _ in range(steps):
                    tank1.move_left()
            else:
                for _ in range(steps):
                    tank1.move_right()

            angle_steps = random.randint(1, 10)
            if random.choice([True, False]):
                for _ in range(angle_steps):
                    tank1.adjust_cannon_angle_up()
            else:
                for _ in range(angle_steps):
                    tank1.adjust_cannon_angle_down()
            projectile = tank1.shoot()
            state = not state
        return projectile, state, env
