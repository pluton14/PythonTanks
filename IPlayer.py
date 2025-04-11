from abc import ABC, abstractmethod
from IControl import IControl
from nowTank import Tank
from projectile import Projectile
from environment import Environment


class IPlayer(ABC):

    @abstractmethod
    def action(self, now_control: IControl, tank: Tank, tank2: Tank, projectile: Projectile, env: Environment, state: bool) -> {Projectile, bool, Environment}:
        pass
