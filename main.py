import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("https://www.youtube.com/watch?v=wXY3voKbj8M")##paste the link that you want to access through QR Code
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="pink")
img.save("Fun_song.png")