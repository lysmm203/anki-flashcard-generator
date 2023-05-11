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
        response = requests.get(f'https://www.merriam-webster.com/dictionary/f{self.word}')
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def get_definition(self):
        definition_div = self.soup.find(class_=['sb-0', 'sb-entry'])
        definition = definition_div.find(class_='dtText').text
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

        self.synonyms = synonyms