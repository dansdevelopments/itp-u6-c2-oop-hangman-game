from .exceptions import *


class GuessAttempt(object):
    def __init__(self, letter, hit=None, miss=None):
        if hit == None and miss == None:
            raise InvalidGuessAttempt("Must be a hit OR a miss")
        if hit != None and type(hit) != bool:
            raise InvalidGuessAttempt("hit must be a bool")
        if miss != None and type(miss) != bool:
            raise InvalidGuessAttempt("miss must be a bool")
        if hit and miss:
            raise InvalidGuessAttempt("Can't be a hit AND a miss")
        self.letter = letter
        if hit == None:
            self.miss = miss
            self.hit = not miss
        if miss == None:
            self.hit = hit
            self.miss = not hit

    def is_hit(self):
        return bool(self.hit)

    def is_miss(self):
        return bool(self.miss)
        

class GuessWord(object):
    def __init__(self, answer):
        if type(answer) != str:
            raise InvalidWordException("Word is type {}, must be type str".format(type(answer)))
        if answer == '':
            raise InvalidWordException("Word can't be''")
        self.answer = answer.lower()
        self.masked = "*" * len(answer)

    def perform_attempt(self, letter):
        if type(letter) != str or len(letter) > 1:
            raise InvalidGuessedLetterException("{} is not a valid letter".format(letter))
        lower_letter = letter.lower()
        is_hit = lower_letter in self.answer
        print("is_hit: {}".format(is_hit))
        if is_hit:
            new_masked_word = ""
            ctr = 0
            for char in self.answer:
                if char == lower_letter:
                    new_masked_word += char
                else:
                    new_masked_word += self.masked[ctr]
                ctr += 1
            self.masked = new_masked_word
        attempt = GuessAttempt(letter, hit=is_hit)
        return(attempt)


class HangmanGame(object):
    pass
