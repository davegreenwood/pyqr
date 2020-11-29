import pyqrcode

s = "hello, world"

code = pyqrcode.create(s)
code.png('img/qr.png', scale=10)
