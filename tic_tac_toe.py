"""
Домашнее задание к лекции №1
Консольная игра крестики-нолики в виде класса
"""

WALL = "#############"
PARTITION = "#---+---+---#"
CROSS = 'X'
TOE = '0'


class TicTacGame:
    """
        Some implementation of TicTacGame
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

    def handing_errors(self, player):
        while True:
            try:
                print("\nВыберите в какую ячейку поставить ваш " + player + " (от 1 до 9, 0 - выход):")
                move = input()
                flag = self.validate_input(move)
                self.board[int(move) - 1] = player

            except TypeError:
                print("\nВведите пожалуйтса число")
                continue
            except IndexError:
                print("\nЧисло должно быть от 0 до 9")
                continue
            except ValueError:
                print("\nЯчейка уже занята. Выберите другую")
                continue
            else:
                return flag

    def validate_input(self, move):
        while True:
            if not move.isdigit():
                raise TypeError

            if not 0 <= int(move) <= 9:
                raise IndexError

            if str(self.board[int(move) - 1]) == 'X' or str(self.board[int(move) - 1]) == '0':
                raise ValueError

            if int(move) == 0:
                print("Спасибо, что зашли к нам!")
                return True

            print()
            return 0

    def start_game(self):
        print("Have fun!\n")
        player_turn = 'X'
        while True:
            self.show_board()

            flag_exit = self.handing_errors(player_turn)

            flag_end = self.check_winner(player_turn)

            if flag_exit or flag_end:
                break

            if player_turn == 'X':
                player_turn = '0'
            else:
                player_turn = 'X'

    def check_winner(self, player_turn):
        self.counter += 1

        for win in self.win_combinations:
            if self.board[win[0] - 1] == player_turn and self.board[win[1] - 1] == player_turn \
                    and self.board[win[2] - 1] == player_turn:
                self.show_board()
                print("\n" + player_turn, r"победили!!! \(★ω★)/" + "\nХотите сыграть еще раз? (Да/Нет)")
                self.decision_to_play()
                return True
        if self.counter == 9:
            self.show_board()
            print("\nИгра завершилась ничьей. Сыграть еще раз? (Да/Любое другое слово, "
                  "значущее отказ (не матерное))")
            self.decision_to_play()
            return True

        return False

    def decision_to_play(self):
        if input() == "Да":
            self.board = list(range(1, 10))
            self.counter = 0
            self.start_game()
        else:
            print("Пока!")


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
