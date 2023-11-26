import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
CELL_SIZE = 50
ROWS = 6
COLS = 8
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 30

# Define the numbers for each cell
board_numbers = [
    [5, 8, 9, 2, 5, 4, 3, 6],
    [1, 4, 2, 5, 7, 7, 9, 2],
    [5, 8, 9, 2, 5, 4, 3, 6],
    [1, 4, 2, 5, 7, 7, 9, 2],
    [5, 8, 9, 2, 5, 4, 3, 6],
    [1, 4, 2, 5, 7, 7, 9, 2]
]

# Define player corresponding colors
players_info = {
    1: {'color': (255, 0, 0)},
    2: {'color': (0, 255, 0)},
    3: {'color': (0, 0, 255)},
}

# Initialize players_paths and players_cities as empty dictionaries
players_paths = {}
players_cities = {}

# Initialize the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Board with Players, Paths, and Cities")

# Function to draw the initial board
def draw_board(numbers):
    # Draw the board and numbers
    for row in range(ROWS + 1):
        for col in range(COLS + 1):
            pygame.draw.circle(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE), 5)

    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            font = pygame.font.Font(None, 36)
            text = font.render(str(numbers[row][col]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
            screen.blit(text, text_rect)


# Function to draw paths
def draw_paths(players_paths):
    for player, path in players_paths.items():
        player_color = players_info[player]['color']
        start_pos = (path[0][1] * CELL_SIZE, path[0][0] * CELL_SIZE)
        end_pos = (path[1][1] * CELL_SIZE, path[1][0] * CELL_SIZE)
        pygame.draw.line(screen, player_color, start_pos, end_pos, 5)

def draw_cities(players_cities):
    for player in players_cities:
        player_color = players_info[player]['color']
        font = pygame.font.Font(None, 36)
        for city in players_cities[player]:
            text = font.render('X', True, player_color)
            text_rect = text.get_rect(center=(city[1] * CELL_SIZE, city[0] * CELL_SIZE))
            screen.blit(text, text_rect)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw initial board
    draw_board(board_numbers)

    # Draw paths on the edges
    draw_paths(players_paths)

    # Draw cities
    draw_cities(players_cities)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

    # User input
    command = input("Enter command (player X city/pc X path/pp X, quit/q): ").lower().split()
    
    if command[0] == 'player' and len(command) >= 4:
        player = int(command[1])
        print(player)
        print(command)
        print(command[2])
        if command[2] == 'city' and len(command) == 5:
            print(command[2])
            row = int(command[3])
            col = int(command[4])
            players_cities.setdefault(player, []).append([row, col])

        elif command[2] == 'path' and len(command) == 7:
            start_row = int(command[3])
            start_col = int(command[4])
            end_row = int(command[5])
            end_col = int(command[6])
            players_paths[player] = [[start_row, start_col], [end_row, end_col]]

    elif command[0] == 'quit' or command[0] == 'q':
        running = False

# Quit Pygame
pygame.quit()
sys.exit()
