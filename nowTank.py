from projectile import Projectile
from cannon import Cannon
from adapter import Adapter


class Tank:
    MAX_HEALTH = 5

    def __init__(self, environment, x, y, rotation, is_player_controlled=True):
        self.tank_adapter = Adapter()
        self.environment = environment
        self.x = x
        self.y = self.find_ground_level(y)
        self.rotation = rotation
        self.energy = 100
        self.health = Tank.MAX_HEALTH
        self.is_player_controlled = is_player_controlled
        self.image = self.tank_adapter.set_image('tank1-nocannon.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)  # Хитбокс танка
        self.hitbox = self.tank_adapter.set_rect(self.x, self.y, self.width, self.height)
        self.cannon = Cannon(self)

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.health = 0
            print("Танк уничтожен!")

    def draw_health_bar(self, screen):
        health_bar_width = 40
        health_bar_height = 5
        health_ratio = self.health / Tank.MAX_HEALTH
        health_color = (255 * (1 - health_ratio), 255 * health_ratio, 0)

        self.tank_adapter.set_square(screen, self.x, self.y - 10, health_bar_width,  health_bar_height,(255, 0, 0))  # Красный фон
        self.tank_adapter.set_square(screen, self.x, self.y - 10, (health_bar_width * health_ratio), health_bar_height, health_color)  # Заполнение

    def find_ground_level(self, start_y):
        y = start_y
        #x = start_x
        while self.environment.only_sky_in_row(self.x, y):
            y += 1
        #y -= 12
        return y

    def adjust_cannon_angle_up(self):
        self.cannon.rotate_up()

    def adjust_cannon_angle_down(self):
        self.cannon.rotate_down()

    def move_left(self):
        new_x = self.x - 5
        if new_x >= 0 and self.environment.only_sky_in_column(new_x, self.y):
            self.x = new_x
            #self.y = self.find_ground_level(self.y)
            self.y = self.environment.tanks_up_down(self, self.x, self.y)
        else:
            print("Not left " + str(self.y))

    def move_right(self):
        new_x = self.x + 5
        if new_x + self.width < self.environment.width and self.environment.only_sky_in_column(new_x, self.y):
            self.x = new_x
            #self.y = self.find_ground_level(self.y)
            self.y = self.environment.tanks_up_down(self, self.x, self.y)
        else:
            print("Not right ", str(self.y))

    # def move_autonomously(self):
    #     import random
    #     steps = random.randint(1, 5)
    #
    #     if random.choice([True, False]):
    #         for _ in range(steps):
    #             self.move_left()
    #     else:
    #         for _ in range(steps):
    #             self.move_right()
    #
    #     angle_steps = random.randint(1, 10)
    #     if random.choice([True, False]):
    #         for _ in range(angle_steps):
    #             self.adjust_cannon_angle_up()
    #     else:
    #         for _ in range(angle_steps):
    #             self.adjust_cannon_angle_down()

    def hitbox_update(self):
        self.hitbox = self.tank_adapter.set_rect(self.x, self.y, self.width, self.height)

    def shoot(self):
        return Projectile(self.x + 15, self.y, self.cannon.rotation, power=5)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.cannon.draw(screen, self.tank_adapter)
        self.draw_health_bar(screen)
