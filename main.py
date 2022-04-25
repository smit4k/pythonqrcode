# Must have qrcode pip library installed. (pip install qrcode)

import qrcode

txt = input("Enter text here:")
img = qrcode.make(txt)
img.save(f'{txt}.jpg')