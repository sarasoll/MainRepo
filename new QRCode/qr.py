import os
import qrcode

img = qrcode.make("https://github.com/sarasoll")
img.save("s.png","PNG")
os.system("start s.png")
