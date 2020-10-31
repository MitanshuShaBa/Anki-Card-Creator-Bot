from anki_connect import invoke


def make_note(word):
    front = word
    back = 'back content'  # TODO: scraped meaning goes here
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

result = invoke('addNotes', notes=notes)
print(result)
