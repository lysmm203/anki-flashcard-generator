import genanki



class Deck:
    def __init__(self):
        self.deck_css = """
        .card{
            text-align: center;
            font-size: 30px;
        }
        """

        self.deck_model = genanki.Model(
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
            css=self.deck_css
        )


