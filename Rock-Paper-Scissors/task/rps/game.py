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

    def set_user_input(self, user_input):
        self.user_input = user_input

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
    rps = RPS()
    rps.set_user_input(input())
    rps.choose_computer_input()
    rps.calc_result()

    print(rps)


gameplay()
