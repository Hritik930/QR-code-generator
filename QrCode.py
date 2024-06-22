import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("Hritik Bhai ki jai ho")
myqr1 = qrcode.make("https://www.youtube.com/watch?v=IUQVO97zcE0")

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 87)

b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
