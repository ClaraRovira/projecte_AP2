from catan_game.player import Player
from catan_game.board import Board
from config import *
from typing import Union

class Game:
    def __init__(self, board: Board, players: dict[Player], path_price: int, city_price: int, destruction_price: int):
        self.board = board
        self.players = players
        self.num_players = len(self.players)
        self.path_price = path_price
        self.city_price = city_price
        self.destruction_price = destruction_price
        self.game_over = True
        self.player_turn = 1

    def is_game_over(self) -> bool:
        return self.game_over
    
    def check_players_turn(self, player_id: int) -> bool:
        turn = self.player_turn % self.num_players
        if turn == 0:
            turn = self.num_players
        return turn == player_id

    def is_valid_action(self, player_id: int, action: str, coordinates: Union[Path, Coord]) -> bool:
        valid_action = True
        if self.check_players_turn(player_id):
            if action ==  "build city":
                if self.check_available_resources(player_id, self.city_price) & self.check_if_player_can_build_city(player_id, coordinates):
                    return True
                else: return False
            elif action == "build path":
                if self.check_available_resources(player_id, self.path_price) & self.check_if_player_can_build_path(player_id, coordinates):
                    return True
                else: return False
            elif action == "destroy city":
                if self.check_available_resources(player_id, self.destruction_price) & self.check_if_player_can_destroy_city(player_id, coordinates):
                    return True
                else: return False
            else: 
                print("Unknown action")
        else: valid_action = False
        return valid_action

    def get_board_cell_numbers(self) -> list[list[int]]:
        return self.board.get_board_status()
    
    def get_board_sizes(self) -> tuple[int, int]:
        return self.board.board_sizes
    
    def get_players_colors(self) -> dict:
        players_colors = {}
        for player in self.players.values():
            players_colors[player.id] = {'color': player.get_rgb_color()}
        return players_colors
    
    def get_players_paths(self) -> dict[int, list[Path]]:
        players_paths = {}
        for player in self.players.values():
            players_paths[player.id] = player.paths 
        return players_paths
    
    def get_players_cities(self) -> dict[int, list[Coord]]:
        players_cities = {}
        for player in self.players.values():
            players_cities[player.id] = player.cities 
        return players_cities

    def build_city(self, player_id: int, city_coord: Coord) -> None:
        if self.is_valid_action(player_id, "build city", city_coord):
            self.pick_up_resources(player_id)
            self.players[player_id].save_city(city_coord) 
            self.board.build_city(player_id, city_coord)
        else:
            print("Invalid action")
        self.player_turn += 1

    def build_path(self, player_id: int, path_coords: Path) -> None:
        if self.is_valid_action(player_id, "build path", path_coords):
            self.pick_up_resources(player_id)
            self.board.build_path(player_id, path_coords)
            self.players[player_id].save_path(path_coords) 
        else:
            print("Invalid action")
        self.player_turn += 1

    def destroy_city(self, player_id: int, destruct_coords: Coord) -> None:
        if self.is_valid_action(player_id, "destroy city", destruct_coords):
            self.pick_up_resources(player_id)
            self.board.destroy_city(player_id, destruct_coords)
            self.players[player_id].destroy_city(destruct_coords) 
        else:
            print("Invalid action")
        self.player_turn += 1

    def pick_up_resources(self, player_id: int):
        # TODO: Add one unit per each unique cell that touches a city from the corresponding player_id
        pass

    def check_available_resources(self, player_id: int, prices: int) -> bool:
        # TODO: Check if player have enough resources to take the corresponding action
        return True

    def check_if_city_node_available(self, player_id: int, city_node: Coord) -> bool:
        # TODO: Check if node is available to construct a city
        return True

    def check_if_path_nodes_available(self, player_id: int, path_coord: Path) -> bool:
        # TODO: Check if node is available to construct a city
        return True
    
    def check_if_player_can_build_city(self, player_id: int,  city_coord: Coord) -> bool:
        # TODO: Check if player have permissions according to the game rules to build a city in the given coordinates
        if self.check_if_city_node_available(player_id, city_coord):
            return True
        else: return False
    
    def check_if_player_can_build_path(self, player_id: int, path_coord: Path) -> bool:
        if self.check_if_path_nodes_available(player_id, path_coord):
            # TODO: Check if player have permissions according to the game rules to build a path in the given coordinates
            return True
        else: return False

    def check_if_player_can_destroy_city(self, player_id: int, path_coord: Path) -> bool: 
        # TODO: Check if city exists from this player id
        return True

    def get_game_status(self):
        pass

