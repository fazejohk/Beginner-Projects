#!/usr/bin/env python

import sys
import random

# The extended, cool rules:
# http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock
CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

RULES = {
    'rock': {
        'scissors': 'blunts',
        'lizard': 'crushes'},
    'paper': {
        'rock': 'covers',
        'Spock': 'disproves'},
    'scissors': {
        'paper': 'cuts',
        'lizard': 'decapitates'},
    'lizard': {
        'paper': 'eats',
        'Spock': 'poisons'},
    'Spock': {
        'rock': 'vaporizes',
        'scissors': 'smashes'}
}


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    @classmethod
    def create(cls, num):
        name = raw_input('What shall we call player {}? '.format(num))
        return cls(name)

    def go(self):
        return random.choice(CHOICES)

    def scored(self):
        self.score += 1

    def __str__(self):
        return self.name


def get_winner(players, choices):
    """
    Determine winner of a rock-paper-scissors round.

    Returns a tuple of (winner, winning move) if exists, else None.
    """
    def get_rule(cs):
        return RULES[cs[0]].get(cs[1], None)

    move = get_rule(choices)

    if move is not None:
        winner = players[0]
    else:
        choices = choices[::-1]
        move = get_rule(choices)
        winner = players[1]

    if move is None:
        return None

    return (winner, (choices[0], move, choices[1]))


def game(how_many_rounds):
    if how_many_rounds % 2 == 0:
        raise RuntimeError('Rounds must be an uneven number')

    players = [Player.create(1), Player.create(2)]
    winning_score = how_many_rounds // 2 + 1

    print('Best of {} - let\'s play!\n'.format(how_many_rounds))

    while True:
        choices = [p.go() for p in players]
        for p, c in zip(players, choices):
            print p, c
        win = get_winner(players, choices)

        if win is None:
            print('No winner.\n')
            continue

        winner, move = win
        winner.scored()
        print('{} {} {}. {} won this round.'.format(
                move[0].capitalize(), move[1], move[2], winner))
        for p in players:
            print('{}: {}'.format(p, p.score))

        if winner.score == winning_score:
            break

        raw_input()

    print('The winner was {}!'.format(winner))


def main():
    game(99)


if __name__ == '__main__':
    sys.exit(main())
