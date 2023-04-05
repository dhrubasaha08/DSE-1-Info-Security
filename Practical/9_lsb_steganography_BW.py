#Implement the code of LSB steganography in black and white image.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img0 = Image.open('BW.png')
img1 = img0.convert('L')
img = np.asarray(img1)

W,H = img.shape

message = input()
message += '[END]'
message = message.encode('ascii')
message_bits = ''.join([format(i,'08b') for i in message])

img = img.flatten()
for idx, bit in enumerate(message_bits):
    val = img[idx]
    val = bin(val)
    val = val[:-1] + bit
    img[idx] = int(val,2)
encoded_img = img.reshape((W,H))

form_img = Image.fromarray(encoded_img)
form_img.save("BWO.png")