import os
from PIL import Image
files = os.listdir("textures/minecraft_source")
#print(files)   # ['file1.py', 'file2.txt', 'subdir', ...]

for file in files:
    without_extn = os.path.splitext(file)[0]
    img = Image.open("textures/minecraft/"+file)  # or .jpg
    img = img.resize((50, 50), Image.NEAREST)
    img.save("textures/image_test/"+without_extn+".gif")  # Turtle only accepts .gif
