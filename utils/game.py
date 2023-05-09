import random

class Hangman():
    def __init__(self) :   
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [letter for letter in random.choice(self.possible_words)]

        self.correctly_guessed_letters = ["_" for letter in self.word_to_find]
        self.wrongly_guessed_letters = []

        self.lives = 5
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        self.letter = input("Please enter a letter: ").lower()
        if self.letter.isalpha() and len(self.letter) == 1:

            if self.letter in self.word_to_find:
                if self.letter in self.correctly_guessed_letters:
                    print("You've already found this letter..")
                else:
                    matched_indexes = []
                    i = 0
                    length = len(self.word_to_find)
                    while i < length:
                        if self.letter == self.word_to_find[i]:
                            matched_indexes.append(i)
                        i += 1
                    for i in matched_indexes:
                        self.correctly_guessed_letters[i]=self.letter
                    self.turn_count += 1
                    print((" ".join(e for e in self.correctly_guessed_letters)).upper())

            else:
                if self.letter not in self.wrongly_guessed_letters:
                    self.wrongly_guessed_letters.append(self.letter)
                    self.lives -= 1
                    self.error_count += 1
                    self.turn_count += 1
                    # print("Wrong letter: ",self.wrongly_guessed_letters)
                    print("Nope!")
                else:
                    print("You've wrongly guessed this letter before!")
        elif len(self.letter) != 1:
            print("You've entered more than one letter")
        else:
            print("You've entered an unexceptable character..")

    def start_game(self):
        while self.lives > 0:
            self.play()
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            if self.lives ==0:
                self.game_over()
                break

    def game_over(self):
        print("You're out of lives! Game is over..")

    def well_played(self):
        self.word = "".join(self.word_to_find).upper()
        print(f"You found the word: {self.word} in {self.turn_count} turns with {self.error_count} errors!")
        
hangman = Hangman()
hangman.start_game()