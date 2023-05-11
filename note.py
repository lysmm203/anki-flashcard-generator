import genanki
from vocabulary import Vocabulary

class Note:
    def __init__(self, vocabulary):
        self.note_css = """
                .card{
                    text-align: center;
                    font-size: 30px;
                }
                """

        self.note_model = genanki.Model(
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
            css=self.note_css
        )
        self.anki_note = None
        self.vocabulary = vocabulary

    def create_note(self):
        formatted_answer = self.vocabulary.definition + '; ' + self.vocabulary.synonyms

        self.anki_note = genanki.Note(
            model = self.note_model,
            fields=[self.vocabulary.word, formatted_answer]
        )