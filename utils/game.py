import random

class Hangman():
    def __init__(self) :   
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(self.possible_words))

        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)  # add '_' for each letter of the word_to_find into a list
        self.wrongly_guessed_letters = []

        self.lives = 5
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        """ 
        This method asks the player to enter a letter and checks whether this letter is included in the 'word_to_find'. 
        If so, it changes with the '_' character with the letter.
        """
        self.letter = input("Please enter a letter: ").lower()
        if self.letter.isalpha() and len(self.letter) == 1:   # checks letter is not a non-alphabetical character and not more than one letter.
            if self.letter in self.word_to_find:                
                if self.letter in self.correctly_guessed_letters:
                    print("You've already found this letter..")
                else:
                    for index, letter in enumerate(self.word_to_find): # to find indexes of the letter in word_to_find and change all _ with the letter
                        if letter == self.letter:
                            self.correctly_guessed_letters[index] = self.letter
                    self.turn_count += 1
                    print((" ".join(e for e in self.correctly_guessed_letters)).upper())

                    # matched_indexes = []
                    # i = 0
                    # length = len(self.word_to_find)
                    # while i < length:
                    #     if self.letter == self.word_to_find[i]:
                    #         matched_indexes.append(i)
                    #     i += 1
                    # for i in matched_indexes:
                    #     self.correctly_guessed_letters[i]=self.letter
                    # self.turn_count += 1
                    # print((" ".join(e for e in self.correctly_guessed_letters)).upper())

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
        """
        This method calls;
        - 'play()' until the game is won finding the word correctly or the game is over.
        - 'well_played()' if the word is found before lives are out.
        - 'game_over()' if 5 lives are out.
        """
        while True:
            self.play()
            if '_' not in self.correctly_guessed_letters:
                self.well_played()
                break
            if self.lives == 0 :
                self.game_over()
                break

    def game_over(self):
        """
        This method stops the game when whole 5 lives are out and prints that the game is over.
        """
        word = "".join(self.word_to_find).upper()
        print(f"You're out of lives! Game is over.. The word was {word}")

    def well_played(self):
        """
        This method stops the game when the user find the word correctly and prints word_to_find, turn_count, and error_count.
        """
        word = "".join(self.word_to_find).upper()
        print(f"You found the word: {word} in {self.turn_count} turns with {self.error_count} errors!")
    
    def new_game():
        while True:
            hangman = Hangman() 
            print("\nWelcome to the Hangman Game!!")
            hangman.start_game()
            response = input("Do you want to play again? Y/N : ")
            if response.upper() != "Y":
                print("Exiting..")
                break



if __name__ == "__main__":
    Hangman.new_game()