from catan_game.game import Game
from catan_game.board import Board
import pygame
import sys

class Observer:
    def __init__(self, game: Game):
        self.game: Game = game
        self.cell_size = 50
        self.extra_info_width = 200  
        self.rows: int
        self.cols: int
        self.width: int
        self.height: int
        self.fps = 30
        self.screen = None
        self.cell_numbers: list
        self.players_colors = dict
        self.players_paths = dict
        self.players_cities = dict

    def obtain_game_info(self):
        self.cols, self.rows = self.game.get_board_sizes()
        self.width = self.cols * self.cell_size + self.extra_info_width  
        self.height = self.rows * self.cell_size
        self.cell_numbers = self.game.get_board_cell_numbers()

    def draw_board(self, offset_x=0):
        for row in range(self.rows + 1):
            for col in range(self.cols + 1):
                pygame.draw.circle(self.screen, (0, 0, 0), (col * self.cell_size + offset_x, row * self.cell_size), 5)

        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (col * self.cell_size + offset_x, row * self.cell_size, self.cell_size, self.cell_size), 1)
                font = pygame.font.Font(None, 36)
                text = font.render(str(self.cell_numbers[row][col]), True, (0, 0, 0))
                text_rect = text.get_rect(
                    center=(col * self.cell_size + self.cell_size // 2 + offset_x, row * self.cell_size + self.cell_size // 2))
                self.screen.blit(text, text_rect)

    def draw_paths(self, offset_x=0):
        for player, path in self.players_paths.items():
            player_color = self.players_colors[player]['color']
            start_pos = (path[0][1] * self.cell_size + offset_x, path[0][0] * self.cell_size)
            end_pos = (path[1][1] * self.cell_size + offset_x, path[1][0] * self.cell_size)
            pygame.draw.line(self.screen, player_color, start_pos, end_pos, 5)

    def draw_cities(self, offset_x=0):
        for player in self.players_cities:
            player_color = self.players_colors[player]['color']
            font = pygame.font.Font(None, 36)
            for city in self.players_cities[player]:
                text = font.render('X', True, player_color)
                text_rect = text.get_rect(center=(city[1] * self.cell_size + offset_x, city[0] * self.cell_size))
                self.screen.blit(text, text_rect)

    def obtain_game_state(self):
        self.players_colors = self.game.get_players_colors()
        self.players_paths = self.game.get_players_paths()
        self.players_cities = self.game.get_players_cities()

    def display_game_state(self):
        self.screen.fill((255, 255, 255))
        self.draw_players_info()
        self.draw_board(offset_x=self.extra_info_width)
        self.draw_paths(offset_x=self.extra_info_width)
        self.draw_cities(offset_x=self.extra_info_width)

        pygame.display.flip()

    def draw_players_info(self):
        player_info_margin = 20
        player_info_width = self.extra_info_width - 2 * player_info_margin
        total_players = len(self.players_colors)

        available_height = self.height - 2 * player_info_margin
        player_info_height = available_height // total_players

        for i, (player, info) in enumerate(self.players_colors.items()):
            player_color = info['color']

            # Draw player info rectangle
            pygame.draw.rect(self.screen, player_color,
                             (player_info_margin, i * player_info_height + player_info_margin, player_info_width,
                              player_info_height))

            # Draw player text
            font = pygame.font.Font(None, 25)
            text = font.render(f'Player {player}', True, (255, 255, 255))
            text_rect = text.get_rect(
                center=(player_info_margin + player_info_width // 2, i * player_info_height + player_info_margin + player_info_height // 2))
            self.screen.blit(text, text_rect)

    def run_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Number Board with Players, Paths, and Cities")

        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.obtain_game_state()
        self.display_game_state()
        clock.tick(self.fps)

    def end_game(self):
        pygame.quit()
        sys.exit()
