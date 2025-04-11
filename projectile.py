from math import cos, sin, pi
class Projectile:
    def __init__(self, x, y, angle, power):
        self.x = x
        self.y = y
        self.angle = angle
        self.power = power
        self.vx = cos(angle * pi / 180) * power
        self.vy = -sin(angle * pi / 180) * power
        self.active = True  # Снаряд активен, пока не столкнется

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # Гравитация

    def check_collision(self, environment, tank):
        if tank.hitbox.collidepoint(int(self.x), int(self.y)):
            environment.show_explosion(int(self.x), int(self.y))
            tank.take_damage()
            self.active = False
            return True
        if environment.is_earth(int(self.x), int(self.y)):
            environment.show_explosion(int(self.x), int(self.y))
            self.active = False
            return True

        return False

    def draw(self, screen, now_adapter):
        if self.active:
            ball_image = now_adapter.set_image('ball.png')
            screen.blit(ball_image, (int(self.x), int(self.y)))