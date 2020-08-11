import sys
import os
from PIL import Image

imageFolder = sys.argv[1]
outputFolder = sys.argv[2]

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

for filename in os.listdir(imageFolder):
    img = Image.open(f'./{imageFolder}{filename}')
    clean_name = os.path.splitext(filename)[0]

    img.save(f'{outputFolder}{clean_name}.png', 'png')
    # print('All done!')
