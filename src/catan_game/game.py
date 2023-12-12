from catan_game.player import Player
from catan_game.board import Board

class Game:
    def __init__(self, board: Board, players: list[Player], path_price: int, city_price: int, destruction_price: int):
        self.board = board
        self.players = players
        self.num_players = len(self.players)
        self.path_price = path_price
        self.city_price = city_price
        self.destruction_price = destruction_price
        self.game_over = True

    def is_game_over(self) -> bool:
        return self.game_over
    
    def get_board_cell_numbers(self) -> list[list]:
        return self.board.cell_numbers
    
    def get_board_sizes(self) -> tuple:
        return self.board.board_sizes
    
    def get_players_colors(self) -> dict:
        players_colors = {}
        for player in self.players:
            players_colors[player.id] = {'color': player.get_rgb_color()}
        return players_colors
    
    def get_players_paths(self):
        players_paths = {
                            1: [[1, 2], [1, 3]],
                            2: [[4, 5], [4, 6]],
                            3: [[6, 2], [6, 3]],
                        }
        return players_paths
    def get_players_cities(self) -> dict:
        players_cities = {
                            1: [[1, 2]],
                            2: [[4, 5]],
                            3: [[6, 2]],
                        }
        return players_cities

    def get_game_status(self):
        print(self.board.board_sizes)
        print(self.board.cell_numbers)
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

    def destroy_city(player_id, destruct_coords):
        print(player_id)
        print(destruct_coords)
        pass
