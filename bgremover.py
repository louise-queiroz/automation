from sys import argv
from rembg import remove
from PIL import Image

input_path = argv[1]
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

