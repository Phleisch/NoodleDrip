# Shorten file names of emoji pngs to just be their code
import os

images = os.listdir('ios-emojis')

for image in images:

    split_parts = image.split('_')
    code_only = split_parts[len(split_parts) - 1]
    os.rename('ios-emojis/' + image, 'ios-emojis/' + code_only)
