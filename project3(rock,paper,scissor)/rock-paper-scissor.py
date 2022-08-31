import random

while True:

    def play():

        user = input("whats your choice ? 'r' for rock, 'p' for paper ,'s' s for scissor :\n")

        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return 'It\'s a tie'
        if is_win(user, computer):
            return 'you won'
        else:
            return 'you lost'


    def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
                (player == 'p' and opponent == 'r'):
            return True


    print(play())

    koko = input('resume or stop:\n')
    if koko == "stop":
        break