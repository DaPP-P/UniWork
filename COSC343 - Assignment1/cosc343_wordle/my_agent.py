__author__ = "Daniel Prvanov"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "prvda311@otago.student.ac.nz"

import numpy as np
import re
from helper import *
from collections import Counter

class WordleAgent():
    """
       A class that encapsulates the code dictating the
       behaviour of the Wordle playing agent

       ...

       Attributes
       ----------
       dictionary : list
           a list of valid words for the game
       letter : list
           a list containing valid characters in the game
       word_length : int
           the number of letters per guess word
       num_guesses : int
           the max. number of guesses per game
       mode: str
           indicates whether the game is played in 'easy' or 'hard' mode

       Methods
       -------
       AgentFunction(percepts)
           Returns the next word guess given state of the game in percepts
       """

    def __init__(self, dictionary, letters, word_length, num_guesses, mode):
        """
      :param dictionary: a list of valid words for the game
      :param letters: a list containing valid characters in the game
      :param word_length: the number of letters per guess word
      :param num_guesses: the max. number of guesses per game
      :param mode: indicates whether the game is played in 'easy' or 'hard' mode
      """

        self.dictionary = dictionary
        self.letters = letters
        self.word_length = word_length
        self.num_guesses = num_guesses
        self.mode = mode

    #def most_common_word(List):
    #    occurence_count = Counter(List)
    #   return occurence_count

    def AgentFunction(self, percepts):
        """Returns the next word guess given state of the game in percepts

      :param percepts: a tuple of three items: guess_counter, letter_indexes, and letter_states;
               guess_counter is an integer indicating which guess this is, starting with 0 for initial guess;
               letter_indexes is a list of indexes of letters from self.letters corresponding to
                           the previous guess, a list of -1's on guess 0;
               letter_states is a list of the same length as letter_indexes, providing feedback about the
                           previous guess (conveyed through letter indexes) with values of 0 (the corresponding
                           letter was not found in the solution), -1 (the correspond letter is found in the
                           solution, but not in that spot), 1 (the corresponding letter is found in the solution
                           in that spot).
      :return: string - a word from self.dictionary that is the next guess
      """

        # This is how you extract three different parts of percepts.
        guess_counter, letter_indexes, letter_states = percepts
        # Here's where you should put in your code
        if guess_counter == 0:
            self.possible_words = list(self.dictionary)
            word_index = np.random.randint(0, len(self.possible_words)) # selects a random word for the list of possible words
        else:
            for indexes, states in zip(letter_indexes, letter_states):
                if states == 0: # checks if the state is equal to zero
                    i = self.letters[indexes] # gets the char of item that has state zero
                    num = word_to_letter_indices(i, self.letters) # converts the char to a number value
                    num = num[0]
                    count = letter_indexes.count(num) # finds how many times char is present
                    if count == 1:
                        string_possible_words = ' '.join(self.possible_words)
                        words_to_remove = re.findall(rf'\w*{i}\w*', string_possible_words) #f inds all words that contain this char
                        for word in list(words_to_remove):
                            self.possible_words.remove(word) # removes words that contain the wrong char once
                if states == -1: #if states is equal to -1
                    i = self.letters[indexes] #gets the char of item that has state zero
                    num = word_to_letter_indices(i, self.letters) # converts the char to a number value
                    num = num[0]
                    count = letter_indexes.count(num)
                    num_index = (letter_indexes.index(num)) # finds the index position of the char
                    string_words = ' '.join(self.possible_words)
                    words_to_keep = re.findall(rf'\w*{i}\w*', string_words) # finds all words that contain i
                    if count != 1:
                        self.possible_words = words_to_keep # if the char appears more than once, ignore indexing
                    else:
                        res = [idx for idx in words_to_keep if idx[num_index] == i]
                        remove_list = [word for word in words_to_keep if word not in res] # finds words that have the letter in the same index as the guess word
                        self.possible_words = remove_list # removes the words from above from self.possible_words
                if states == 1: #if states = one
                    i = self.letters[indexes] #gets the char of item that state zero
                    num = word_to_letter_indices(i, self.letters) #converts the char to a number value
                    num = num[0]
                    num_index = (letter_indexes.index(num)) #finds the index position of the char
                    count = letter_indexes.count(num)
                    string_words = ' '.join(self.possible_words)
                    words_to_keep = re.findall(rf'\w*{i}\w*', string_words)  # finds all words that contain i
                    if count != 1:
                        res = words_to_keep
                    else:
                        res = [idx for idx in words_to_keep if idx[num_index] == i] # finds words that have the letter in the same index as the guess word
                    self.possible_words = res


            string_words = ' '.join(self.possible_words)
            keys = [k for k, value in Counter(string_words).most_common()] # finds the most common character in the words
            k = (keys[0])
            random_select = re.findall(rf'\w*{k}\w*', string_words) # finds all words that contain the most common character
            word_index = np.random.randint(0, len(random_select)) # randomly selects a word that contains the most common character

        return self.possible_words[word_index]
