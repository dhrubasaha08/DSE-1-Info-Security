from PIL import Image
import sys
from matplotlib import image
import numpy as np


def encode():
    img = Image.open('/data/1234.jpg')
    data = input("Enter data to be encoded: ")
    if len(data) == 0:
        raise ValueError('Data is empty')
    newimg = image.copy()
    encode_enc(newimg, data)
    new_img_name = input("Enter the name of new image(with extension): ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in iter(newimg.getdata()):
        if (x == w):
            x = 0
            y += 1
        if (x, y) == newimg.size:
            break
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        a = pixel[3]
        val = format(r, '08b')
        val = val[:-1] + str(ord(data[0]) % 2)
        data = data[1:]
        r = int(val, 2)
        if (len(data) == 0):
            newimg.putpixel((x, y), (r, g, b, a))
            break
        val = format(g, '08b')
        val = val[:-1] + str(ord(data[0]) % 2)
        data = data[1:]
        g = int(val, 2)
        if (len(data) == 0):
            newimg.putpixel((x, y), (r, g, b, a))
            break
        val = format(b, '08b')
        val = val[:-1] + str(ord(data[0]) % 2)
        data = data[1:]
        b = int(val, 2)
        if (len(data) == 0):
            newimg.putpixel((x, y), (r, g, b, a))
            break
        newimg.putpixel((x, y), (r, g, b, a))
        x += 1


def decode():
    img = np.asarray(Image.open('data/1234.jpg'))
    data = ''
    imgdata = iter(image.getdata())
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data


def main():
    print("LSB Steganography")
    print("""1. Encode
2. Decode
3. Exit""")
    choice = input("choice: ")
    if choice == str(1):
        encode()
    elif choice == str(2):
        print("Decoded word- " + decode())
    elif choice == str(3):
        sys.exit()
    else:
        print("Invalid option")
        main()


main()
