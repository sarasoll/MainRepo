from tkinter import image_names
import pyqrcode as qr
url ="https://github.com/sarasoll"
image_name="qr.png"
QR=qr.create(url)
size=13
QR.png(image_name,scale=size)