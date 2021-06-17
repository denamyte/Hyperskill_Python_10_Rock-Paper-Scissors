class RPS:
    dependency_list = ['rock', 'paper', 'scissors']

    def __init__(self):
        pass

    def cheat_move(self):
        user_choice = input()
        i = self.dependency_list.index(user_choice)
        win_index = (i + 1) % len(self.dependency_list)
        print(f'Sorry, but the computer chose {self.dependency_list[win_index]}')


RPS().cheat_move()
