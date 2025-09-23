import turtle as trtl
from time import sleep
from PIL import Image

# Resize image to 50x50
img = Image.open("textures/minecraft/coins.png")  # or .jpg
img = img.resize((50, 50), Image.NEAREST)
img.save("textures/minecraft/coins.gif")  # Turtle only accepts .gif
img = Image.open("textures/minecraft/trees.gif")  # or .jpg
img = img.resize((50, 50), Image.NEAREST)
img.save("textures/minecraft/trees.gif")  # Turtle only accepts .gif
file = "textures/minecraft/"
t = trtl.Turtle()
colors = ["textures/minecraft/coins.gif",file+"grass.gif",file+"trees.gif"]
wn = trtl.Screen()
tiles = ["[R]", "[G]", "[B]"]
player = trtl.Turtle()
player.turtlesize(2)
t.speed(0)
player.goto(0,0)
wn.register_shape("textures/minecraft/grass.gif")
player.shape("circle")

for tile_image in colors:
    wn.register_shape(tile_image)

dummy_map = [["[R]","[G]","[B]"],
             ["[G]","[B]","[R]"],
             ["[B]","[R]","[G]"]]

def square():
    t.seth(0)
    for n in range(4):
        t.fd(50)
        t.rt(90)
    


def render():
    
    for y in range(len(dummy_map)):
        start_y = len(dummy_map)*25 - y*50-25
        for x in range(len(dummy_map[y])):
            start_x = -1*len(dummy_map[y])*25 + x*50+25
            current_tile_color = colors[tiles.index(dummy_map[y][x])]
            t.shape(current_tile_color)
            t.penup()
            t.goto(start_x,start_y)
            t.seth(0)
            t.stamp()
    player.goto(0,0)
            


def main():
    while True:
        render()
        break
    t.goto(100,0)
    t.shape("textures/minecraft/grass.gif")
    t.turtlesize()
    t.turtlesize(3)
    t.stamp()
main()
wn.mainloop()