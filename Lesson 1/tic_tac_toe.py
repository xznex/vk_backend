"""
Домашнее задание к лекции №1
Консольная игра крестики-нолики в виде класса
"""

import sys

WALL = "#############"
PARTITION = "#---+---+---#"


class TicTacGame:
    """
    TicTacGame, в будущем покрытый тестами
    """

    def __init__(self):
        self.board = list(range(1, 10))
        self.win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                                 (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        self.counter = 0

    def show_board(self):
        print(WALL)
        for i in range(3):
            print(f"# {self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]} #")
            if i != 2:
                print(PARTITION)
        print(WALL)

    def validate_input(self, player):
        print("\nВыберите в какую ячейку поставить ваш " + player + " (от 1 до 9, 0 - выход):")
        while True:
            move = input()
            if not move.isdigit() or not 0 <= int(move) <= 9:
                print("Введите пожалуйтса число (от 1 до 9)")
                continue
            move = int(move)
            if move == 0:
                print("Спасибо, что зашли к нам!")
                sys.exit()
            if str(self.board[move - 1]) in 'X0':
                print(f"Ячейка занята {self.board[move - 1]}. Выберите другую")
                continue
            self.board[move - 1] = player
            print()
            return

    def start_game(self):
        print("Have fun!\n")
        player_turn = 'X'
        while True:
            self.show_board()
            self.validate_input(player_turn)
            self.check_winner(player_turn)

            if player_turn == 'X':
                player_turn = '0'
            else:
                player_turn = 'X'

    def check_winner(self, player_turn):
        p_t = player_turn
        self.counter += 1

        for win in self.win_combinations:
            if self.board[win[0] - 1] == p_t and self.board[win[1] - 1] == p_t and self.board[win[2] - 1] == p_t:
                self.show_board()
                print("\n" + player_turn, r"победили!!! \(★ω★)/")
                sys.exit()
        if self.counter == 9:
            self.show_board()
            print("Игра завершилась ничьей. Сыграть еще раз? (Да/Любое другое слово, значющее отказ (не матерное))")
            if input() == "Да":
                self.board = list(range(1, 10))
                self.start_game()
            else:
                print("Пока!")
                sys.exit()


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
