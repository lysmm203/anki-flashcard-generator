import csv
from collections import defaultdict
import requests
import genanki
import random
from bs4 import BeautifulSoup

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

    deck_css = """
        .card{
            text-align: center;
            font-size: 30px;
        }
        """

    deck_model = genanki.Model(
        1607393419,
        'GRE_Vocab_Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],
        templates=[
            {'name': 'Card 1',
             'qfmt': '{{Question}}',
             'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'
             }
        ],
        css=deck_css
    )
    response = requests.get(f'https://www.merriam-webster.com/dictionary/determine')
    soup = BeautifulSoup(response.content, 'html.parser')
    definition = soup.find(class_=['sb-0', 'sb-entry']).get_text()
    definition1 = definition.replace('\n', ' ')
    definition2 = definition1[8: -4]
    print('a')



    # for group in columns:
    #     anki_deck = genanki.Deck(
    #         random.randrange(1 << 30, 1 << 31),
    #         'test_deck'
    #     )
    #     for word in columns[group]:
    #         # response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}').json()
    #         definition = response[0]['meanings'][0]['definitions'][0]['definition']
    #         synonym = None
    #         try:
    #             synonym = response[0]['meanings'][0]['synonyms'][0]
    #         finally:
    #             note = genanki.Note(
    #                 model = deck_model,
    #                 fields = [word, f'{definition}; {synonym}']
    #             )
    #         anki_deck.add_note(note)
    #
    #     genanki.Package(anki_deck).write_to_file(f'GRE Vocab Group {group}.apkg')


