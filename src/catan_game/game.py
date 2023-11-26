from catan_game.player import Player
from catan_game.board import Board

class Game:
    def __init__(self, board, players, path_price, city_price, destruction_price):
        self.board: Board = board
        self.players: list[Player] = players
        self.num_players = len(self.players)
        self.path_price = path_price
        self.city_price = city_price
        self.destruction_price = destruction_price
        self.game_over = True

    def is_game_over(self):
        return self.game_over

    def get_game_status(self):
        print(self.board.board_sizes)
        print(self.board.cells_board)
        print(self.num_players)
        print(self.players)
        print(self.path_price)
        print(self.city_price)
        print(self.destruction_price)
        pass

    def build_city(self, player_id, node_coords):
        print(player_id)
        print(node_coords)
        pass

    def build_path(self, player_id, path_coords):
        print(player_id)
        print(path_coords)
        pass

    def destruct_city(player_id, destruct_coords):
        print(player_id)
        print(destruct_coords)
        pass
