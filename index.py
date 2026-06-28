import random
import time
from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self):
        pass

class SimonGame(Game):
    def __init__(self, name):
        super().__init__(name)
        self._sequence = []
        self._score = 0
        self.colors = ["Red", "Blue", "Green", "Yellow"]

    @property
    def score(self):
        return self._score

    def add_color(self):
        color = random.choice(self.colors)
        self._sequence.append(color)

    def show_sequence(self):
        print("\nMemorize the sequence:\n")
        for color in self._sequence:
            print(color)
            time.sleep(1.2)
        print("\n" * 40)

    def get_user_input(self):
        user_input = input("Enter the sequence separated by spaces:\n")
        return user_input.split()

    def check_answer(self, user_answer):
        return user_answer == self._sequence

    def play(self):
        print("=================================")
        print(" Welcome to Simon Memory Game ")
        print("=================================")
        print("\nRemember the color sequence!\n")
        while True:
            print(f"\nLevel: {self._score + 1}")
            self.add_color()
            self.show_sequence()
            user_answer = self.get_user_input()
            if self.check_answer(user_answer):
                print("\nCorrect Answer!")
                self._score += 1
            else:
                print("\nWrong Sequence!")
                print("Game Over!")
                print(f"Final Score: {self._score}")
                break

game = SimonGame("Simon Memory Game")
game.play()