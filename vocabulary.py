import requests
from bs4 import BeautifulSoup
from helpers import definition_cleanup

class Vocabulary:
    def __init__(self, word):
        self.word = word
        self.soup = None
        self.definition = None
        self.synonyms = None

    def get_soup(self):
        response = requests.get(f'https://www.merriam-webster.com/dictionary/{self.word}')
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_definition(self):
        definition_div = self.soup.findAll(class_=['sb-0', 'sb-entry'])

        for div in definition_div:
            if div.find(class_='dtText'):
                definition = div.find(class_='dtText').text
                break

        definition_cleaned = definition_cleanup(definition)
        self.definition = definition_cleaned

    def get_synonyms(self):
        synonym_table = self.soup.find(class_='mw-grid-table-list')
        synonyms = []

        try:
            synonym_list = synonym_table.find_all('li')
        except:
            synonyms.append(" ")
        else:
            for synonym in synonym_list:
                synonyms.append(synonym.text)

        synonym_string = ', '.join(synonyms)

        self.synonyms = synonym_string