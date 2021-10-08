import pyqrcode
import png
from pyqrocode import QRcode
s = "hello.com"
#any thing you enter in 's' it will converted in qr if any problem shows then add .com in last like ashish.com
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)

#best for links
