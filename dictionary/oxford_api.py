import requests
import json
import random

word_bank = [
    'ace', 'apple', 'acrobat', 'abandon', 'ability', 'able', 'above',
    'abroad', 'absence', 'absolute', 'accept', 'accent', 'accompany',
    'account', 'accurate', 'achieve', 'acid', 'active'
]
results = []
source_lang = 'en-us'

# Function to check if a word exists in the Oxford Dictionaries API
def fetch_word_data(word_id):
    base_url = 'https://od-api-sandbox.oxforddictionaries.com/api/v2/entries'
    url = f'{base_url}/{source_lang}/{word_id}'
    headers = {
        'app_id': 'bb4d8317',
        'app_key': '9073493fa8c8db1c41c02017b6aba3cd'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for word '{word_id}': {response.status_code}")
        return None

for word_id in word_bank:
    word_data = fetch_word_data(word_id)
    if word_data:
        results.append(word_data)

if results:
    with open('response.json', 'w') as json_file:
        json.dump({'results': results}, json_file, indent=4)
    print("Data saved to response.json")
else:
    print("No data fetched from the API.")

