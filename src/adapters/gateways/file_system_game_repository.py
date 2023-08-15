from src.interfaces.persistence.game_repository_interface import GameRepositoryInterface
from src.adapters.gateways.file_system_gateway import FileSystemGateway
from src.app.entities.game import Game

class FileSystemGameRepository(GameRepositoryInterface):
    def __init__(self, file_path):
        self.file_system_gateway = FileSystemGateway(file_path)
        self.games = []

    def save(self, game: Game):
        self.games.append(game)

    def get_all(self) -> list[Game]:
        return self.games
