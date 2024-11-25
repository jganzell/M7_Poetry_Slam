"""
Jolie Ganzell
CSCI 3725
M7 Poetry Slam
21 November, 2024

File containing a class for a Poem object.
Dependencies: line, bs4, requests, pronounciing, os, random, TextBlob, spacy
"""

from line import Line
import bs4
import requests
import pronouncing
import os
import random
from textblob import TextBlob
import spacy
nlp = spacy.load("en_core_web_sm")

class Poem:
    """
    Poem class: a creator of a lymerick poem

    Methods: read_website(), get_user_imput(), make_rhyme_scheme(),
    write_limerick(), generate_line(), save_poem(), evaluate(),
    perform_poem()
    """

    def __init__(self):
        """
        A creator of a lymerick poem, which has a specific syllable counts,
        stress pattern, and rhyme scheme.
        """
        self.lines = []
        self.name = ''
        self.trait = ''
        self.syllable_counts = {1: 8, 2: 8, 3: 5, 4: 5, 5: 8}
        self.stress = {1: '01001001', 2: '01001001', 3: '01001',
                       4: '01001', 5: '01001001'}
        self.rhyme_scheme = {1: '', 2: '', 3: '', 4: '', 5: ''}
        self.insp = ''

    def read_website(self):
        """
        Reads a given website and sets the poem's inspiring set to be the
        text from that website.
        """
        url = f'https://americanliterature.com/childrens-stories/{self.trait}'
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, 'html.parser')
        script = soup.find("div", class_="al-jumbotron")
        script_text = script.get_text(separator="\n").strip()
        self.insp = nlp(script_text)

    def get_user_input(self):
        """
        Gets user input to determine the name of someone they want to roast
        and their favorite childrens story. Sets the poem's name to be the
        name the user wants to roast, and sets the poem's trait based on the
        user's favorite story (to be used in read_website()).
        """
        name = input("Who is the person you would like to roast? ")
        self.name = name

        story = input("What is your favorite childrens story?"+
                      "Please select from: \nThe three little pigs"+
                      "\nLittle red riding hood\nJack and the beans"+
                      "tock\nSnow white\nCinderella\nThe gingerbread"+
                      " man\nHansel and Gretel\nGoldilocks and the "+
                      "three bears\n")
        if ("pig" or "Pig") in story:
            self.trait = "the-three-little-pigs"
        elif ("red" or "Red") in story:
            self.trait = "little-red-riding-hood"
        elif ("beanstalk" or "Beanstalk") in story:
            self.trait = "jack-and-the-beanstalk"
        elif ("white" or "White") in story:
            self.trait = "snow-white"
        elif ("cinderella" or "Cinderella") in story:
            self.trait = "cinderella"
        elif ("gingerbread" or "Gingerbread") in story:
            self.trait = "the-gingerbread-man"
        elif ("hansel" or "Hansel") in story:
            self.trait = "hansel-and-gretel"
        elif ("goldilocks" or "Goldilocks") in story:
            self.trait = "goldilocks-and-the-three-bears"
        else:
            self.trait = "the-three-little-pigs"
        
    def make_rhyme_scheme(self):
        """
        Determines the 'A' and 'B' words in an 'AABBA' rhyme scheme. The 'A'
        words will all rhyme with the inputted name. The 'B' words will all
        rhyme with a random word from the inspiring set.
        """
        self.rhyme_scheme[1] = self.name
        self.rhyme_scheme[2] = self.name
        self.rhyme_scheme[5] = self.name

        word = random.choice(self.insp)
        while not str(word).isalnum():
            word = random.choice(self.insp)
        
        self.rhyme_scheme[3] = str(word)
        self.rhyme_scheme[4] = str(word)

    def write_limerick(self):
        """
        Calls get_iser_input(), read_website(), and make_rhyme_scheme()
        to gather the knowledge needed to write a limerick. Then calls
        generate_line() five times, and adding each line to the poem if it
        has the correct number of syllables and stress pattern.

        Returns: a list of Line objects that fits the requirements of a limerick
        """
        self.get_user_input()
        self.read_website()
        self.make_rhyme_scheme()

        for i in [1, 2, 3, 4, 5]:
            temp_line = self.generate_line(i)
            while ((temp_line.count_syllables() != self.syllable_counts[i])
                   and (temp_line.determine_stress_pattern != self.stress[i])):
                temp_line = self.generate_line(i)
            self.lines.append(temp_line)
        return self.lines

    def generate_line(self, line_num):
        """
        Generates a line based on the word that the line needs to rhyme with.
        
        Args:
        - line_num (int): a number 1, 2, 3, 4, or 5 corresponding to line number

        Returns: a Line object to be used in write_limerick()
        """
        # 1. Chooses a rhyme word (the last word of the line) and determines
        # what part of speech it is.
        target_rhyme = self.rhyme_scheme[line_num]
        rhymes = pronouncing.rhymes(target_rhyme)
        if rhymes:
            rhyme_word = random.choice(rhymes)
            rhyme_doc = nlp(rhyme_word)
            if rhyme_doc[0].pos_ not in ["NOUN", "VERB", "ADJ", "ADV"]:
                rhyme_doc = nlp(target_rhyme)
        else:
            rhyme_word = nlp(target_rhyme)
            rhyme_doc = nlp(rhyme_word)

        # 2. Creates a list of all the possible nouns, verbs, adjectives,
        # and adverbs int he inspiring set.
        nouns = [token.text for token in self.insp if token.pos_ == "NOUN"
                 and str(token).isalnum()]
        verbs = [token.text for token in self.insp if token.pos_ == "VERB"
                 and str(token).isalnum()]
        adjectives = [token.text for token in self.insp if token.pos_ == "ADJ"
                      and str(token).isalnum()]
        adverbs = [token.text for token in self.insp if token.pos_ == "ADV"
                   and str(token).isalnum()]

        nouns = [word.lower() for word in nouns]
        verbs = [word.lower() for word in verbs]
        adjectives = [word.lower() for word in adjectives]
        adverbs = [word.lower() for word in adverbs]

        # 3. Depending on what part of speech the last word in the line is,
        # selects a random sentence structure for the line.
        if line_num == 1:
            nouns = [self.name]

        if rhyme_doc[0].pos_ == "NOUN":
            sentence_structures = [
                f"{random.choice(nouns).capitalize()} {random.choice(verbs).lower()} the {random.choice(adjectives)} {rhyme_word}",
                f"{random.choice(nouns).capitalize()} {random.choice(verbs)} the {rhyme_word}",
                f"The {random.choice(nouns)} {random.choice(verbs)} {rhyme_word}"
            ]
        elif rhyme_doc[0].pos_ == "VERB":
            sentence_structures = [
                f"{random.choice(adverbs).capitalize()}, the {random.choice(nouns)} {rhyme_word}",
                f"A {random.choice(adjectives)} {random.choice(nouns)} will {rhyme_word}",
                f"The {random.choice(nouns)} {rhyme_word}"
            ]
        elif rhyme_doc[0].pos_ == "ADJ":
            sentence_structures = [
                f"{random.choice(nouns).capitalize()} {random.choice(verbs)} the {random.choice(adjectives)} {rhyme_word}",
                f"The {random.choice(nouns)} was {rhyme_word}",
                f"A {random.choice(adjectives)} {random.choice(nouns)} is {rhyme_word}"
            ]
        elif rhyme_doc[0].pos_ == "ADV":
            sentence_structures = [
                f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {rhyme_word}",
                f"{random.choice(nouns).capitalize()} {random.choice(verbs)} {rhyme_word}",
                f"A {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}, {rhyme_word}"
            ]
        else:
            sentence_structures = [
                f"{random.choice(nouns).capitalize()} {random.choice(verbs)} the {random.choice(adjectives)} {rhyme_word}"
            ]

        to_be_line = random.choice(sentence_structures)

        # 4. Returns the chosen line.
        return Line(to_be_line)

    def add_line(self, line):
        """
        Adds a line to the poem if the line has already been created.
        """
        self.lines.append(Line(line))
    
    def save_poem(self):
        """
        Saves the poem as a txt file.
        """
        f = open(self.lines[0].get_line().replace(" ", "_")
                 .replace(",", "") + ".txt", "w")
        f.write(str([line.get_line() for line in self.lines]))
        f.close()

    def evaluate(self):
        """
        Evaluates the poem based on its polarity. A polarity score closer to
        -1 or 1 is prefered.

        Returns: a decimal number ranging from -1 to 1
        """
        testimonial = TextBlob(str([line.get_line() for line in self.lines]))
        return testimonial.polarity

    def perform_poem(self):
        """
        Reads the poem aloud.
        """
        for line in self.lines:
            read_me = ''
            for word in line.get_line():
                read_me += word
            os.system(f"say -v Sandy '{read_me}'")

    def __str__(self):
        to_print = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        for line in self.lines:
            to_print = to_print + line.get_line() + '\n'
        to_print = to_print + "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        return(to_print)
