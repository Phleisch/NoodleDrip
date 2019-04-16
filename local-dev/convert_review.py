# Takes in review and convert it to json file, download album art from link

import json
import argparse

def text_to_json(remove, file_path):
    data = {}
    album = {}
    review = {}
    songs = {}

    counter = 1

    try:

        with open(file_path, 'r', encoding='utf8') as text_data:
            text_data = text_data.readlines()
        
        for line in text_data:
            line = line.strip()
            if len(line) == 0:
                continue
            
            if counter >= 1 and counter <= 5:
                parts = line.split(': ')
                var_name = parts[0]
                value = parts[1]
                album[var_name] = value

            counter += 1

        review['songs'] = songs
        data['album'] = album
        data['review'] = review

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