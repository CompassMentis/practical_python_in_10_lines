"""
Same idea as dice_rolls.py, but
as a command line script

Call with:

python dice_rolls.py 5

to roll the dice five times
"""

import random
import argparse


def main():
    parser = argparse.ArgumentParser(description='Role some dice')
    parser.add_argument('number_of_rolls', type=int, metavar='How many rolls?', choices=range(1, 10))
    args = parser.parse_args()
    for i in range(args.number_of_rolls):
        print(f'Roll {i + 1}: {random.randint(1, 6)}')


main()
