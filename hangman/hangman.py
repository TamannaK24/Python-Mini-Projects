import random 


hangman = [
    r"""
    ----
    |  |
       |
       |
       |
  ----------
""",
r"""
    ----
    |  |
    O  |
       |
       |
  ----------
""",
r"""
    ----
    |  |
    O  |
    |  |
       |
  ----------
""",
r"""
    ----
    |  |
    O  |
    |\ |
       |
  ----------
""",
r"""
    ----
    |  |
    O  |
   /|\ |
       |
  ----------
""",
r"""
    ----
    |  |
    O  |
   /|\ |
     \ |
  ----------
""",
r"""
    ----
    |  |
    O  |
   /|\ |
   / \ |
  ----------
""",
]


print("Hello welcome to hangman!")
words = [] 
with open('words.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        words.append(line.strip())

random_word = random.choice(words)
blank_word = []
        
for _ in random_word:
    blank_word.append("_")

print(blank_word) 
random_word = list(random_word)   
word_guessed = False
tries = 0 

while word_guessed != True and tries < 7:
    guess = input("Guess a letter: ").lower().strip()
    if guess in random_word:
      for i, item in enumerate(random_word):
          if random_word[i] == guess:
              blank_word[i] = guess 
      print(blank_word,"\n")
      if random_word == blank_word:
          word_guessed = True
          print(f"You guessed the word! {''.join(random_word)}")
    else:
        tries += 1
        print("Uh oh that was incorrect!")
        print(hangman[tries])
        print(blank_word)
    if tries == 6:
        print(f"Game over. The word was {''.join(random_word)}")
        exit()



