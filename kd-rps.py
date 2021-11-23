#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    """KD be able to count wins"""
    wins = 0

    def move(self):
        return 'rock'
        self.their_move = random.choice(moves)
        self.my_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


"""KD add random player"""
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


"""KD add human player"""
class HumanPlayer(Player):
    def move(self):
        move = input("Please choose rock, paper, or scissors: ")
        if move in moves:
            return move
        else:
            self.move()

"""KD add reflect player"""
class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = None
    def move(self):
        if self.their_move in moves:
            return self.their_move
        else:
            return self.my_move

"""KD add cycle player"""
class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = None
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        """KD start score"""
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        """KD add way to present score"""
        if beats (move1, move2):
            self.p1.wins += 1
            print(f"Player 1 wins this round! \nScore: {self.p1.wins}" f" to {self.p2.wins}")
        elif beats (move2, move1):
            self.p2.wins +=1
            print(f"Player 2 wins this round! \nScore: {self.p2.wins}" f" to {self.p1.wins}")
        else:
            print(f"It's a tie! \nScore: {self.p1.wins}" f" to {self.p2.wins}")

    def play_game(self):
        print("Game start!")
        numRounds = int(input("How many rounds do you want to play? Enter a whole number: " ))

        for round in range(numRounds):
            print(f"Round {round}:")
            self.play_round()
        print("\n\nGame over!")

        """KD add way to present game score"""
        if self.p1.wins > self.p2.wins:
            print(f"Player 1 wins {self.p1.wins}" f" to {self.p2.wins}!")
        elif self.p2.wins > self.p1.wins:
            print(f"Player 2 wins {self.p2.wins}" f" to {self.p1.wins}!")
        else:
            print(f"It's a tie!  \nScore: {self.p1.wins}" f" to {self.p2.wins}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
