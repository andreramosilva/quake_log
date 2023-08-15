from src.interfaces.persistence.game_repository_interface import GameRepositoryInterface
from src.app.entities.game import Game

class GameRepository(GameRepositoryInterface):
    def __init__(self):
        self.games = []

    def save(self, game: Game):
        self.games.append(game)

    def get_all(self) -> list[Game]:
        return self.games
