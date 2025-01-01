import json
import os

import parser

configPath = 'config.json'

def main():
    config = load_config()
    stellaris_dir = config['stellarisPath']
    tech_dir = stellaris_dir + '\\common\\technology'
    stellaris_mods_dir = config['modsPath']
    output = {}

    for filename in os.listdir(tech_dir):
        parsed: dict = get_file_parsed(tech_dir, filename)
        if (parsed):
            for key, item in parsed.items():
                output[key] = item

    output_path = 'exported_tech_tree.json'
    with open(output_path, 'w') as json_file:
        json.dump(output, json_file, indent=4)

def load_config():
    try:
        with open(configPath, 'r') as file:
            data = json.load(file)
        print('Config loaded')
        return data
    except FileNotFoundError:
        print('Config file not found, please copy config.json.example and paste as config.json')
    except json.JSONDecodeError:
        print('Config file is invalid')

def get_file_parsed(tech_dir: str, filename: str):
    file_path = os.path.join(tech_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return parser.execute(content)

main()
