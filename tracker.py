import math


class StatisticsTracker:

    def __init__(self, nameOne, nameTwo):
        self.nameOne = nameOne
        self.nameTwo = nameTwo
        self.games = 0
        self.exes = 0
        self.wins = 0
        self.draws = 0

    def recordGame(self, ex, win):
        self.games += 1
        if ex:
            self.exes += 1
        if ex and win == 1:
            self.wins += 1
        elif win == 0.5:
            self.draws += 1

    def printReport(self):
        print
        print 'In this session, there were {} games played.'.format(self.games)
        print '{} player played EX\'s {}% of the time.'.format(
            self.nameOne, float(self.exes) / self.games)
        print '{} player won {}% of the time.'.format(
            self.nameOne, float(self.wins) / self.games)
        print '{} player drew {}% of the time.'.format(
            self.nameOne, float(self.draws) / self.games)
        print 'This resulted in a total win percentage of {}%'.format(
            (self.wins + self.draws * 0.5) / self.games)
        print 'Thank you for using our evaluation tool.'
        print
