
#███▀▀██▀▀███        ▀███▀▀▀██▄  ▀███▀   ▀███▀
#█▀   ██   ▀█         ██    ██    ██       █
#     ██     ███▀██▄  ██    ██    ██       █
#     ██    ███   ██  ██▀▀▀█▄▄    ██       █
#     ██        ▄▄██  ██    ▀█    ██       █
#     ██     ▄▄█▀     ██    ▄█    ██▄     ▄█
#   ▄████▄  █████████ ███████      ▀██████▀▀
import random
import math
from PIL import Image

def split_str(s):
    return [c for c in s]

rg = input("Text to encrypt: ")

preBytes = bytes(rg, 'UTF-8')

img_data = []
preBbytes = split_str(rg)
bBytes = []
for a in range(len(preBbytes)):
    bBytes.append(ord(preBbytes[a]))

x = 0
for byte in range(len(bBytes)):
    if bBytes[byte] < 256:
        color = (random.randint(1,255), random.randint(1,255), bBytes[byte])
        img_data.append((x, 0, color))
    else:
        c = math.ceil(bBytes[byte]/255)
        f = math.floor(bBytes[byte]/255)
        colorMain = bBytes[byte]-255*f
        y = 0
        for a in range(f):
            color = (random.randint(1, 255), random.randint(1, 255), 255)
            img_data.append((x, y, color))
            y = y+1
        color = (random.randint(1, 255), random.randint(1, 255), colorMain)
        img_data.append((x, c, color))
    x = x + 1
img = Image.new('RGB', (len(bBytes), math.ceil(max(bBytes)/255)+1), color='white')
for d in img_data:
    img.putpixel((d[0], d[1]), d[2])


img.save("image.png")
print("Success!")
