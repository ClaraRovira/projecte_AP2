import matplotlib.colors as mcolors
from config import *
class Player:
    def __init__(self, player_id: int, player_color: str, player_resources: int):
        self.id = player_id
        self.color = player_color
        self.resources = player_resources
        self.paths: list[Path] = []
        self.cities: list[Coord] = []

    def save_path(self, path: Path) -> None:
        self.paths.append(path)

    def get_paths(self) -> list[Path]:
        return self.paths
    
    def save_city(self, city: Coord) -> None:
        self.cities.append(city)

    def get_cities(self) -> list[Coord]:
        return self.cities

    def destry_city(self, city: Coord) -> None:
        self.cities.remove(city)

    def get_rgb_color(self) -> tuple:
        rgb_tuple = mcolors.to_rgb(self.color)
        rgb_values = tuple(int(val * 255) for val in rgb_tuple)
        return rgb_values

    def get_info(self) -> dict[str, any]:
        player_info = {
            "id": self.id,
            "color": self.color,
            "resources": self.resources,
            "cities": len(self.cities),
            "cities_coord": self.cities,
            "paths": len(self.paths),
            "paths_coord": self.paths,
        }

        return player_info

    def get_num_resources(self) -> int:
        return self.resources

    def get_color(self) -> str:
        return self.color
    
    def decrease_resources(self, value: int) -> None:
        self.resources = self.resources - value

    def increase_resources(self, value: int) -> None:
        self.resources = self.resources + value
