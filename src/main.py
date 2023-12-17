from catan_game.player import Player
from catan_game.board import Board
from catan_game.game import Game
from catan_game.observer import Observer
from config import *

def get_input():
    num_players = int(input("Enter number of players: "))
    board_sizes = tuple(map(int, input("Enter board sizes [cols, rows]: ").split()))
    path_price = int(input("Enter path price: "))
    city_price = int(input("Enter city price: "))
    destruction_price = int(input("Enter destruction price: "))
    player_resources = int(input("Enter initial resources: "))

    players = {}
    for i in range(1, num_players + 1):
        player_info = input(f"Enter initial city coordinates and color for player {i} (e.g., 6 5 red): ").split()
        init_city_coords = tuple(map(int, player_info[:-1]))
        player_color = player_info[-1]
        player = Player(player_id=i,player_color=player_color, player_resources=player_resources)
        player.cities = [init_city_coords]
        players[i] = player

    print("Enter initial board cell values:")
    init_cell_values = []
    for i in range(board_sizes[0]):
        row = list(map(int, input().split()))
        init_cell_values.append(row)

    return board_sizes, path_price, city_price, destruction_price, players, init_cell_values

def process_user_input(user_input, game):
    parts = user_input.split()
    if len(parts) >= 4:
        action = parts[2].lower()
        player_id = int(parts[1])
        if action == 'city':
            node_coords = tuple(map(int, parts[3:]))
            game.build_city(player_id, node_coords)
        elif action == 'path':
            s_coords = tuple(map(int, parts[3:5]))
            e_coords = tuple(map(int, parts[5:7]))
            path_coords = (s_coords, e_coords)
            game.build_path(player_id, path_coords)
        elif action == 'destruct':
            destruct_coords = tuple(map(int, parts[3:]))
            game.destroy_city(player_id, destruct_coords)
    elif parts[0] == 'exit':
        game.game_over = True
    else:
        print("Invalid action")

def main():
    #board_sizes, path_price, city_price, destruction_price, players, init_cell_values = get_input()

    # """ Mocked data example
    board_sizes = [8, 6]
    init_cell_values = [
                            [5, 8, 9, 2, 5, 4, 3, 6],
                            [1, 4, 2, 5, 7, 7, 9, 2],
                            [5, 8, 9, 2, 5, 4, 3, 6],
                            [1, 4, 2, 5, 7, 7, 9, 2],
                            [5, 8, 9, 2, 5, 4, 3, 6],
                            [1, 4, 2, 5, 7, 7, 9, 2]
                        ]
    players = {
                1: Player(1,'red', 10), 
                2: Player(2,'green', 10), 
                3: Player(3,'blue', 10)
            }   
    
    path_price = 5
    city_price = 5
    destruction_price = 5

    # """ 

    board = Board(board_sizes, init_cell_values)
    game = Game(board, players, path_price, city_price, destruction_price)
    observer = Observer(game)

    # """ Mocked data example
    game.players[1].cities = [(1, 2), (3, 5)]
    game.players[2].cities = [(4, 5)]
    game.players[3].cities = [(6, 2)]

    game.players[1].paths = [((1, 2), (1, 3)), ((1, 3), (2, 3))]
    game.players[2].paths = [((4, 5), (4, 6))]
    game.players[3].paths = [((6, 2), (6, 3))]

    # """

    observer.obtain_game_info()

    print('Game starts...')
    game.game_over = False
    while not game.is_game_over():
        observer.run_game()
        user_input = input()
        process_user_input(user_input, game)
    
    observer.end_game()

if __name__ == "__main__":
    main()