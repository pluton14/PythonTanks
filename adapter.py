import pygame
from pygame.time import Clock
from pygame.locals import *
import sys
from IView import IView
from IControl import IControl


class Adapter(IView, IControl):
    __screen: pygame.SurfaceType
    __buttons: dict[str, pygame.Rect] = {}
    _screen: pygame.SurfaceType
    s_width: int
    s_height: int
    __clock: Clock

    def __init__(self) -> None:
        self.__screen = self.set_screen(640, 400)
        pygame.init()
        self.__clock = pygame.time.Clock()

    def set_screen(self, width: int, height: int) -> pygame.SurfaceType | pygame.Surface:
        self.s_width = width
        self.s_height = height
        self.__screen = pygame.display.set_mode((width, height))
        self._screen = self.__screen
        return self.__screen

    def get_screen(self) -> pygame.SurfaceType | pygame.Surface:
        return self.__screen

    def set_clock(self) -> pygame.time.Clock:
        now_clock = pygame.time.Clock()
        return now_clock

    def my_flip(self) -> None:
        pygame.display.flip()

    def my_time(self, ms: int) -> None:
        pygame.time.wait(ms)

    def set_square(self, now_screen: pygame.Surface | pygame.SurfaceType, x: int, y: int, size_x: int, size_y: int, color: tuple[int, int, int]) -> None:
        pygame.draw.rect(now_screen, color, (x, y, size_x, size_y))

    def set_circle(self, img: pygame.Surface | pygame.SurfaceType, x: int, y: int, z: int, color: tuple[int, int, int, int]) -> None:
        pygame.draw.circle(img, color, (x, y), z)

    def set_rect(self, x: int, y: int, width: int, height: int) -> pygame.Rect:
        now_rect = pygame.Rect(x, y, width, height)
        return now_rect

    def get_events(self) -> {list[pygame.event.Event], list[int]}:
        res = pygame.event.get()
        key = []
        cnt = 0
        for event in res:
            # if event.type == QUIT:
            #     self.running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    key.append(1)
                if event.key == K_LEFT:
                    key.append(2)
                if event.key == K_RIGHT:
                    key.append(3)
                if event.key == K_UP:
                    key.append(4)
                if event.key == K_DOWN:
                    key.append(5)
        return res, key

    def set_image(self, file: str) -> pygame.SurfaceType | pygame.Surface:
        now_img = pygame.image.load(file)
        return now_img

    def set_rotate(self, img: pygame.Surface | pygame.SurfaceType, angle: int) -> pygame.Surface | pygame.SurfaceType:
        now_rotated = pygame.transform.rotate(img, angle)
        return now_rotated

    def exit(self) -> None:
        pygame.quit()
        sys.exit()

    def wait(self, fps: int) -> None:
        self.__clock.tick(fps)