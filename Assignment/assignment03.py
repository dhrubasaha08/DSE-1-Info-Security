'''
this is lsb-steganography technique for gray scale image. try to modify it for
RGB image. 'data/1234.jpg' is the path where the image is stored
'''


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.asarray(Image.open('data/1234.jpg'))

#plt.imshow(img, cmap='gray')

W,H = img.shape

#message processing
message = input()
message += '[END]'
message = message.encode('ascii')
message_bits = ''.join([format(i,'08b') for i in message])

#encoding
img = img.flatten()
for idx, bit in enumerate(message_bits):
    val = img[idx]
    val = bin(val)
    val = val[:-1] + bit
    img[idx] = int(val,2)
encoded_img = img.reshape((W,H))

#plotting
form_img = Image.fromarray(encoded_img)
plt.imshow(form_img, cmap='gray')
form_img.save("data/1234-modified.jpg")
