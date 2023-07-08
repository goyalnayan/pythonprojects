# Simple QR code
import qrcode as qr
img = qr.make("https://www.youtube.com/@nayangoyal28")
# this link will be generated into QR code
img.save("nayangoyal_youtube.png")



# Advance QR code
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,
                   border=40)
qr.add_data("https://www.w3resource.com/python-exercises/python-basic-exercises.php")
qr.make(fit=True)
img = qr.make_image(fill_color="orange", back_color="black")
img.save("w3resources_website.png")