class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = {34, 0, 23, 9}

    def total(self):
        return sum(self.numbers)


# player1 = LotteryPlayer()
# player2 = LotteryPlayer()

player1 = LotteryPlayer("Bob")

player2 = LotteryPlayer("Jose")
player2.numbers = {30, 28, 55, 2}

# print(player1.name)
# print(player1.numbers)
# print(player1.total())

# print( player1 == player2)
print(player2.name == player1.name)
print(player2.numbers == player1.numbers)