from dotenv import dotenv_values
import json
import os

import parser

envPath = '.env'
output_path = 'exported_tech_tree.json'

def main():
    env = load_env()
    stellaris_path = env['STELLARIS_PATH']
    stellaris_mods_path = env['MODS_PATH']
    tech_dir = env['TECH_DIR']
    output = []

    # Stellaris techs
    print('Processing: Stellaris')
    for filename in os.listdir(stellaris_path + tech_dir):
        file_path = os.path.join(stellaris_path + tech_dir, filename)

        if os.path.isfile(file_path):
            parsed: dict = get_file_parsed(stellaris_path + tech_dir, filename)

            if parsed:
                for key, item in parsed.items():
                    if isinstance(item, dict):
                        item['name'] = key
                        item['mod_name'] = 'Stellaris'
                        output.append(item)
                    else:
                        print(f'Skipping {key}: {item} is not a dictionary.')
    print('Finished processing: Stellaris')

    # Mods techs
    for folder in os.listdir(stellaris_mods_path):
        folder_path = os.path.join(stellaris_mods_path, folder)

        if os.path.exists(folder_path + tech_dir):
            current_mod = load_mod_name(folder_path)
            print('Processing: ' + current_mod)

            for filename in os.listdir(folder_path + tech_dir):
                file_path = os.path.join(folder_path + tech_dir, filename)

                if os.path.isfile(file_path):
                    parsed: dict = get_file_parsed(folder_path + tech_dir, filename)

                    if parsed:
                        for key, item in parsed.items():
                            if isinstance(item, dict):
                                item['name'] = key
                                item['mod_name'] = current_mod
                                output.append(item)
                            else:
                                print(f'Skipping {key}: {item} is not a dictionary.')
            print('Finished processing: ' + current_mod)

    # Export JSON
    with open(output_path, 'w') as json_file:
        json.dump(output, json_file, indent=4)

def load_env():
    data = dotenv_values(envPath)
    print('Enviroment variables loaded')
    return data

def get_file_parsed(tech_dir: str, filename: str):
    file_path = os.path.join(tech_dir, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return parser.execute(content)

def load_mod_name(mod_folder_path: str):
    file_path = os.path.join(mod_folder_path, 'descriptor.mod')
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            parsed = parser.execute(content)
            return parsed['name']

main()
