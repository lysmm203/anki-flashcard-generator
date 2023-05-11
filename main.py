import csv
from collections import defaultdict
import requests
import genanki

if __name__ == '__main__':

    with open('GRE_vocabs.csv') as f:
        csv_reader = csv.reader(f)
        first_row = next(csv_reader)
        columns = defaultdict(list)

        for row in csv_reader:
            index = 1
            for word in row:
                if word == "":
                    continue
                columns[index].append(word)
                index += 1

    response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/determination').json()
    definition = response[0]['meanings'][0]['definitions'][0]['definition']

    # There is possibility of no synonyms
    # synonym = response[0]['meanings'][0]['synonyms'][0]

    print('a')
