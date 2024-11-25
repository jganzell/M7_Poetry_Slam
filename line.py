"""
Jolie Ganzell
CSCI 3725
M7 - Poetry Slam
21 November, 2024

File containing a class for a Line object. 
Dependencies: pronouncing, spacy
"""

import pronouncing
import spacy
nlp = spacy.load("en_core_web_sm")

class Line:
    """
    Line class: a line that makes up a poem.

    Parameters: line

    Methods: get_words(), get_line(), estimate_syllables(), count_syllables()
        determine_stress_pattern()
    """

    def __init__(self, line):
        """
        A line that makes up a poem.

        Args:
        - line (str): a string of words that are in the line
        """
        self.words = nlp(line)
        self.line = line

    def get_words(self):
        """
        Returns: the words in the line as tokens
        """
        return self.words
    
    def get_line(self):
        """
        Returns: the words in the line as a string
        """
        return self.line
    
    def estimate_syllables(self, word):
        """
        Estimates the number of syllables in a word. Used only for unknown
        words that will cause count_syllables() to crash.
        
        Args:
        - word (str): a word that is unknown to the pronouncing dictionary

        Returns: the number of vowels in a word
        """
        vowels = "aeiouy"
        return sum(1 for char in word if char.lower() in vowels)

    def count_syllables(self):
        """
        Calculates the number of syllables in a line.

        Returns: the number of syllables in a line
        """
        spec_chars = [';', ':', '!', "?", ".", ",", "$",
                      "%", "/", '"', "-", "'", "_"]
        no_spec_char = ''.join(i for i in self.line if not i in spec_chars)

        syllable_count = 0
        for p in no_spec_char.split():
            phones = pronouncing.phones_for_word(p)
            if phones:
                syllable_count += pronouncing.syllable_count(phones[0])
            else:
                syllable_count += self.estimate_syllables(p)
        return syllable_count
    
    def determine_stress_pattern(self):
        """
        Determines the stress pattern of the line. 

        Returns: a string of 1s and 0s, where a 1 represents a stressed
        syllable, and a 0 represents an unstressed syllable
        """
        spec_chars = [';', ':', '!', "?", ".", ",", "$",
                      "%", "/", '"', "-", "'", "_"]
        no_spec_char = ''.join(i for i in self.line if not i in spec_chars)
        print(no_spec_char.split())
        phones = [pronouncing.phones_for_word(p)[0] for p in no_spec_char.split()]
        stresses = [pronouncing.stresses(p) for p in phones]
        pattern = ''
        for s in stresses:
            pattern += s
        return pattern
    
    def __str__(self):
        to_print = []
        for token in self.words:
            to_print.append(token)
        return(str(to_print))
    