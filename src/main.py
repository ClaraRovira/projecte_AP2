from catan_game.player import Player
from catan_game.board import Board
from catan_game.game import Game
from catan_game.observer import Observer

def get_input():
    num_players = int(input("Enter number of players: "))
    board_sizes = tuple(map(int, input("Enter board sizes (e.g., 8 6): ").split()))
    path_price = int(input("Enter path price: "))
    city_price = int(input("Enter city price: "))
    destruction_price = int(input("Enter destruction price: "))
    player_resources = int(input("Enter initial resources: "))

    players = []
    init_city_coords = {}
    for i in range(1, num_players + 1):
        player_info = input(f"Enter initial city coordinates and color for player {i} (e.g., 6 5 red): ").split()
        init_city_coords[i] = tuple(map(int, player_info[:-1]))
        player_color = player_info[-1]
        player = Player(player_id=i,player_color=player_color, player_resources=player_resources)
        players.append(player)

    print("Enter initial board cell values:")
    init_cell_values = []
    for i in range(board_sizes[0]):
        row = list(map(int, input().split()))
        init_cell_values.append(row)

    return board_sizes, path_price, city_price, destruction_price, players, init_cell_values

def process_user_input(user_input, game):
    # Process user input and update game state
    parts = user_input.split()
    if len(parts) >= 4:
        action = parts[2].lower()
        player_id = int(parts[1])
        if action == 'city':
            node_coords = tuple(map(int, parts[3:]))
            game.build_city(player_id, node_coords)
        elif action == 'path':
            path_coords = tuple(map(int, parts[3:]))
            game.build_path(player_id, path_coords)
        elif action == 'destruct':
            destruct_coords = tuple(map(int, parts[3:]))
            game.destruct_city(player_id, destruct_coords)
        else:
            print("Invalid action")

def main():
    board_sizes, path_price, city_price, destruction_price, players, init_cell_values = get_input()

    board = Board(board_sizes, init_cell_values)
    game = Game(board, players, path_price, city_price, destruction_price)
    observer = Observer(game)

    print('Game starts...')
    game.game_over = False
    
    while not game.is_game_over():
        user_input = input()
        process_user_input(user_input, game)

if __name__ == "__main__":
    main()