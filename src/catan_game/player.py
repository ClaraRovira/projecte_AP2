import matplotlib.colors as mcolors
class Player:
    def __init__(self, player_id: str, player_color: str, player_resources: int):
        self.id = player_id
        self.color = player_color
        self.resources = player_resources

    def get_player_info(self):
        pass

    def get_num_resources(self) -> int:
        pass

    def get_color(self) -> str:
        pass
    
    def get_rgb_color(self):
        rgb_tuple = mcolors.to_rgb(self.color)
        rgb_values = tuple(int(val * 255) for val in rgb_tuple)
        return rgb_values
    
    def decrease_resources(self, value: int) -> None:
        pass

    def increase_resources(self, value: int) -> None:
        pass
