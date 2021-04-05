from anki_connect import invoke
from scraper import get_definition
from utils import get_words


def make_note(front, back):
    note = {
        "deckName": "GRE Vocab",
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back
        },
        "options": {
            "allowDuplicate": False,
            "duplicateScope": "deck"
        },
    }
    return note


notes = []
rejected_words = []

words = get_words()
for i, word in enumerate(words):
    if i == 60:
        break
    if words == '':
        continue
    try:
        definition = get_definition(word)
        if type(definition) is dict:
            print(word)
            print(definition)
            rejected_words.append(word)
        else:
            notes.append(make_note(word, definition))
    except KeyError as e:
        print(word)
        print(e)
        rejected_words.append(word)

result = invoke('addNotes', notes=notes)
result = [result_card for result_card in result if result_card is not None]
print(len(result), 'cards were added')

with open('rejected.txt', 'a') as f:
    f.writelines([line + '\n' for line in rejected_words])
with open('word_list.txt', 'w'):
    pass

if __name__ == '__main__':
    pass
