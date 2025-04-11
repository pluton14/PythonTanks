from adapter import Adapter
class Cannon:
    def __init__(self, tank):
        self.cannon_adapter = Adapter()
        self.tank = tank
        self.image = self.cannon_adapter.set_image('tank1-cannon.png')
        self.rotation = tank.rotation

    def rotate_up(self):
        self.rotation = (self.rotation - 5) % 360

    def rotate_down(self):
        self.rotation = (self.rotation + 5) % 360

    def draw(self, screen, now_adapter):
        rotated_cannon = now_adapter.set_rotate(self.image, self.rotation)
        cannon_width = rotated_cannon.get_width()
        cannon_x = self.tank.x + (self.tank.width - cannon_width) // 2
        cannon_y = self.tank.y - 14
        screen.blit(rotated_cannon, (cannon_x, cannon_y))