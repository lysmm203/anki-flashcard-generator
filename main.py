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

    deck_css = """
    .card{
        text-align: center;
        font-size: 30px;
    }
    """

    test_model = genanki.Model(
        1607392319,
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

    test_note = genanki.Note(
        model = test_model,
        fields = ['This is a question', 'This is an answer']
    )

    test_deck = genanki.Deck(
        2059400110,
        'test_deck'
    )
    test_deck.add_note(test_note)

    genanki.Package(test_deck).write_to_file('test.apkg')



    print('a')
