from config import *

class Board:
    def __init__(self, board_sizes: tuple, init_cell_values: list[list]):
        self.board_sizes = board_sizes 
        self.cell_numbers = init_cell_values 
        self.nodes = {} 

    def get_board_status(self) -> list[list[int]]:
        return self.cell_numbers
    
    def build_city(self, player_id: int, city_coord: Coord) -> None:
        pass

    def build_path(self, player_id: int, path_coord: Path) -> None:
        pass

    def destroy_city(self, player_id: int, city_coord: Coord) -> None:
        pass

    def substract_cells_resources(self, city: Coord) -> None:
        # TODO: Given a city coordinates, substract one unit to the corresponding cells if possible
        pass

    
