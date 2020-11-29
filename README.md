# QR code in python

As an introduction to programming with python, we will learn how to create a Quick Response (QR) code.

## Requirements

The code required is pure python...

1. `python 3`
2. `pyqrcode` <https://github.com/mnooner256/pyqrcode>
3. `pypng`    <https://github.com/drj11/pypng>

and can be installed with pip:

    pip install pyqrcode pypng

## Usage

Producing a QR code is wonderfully compact:

```
import pyqrcode
code = pyqrcode.create("hello, world")
code.png('img/qr.png', scale=10)
```

You can run the example with `python qr.py` which produces this image:

![a qr code](img/qr.png)
