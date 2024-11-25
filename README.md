# LIFT: Limericks Inspired by Fairy Tales
Jolie Ganzell
CSCI 3725
M7 - Poetry Slam
21 November, 2024

Link to GitHub:

### Description of LIFT
LIFT is a program that creates limericks based on children's stories. A limerick is a type of poem with five lines. The first two lines and the fifth line rhyme, and the third and fourth lines rhyme. Additionally, the lines have 8, 8, 5, 5, and 8 syllables in them, with the eight syllable lines following a "da DUM da da DUM da da DUM" stress pattern and the five syllable lines following a "da DUM da da DUM" stress pattern. LIFT focuses on creating a poem that follows these rigid rhyme scheme, syllable count, and meter patterns. Additionally, limericks are meant to be funny, and are often used as a means of roasting someone, which LIFT achieves by incorprating the name of someone of the user's choice into the poem. LIFT also performs and evaluates the limericks that it creates. LIFT evaluates by giving its poem a polarity score which is represented by a number between -1 and 1. -1 wouuld signify a strongly negative poem, and 1 would signify a stronly positive poem, with a score of 0 representing a neutral poem. A score farther from 0 is considered better, since limericks are supposed to be funny and evoke emotion.

### My story
Fairy tales were a big part of my life growing up. As a child I loved to read, and even before that my parents would often read to my sister and I. As I got a little older, some of my favorite books were adaptations of fairy tales. Now that I am in college, I think less often about these stories that shaped my childhood, but I know they still inspire aspects of my daily life. This is why fairy tales make such great inspiration for limericks. Limericks are meant to be a little silly, meant to be humurous. One way to achieve this is to look back to these less serious childhood stories, and take a more adult spin on them by turning them into ways to roast your friends.

### To run LIFT
Before running LIFT for the first time make sure the required libraries are installed. These include BeautifulSoup, Requests, Pronouncing, TextBlob, and spaCy. To install, run `pip install bs4`, `pip install requests`, `pip install pronouncing`, `pip install textblob`, `pip install spacy`. To run LIFT, run `python3 main.py`. You will then be prompted for input about ther person you want to roast and what your favorite childrens story is, and then a limerick will be generated. After the limerick is generated, you will be prompted about whether you want to save the poem you just generated, and whether you want to replay a file that had been previously generated.

### How this project challenged me
In the beginning, this seemed like a very daunting project, especially given so much freedom to take it in whichever way I wanted, and I was not quite sure how to begin. But in the end, that just made me feel even more accomplished at having made a poetry generator that speaks the poems. I had also never heard of many of the packages that I used in this project, so it was both challenging and fun to be able to explore those. Throughout this assignment, I learned a lot and would probably do it very differently if I were to do it again. One change I would make is that I would use n-grams instead of the fill-in-the-blank method to develop lines. I realised this way too late in the process of the project for me to implement such a big change, so I just thought about how I could do it differently another time.

### My inspiration
As a human, humor is both an important and dificult to understand part of daily life and interacting with other people. As we make computers able to perform more and more human-like tasks, it is becoming more important to talk about how those computers may also develop a sense of humor. This is described in a paper by Cowie (2023), where he talks about how algorithms with a sense of humor had a more positive reception by the user than algorithms without a sense of humor. But Cowie (2023) also describes sitations where users are offput by a funny computer, and less likely to cooperate with it. Both positive and negative outcomes are possible, and it is important to ensure that if it is used in the field of AI, it is properly placed (Cowie, 2023). This complexity helped inspire me to dive into the world of computational humor and experience it myself.
Limericks are effective as a form of poetry because they follow very strict rules. Their meter and rhyme scheme make them easily recognisable and add to their fun, goofy nature. 

### Sources
