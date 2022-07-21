from PIL import Image

img = Image.open("image.png")
px = []
for pixel in range(img.width):
    prePx = img.getpixel((pixel, 0))[2]
    if prePx == 255:
        a = False
        y = 1
        while not a:
            px1 = img.getpixel((pixel, y))[2]
            y = y + 1
            if px1 != 255:
                px.append(px1 + 255 * (y-2))
                a = True
    else:
        px.append(img.getpixel((pixel, 0))[2])

rs = ''.join(map(chr, px))
#for bytes in range(len(px)):
    #rs = rs + str(px[bytes], 'UTF-8')

print(rs)