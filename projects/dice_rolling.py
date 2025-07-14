import random


class Dice:
    def roll(self):
        dice1 = random.randint(0, 6)
        dice2 = random.randint(0, 6)
        final_result = (dice1, dice2)
        return final_result


rolled_dice = Dice()
print(rolled_dice.roll())
