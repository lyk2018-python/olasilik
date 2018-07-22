from random import choice

class Possibility:
    """
        This module functions returns head or tail, rock or paper or scissors,
        dice or roll. It depends on what you want.
        Usage:
            dice_roll()
            head_tail()
            rock_paper_scissors()

    """
    def dice_roll(self):
        return choice(range(6))
    def head_tail(self):
        return choice(["Head", "Tail"])
    def rock_paper_scissors(self):
        return choice(["Rock", "Paper", "Scissors"])
