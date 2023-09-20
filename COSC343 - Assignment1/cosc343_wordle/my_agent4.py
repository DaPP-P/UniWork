__author__ = "Daniel Prvanov"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "prvda311@otago.student.ac.nz"

import numpy as np
import re
import wordle
from itertools import groupby
from helper import *

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
         word_index = np.random.randint(0, len(self.possible_words))
      else:
         self.confirmed = []
         for indexes, states in zip(letter_indexes, letter_states):
            if states == -1 or states == 1:
               i = self.letters[indexes]
               self.confirmed.append(i)
               print(i, "was added to the confirmed list", self.confirmed)
               self.string_possible_words = ' '.join(self.possible_words)
               words_to_keep = re.findall(rf'\w*{i}\w*', self.string_possible_words)
               #print(words_to_keep)
               ## if word does not contain self.letters[indexes] remove from
               self.possible_words = words_to_keep
            elif states == 0:
               i = self.letters[indexes]
               print("i is", i)
               print("confirmed words are",self.confirmed)
               if i in self.confirmed:
                  break
               else:
                  self.string_possible_words = ' '.join(self.possible_words)
                  words_to_remove = re.findall(rf'\w*{i}\w*', self.string_possible_words)
                  #print(self.possible_words)
                  #print(words_to_remove)
                  for word in list(self.possible_words):
                     if word in words_to_remove:
                        self.possible_words.remove(word)
                  #print(self.possible_words)

         word_index = np.random.randint(0, len(self.possible_words))



      # a good idea to replace this with a better guess based on your code above.
      return self.possible_words[word_index]
