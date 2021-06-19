import random


class RPS:
    DEPENDENCY_LIST = ['rock', 'paper', 'scissors']
    SIZE = len(DEPENDENCY_LIST)
    STATE_DRAW, STATE_WIN, STATE_LOSE = range(3)
    MESSAGES = {STATE_DRAW: 'There is a draw ({})',
                STATE_WIN: 'Well done. The computer chose {} and failed',
                STATE_LOSE: 'Sorry, but the computer chose {}'}

    def __init__(self):
        self.user_input = ''
        self.comp_input = ''
        self.state = self.STATE_DRAW

    def set_valid_user_input(self, user_input) -> bool:
        if user_input not in self.DEPENDENCY_LIST:
            return False
        self.user_input = user_input
        return True

    def set_user_input(self, user_input):
        self.user_input = user_input

    @staticmethod
    def option_is_valid(option: str):
        return option in RPS.DEPENDENCY_LIST

    def choose_computer_input(self):
        self.comp_input = random.choice(self.DEPENDENCY_LIST)

    def calc_result(self):
        user_ind = self.DEPENDENCY_LIST.index(self.user_input)
        comp_ind = self.DEPENDENCY_LIST.index(self.comp_input)
        self.state =\
            self.STATE_DRAW if user_ind == comp_ind else\
            self.STATE_LOSE if (user_ind + 1) % self.SIZE == comp_ind else\
            self.STATE_WIN

    def __str__(self):
        return self.MESSAGES.get(self.state).format(self.comp_input)


def gameplay():
    while True:
        inp = input()
        if inp == '!exit':
            break
        if not RPS.option_is_valid(inp):
            print('Invalid input')
            continue
        rps = RPS()
        rps.set_user_input(inp)
        rps.choose_computer_input()
        rps.calc_result()
        print(rps)

    print('Bye!')


gameplay()
