import requests
import json
from utils import format_json
from config import app_id, app_key, language


def get_definition(word):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word.lower()

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    json_content = r.json()
    # For logging
    if __name__ == '__main__':
        with open('sample_file.json', 'w') as f:
            json.dump(json_content, f, indent=2)

    if 'error' in json_content:
        # print('error')
        return {'error': 'word not found'}
    else:
        back_content = format_json(json_content)
        # print(back_content)
        return back_content


if __name__ == '__main__':
    print(get_definition('Fervent'))

