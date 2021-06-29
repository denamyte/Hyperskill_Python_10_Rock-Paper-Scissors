import random
from typing import Dict, List


class RPS:
    DEFAULT_OPTIONS = ['rock', 'paper', 'scissors']
    STATE_DRAW, STATE_WIN, STATE_LOSE = range(3)
    MESSAGES: Dict[int, str] = {STATE_DRAW: 'There is a draw ({})',
                                STATE_WIN: 'Well done. The computer chose {} and failed',
                                STATE_LOSE: 'Sorry, but the computer chose {}'}
    POINTS: Dict[int, int] = {STATE_DRAW: 50,
                              STATE_WIN: 100}
    FILE_NAME = 'rating.txt'

    def __init__(self):
        self._user_name: str = ''
        self._user_rating: int = 0
        self._user_input: str = ''
        self._comp_input: str = ''
        self._state: int = self.STATE_DRAW
        self._options: List[str] = []
        self._half_size = 0
        self._size = 0

    def read_user_name_and_greet(self):
        self._user_name = input('Enter your name: ')
        print(f'Hello, {self._user_name}')

    def read_rating_file(self):
        with(open(self.FILE_NAME, 'r')) as file:
            ratings = {k: int(v) for k, v in (line.split() for line in file.readlines())}
            self._user_rating = ratings.get(self._user_name, 0)

    def read_options(self):
        inp = input()
        self._options = inp.split(',') if inp else self.DEFAULT_OPTIONS[:]
        self._size = len(self._options)
        self._half_size = self._size // 2

    @property
    def user_rating(self):
        return self._user_rating

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, value: str):
        self._user_input = value

    def option_is_valid(self, option: str):
        return option in self._options

    def choose_computer_input(self):
        self._comp_input = random.choice(self._options)

    def calc_result(self):
        user_ind = self._options.index(self._user_input)
        comp_ind = self._options.index(self._comp_input)
        self._state = \
            self.STATE_DRAW if user_ind == comp_ind else \
            self.calc_complex_result(user_ind, comp_ind)

    def calc_complex_result(self, user_ind, comp_ind) -> int:
        diff = comp_ind - user_ind
        if diff < 0:
            diff += self._size
        return self.STATE_LOSE if diff <= self._half_size else self.STATE_WIN

    def update_user_rating(self):
        self._user_rating += self.POINTS.get(self._state, 0)

    def __str__(self):
        return self.MESSAGES.get(self._state).format(self._comp_input)


def gameplay():
    rps = RPS()
    rps.read_user_name_and_greet()
    rps.read_rating_file()
    rps.read_options()
    print("Okay, let's start")

    while True:
        inp = input()
        if inp == '!exit':
            break
        if inp == '!rating':
            print('Your rating:', rps.user_rating)
            continue
        if not rps.option_is_valid(inp):
            print('Invalid input')
            continue
        rps.user_input = inp
        rps.choose_computer_input()
        rps.calc_result()
        rps.update_user_rating()
        print(rps)

    print('Bye!')


gameplay()
