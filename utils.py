def get_words():
    with open('word_list.txt', 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def format_json(json_content):
    back_content = ''

    for result in json_content['results']:
        for lexicalEntry in result['lexicalEntries']:
            for entry in lexicalEntry['entries']:
                for sense in entry['senses']:
                    for definition in sense['definitions']:
                        # print(definition)
                        back_content += definition + '\n'

                    back_content += 'Example:\n'
                    for example in sense['examples']:
                        # print(example['text'])
                        back_content += example['text'] + '\n'

                    back_content += 'Synonym:\n'
                    for synonym in sense['synonyms']:
                        # print(synonym['text'])
                        back_content += synonym['text'] + '\n'
                    # print()
                    back_content += '\n'

    return back_content
