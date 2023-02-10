from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.asarray(Image.open('1234.jpg'))
plt.imshow(img, cmap='gray')
img
W,H,C = img.shape
W,H,C
message = input()
message += '[END]'
message = message.encode('ascii')
message_bits = ''.join([format(i,'08b') for i in message])
message
message_bits

img = img.flatten()
for idx, bit in enumerate(message_bits):
    val = img[idx]
    val = bin(val)
    val = val[:-1] + bit
    img[idx] = int(val,2)
encoded_img = img.reshape((W,H))

form_img = Image.fromarray(encoded_img)
plt.imshow(form_img, cmap='gray')
form_img.save("data/1234-modified.jpg")

decode_img = encoded_img.flatten()

decode_img

msg = ""
idx = 0
while msg[-5:] != '[END]':
    bits = [bin(i)[-1] for i in img[idx:idx+8]]
    bits = ''.join(bits)
    msg += chr(int(bits,2))
    idx+=8
    if idx > img.shape[0]:
        print("No hidden message")
        break

msg