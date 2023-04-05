#Implement the code of LSB steganography in RGB image.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.asarray(Image.open('RGB.jpg'))
W,H,C = img.shape

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
encoded_img = img.reshape((W,H,C))

form_img = Image.fromarray(encoded_img)
form_img.save("RGBO.jpg")