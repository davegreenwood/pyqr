import pyqrcode

url = "https://davegreenwood.github.io/pyqr/"
code = pyqrcode.create(url)
code.png('img/qr.png', scale=10)
