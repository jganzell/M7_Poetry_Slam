"""
Jolie Ganzell
CSCI 3725
M7 - Poetry Slam
21 November, 2024

Main file which writes a limerick, prints it out, performs it, scores
it, offers the user the oportunity to save it, and offers the user the
oportunity to replay an old poem.
Dependencies: Poem, os
"""

from poem import Poem
import os

def main():

    def perform_old_poem():
        """
        Reads a previously written and saved poem aloud.
        """
        filename = input("Please enter the name of the file you would like to replay: ")
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
            content = content[2:-2].split("', '")
            old_poem = Poem()
            for line in content:
                old_poem.add_line(line)
            print(old_poem)
            old_poem.perform_poem()
        else:
            print("File not found.")

    limerick = Poem()
    limerick.write_limerick()
    print(limerick)
    limerick.perform_poem()
    print("Polarity score: ", limerick.evaluate(), "\n")

    save = input("Would you like to save the poem to a file (y/n)? ")
    if save.lower() == 'y':
        limerick.save_poem()
    
    do_perform_old_poem = input("Would you like to replay an old poem (y/n)? ")
    if do_perform_old_poem.lower() == 'y':
        perform_old_poem()

if __name__ == "__main__":
    main()
