from random import choice

__author__ = "LYK 2018 DJANGO"
__license__ = "MIT License"
__version__ = "1.0.0"

class Possibility:
    """
        This module functions returns head or tail, rock or paper or scissors,
        dice or roll. It depends on what you want.
        Usage:
            dice_roll(numbers of dice)
            head_tail()
            rock_paper_scissors()

    """
    def dice_roll(self, how_many_dice):
        """
            Calculation of dice probabilities
        """
        dice = ["yek", "dü", "se", "çehar", "penç", "şeş"]
        list_dice_probability = []
        for i in range(how_many_dice):
            list_dice_probability.append(choice(dice))
        return list_dice_probability

    def head_tail(self):
        """
		  Head or Tail
	    """
        return choice(["Head", "Tail"])

    def rock_paper_scissors(self):
        """
            Classic rock-paper-scissors for 2 people
        """
        first_person = choice(["Rock", "Paper", "Scissors"])
        second_person = choice(["Rock", "Paper", "Scissors"])
        return print("First Person  : {}\nSecond Person : {}".format(first_person, second_person))
