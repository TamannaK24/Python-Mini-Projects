import json
import random

with open('response.json', 'r') as json_data:
    data = json.load(json_data)

if 'results' in data and len(data['results']) > 0:
    random_result = random.choice(data['results'])
    word = random_result.get('word', 'No word found')
    print(word)    

word_arr = list(word)
blank_word = [] 
print(word_arr) 

for _ in range(len(word)):
    blank_word.append('_')
print(blank_word)

while word_arr != blank_word: 
    for i in range(len(word_arr)):
        guess = input("Enter a letter: ")
        if guess == word_arr[i]:
            blank_word[i] = guess
            print(blank_word) 
        else:
            print(blank_word) 
