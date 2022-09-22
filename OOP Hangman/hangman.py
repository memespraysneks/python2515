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
        pass

    def play(self):
        pass