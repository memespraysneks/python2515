from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import random

class SecretWord:
    def __init__(self, word=""):
        if not word or type(word) is not str:
            with open(word, "r") as f:
                lines = f.readlines()
                choice = random.choice(lines)
                self.word = choice.strip().upper()
        else:
            self.word = word.upper()
    
    def show_letters(self, letters):
        answer = []
        for i in range(len(letters)):
            letters[i] = letters[i].upper()
        for letter in self.word.upper():
            if letter in letters:
                answer += letter.upper()
            else:
                answer += "_"
        return " ".join(answer)
    
    def check_letters(self, letters):
        return "_" not in self.show_letters(letters)


    def check(self, guess):
        return self.word == guess.upper()

class Game:
    def __init__(self, turns=10):
        self.turns = turns
        self.secret_word = SecretWord()
        self.letters = []
    
    def play_one_round(self):
        success = 0
        while success == 0:
            guess = input("What would you like to guess?")
            if guess.isalpha() == True:
                if len(guess) == 1 and guess.upper() not in self.letters:
                    self.letters.append(guess.upper())
                    self.secret_word.show_letters(self.letters)
                    self.turns -= 1
                    return self.secret_word.check_letters(self.letters)
                elif len(guess) == 1:
                    pass
                else:
                    self.turns -= 1
                    return self.secret_word.word == guess.upper()
            else:
                print("You can't guess that try again")

    def play(self):
        while self.turns != 0:
            if self.play_one_round() == True:
                print("You won!")
                return True

            
        if self.turns == 0 and self.play_one_round() == False:
            print("You lose!")