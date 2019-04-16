# Takes in review and convert it to json file, download album art from link

import json
import argparse

def text_to_json(remove, file_path):

    try:
        data = {}

        with open(file_path, 'r', encoding='utf8') as text_data:
            text_data = text_data.readlines()
        
        for line in text_data:
            if len(line.strip()) == 0:
                continue
            print(line.strip())

        print(data)

    except IOError:
        print('Could not find file \'%s\'' % file_path)

def main():
    parser = argparse.ArgumentParser(description='Convert review to json format')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove files being converted when done. Does not remove the file if there was an error during conversion')
    parser.add_argument('-f', '--files', required=True, nargs='+', help='files to be converted')
    args = parser.parse_args()

    remove = args.remove
    files = args.files

    for file_path in files:
        text_to_json(remove, file_path)

main()