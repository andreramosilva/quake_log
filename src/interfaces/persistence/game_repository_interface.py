from abc import ABC, abstractmethod
from src.app.entities.game import Game

class GameRepositoryInterface(ABC):
    @abstractmethod
    def save(self, game: Game):
        pass

    @abstractmethod
    def get_all(self) -> list[Game]:
        pass
