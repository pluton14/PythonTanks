from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def set_clock(self):
        pass

    @abstractmethod
    def set_screen(self, width: int, height: int):
        pass

    @abstractmethod
    def my_flip(self):
        pass

    @abstractmethod
    def my_time(self, ms: int):
        pass

    @abstractmethod
    def set_image(self, file: str):
        pass

    @abstractmethod
    def set_rect(self, x: int, y: int, width: int, height: int):
        pass

    @abstractmethod
    def set_square(self, screen, x: int, y: int, size_x: int, size_y: int, color: tuple[int, int, int]):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def wait(self, fps: int):
        pass