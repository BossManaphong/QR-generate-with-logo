import qrcode
from PIL import Image

""""
Youtube logo = youtube-logo.png
Github logo = github-logo.png
Thammasat University logo = tu-logo.png
"""
logo = Image.open('logo/tu-logo.png')
url = 'https://cs.sci.tu.ac.th/'

width_height = 125
logo = logo.resize((width_height, width_height))

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    border=1
)
QRcode.add_data(url)
QRcode.make(fit=True)
QRimg = QRcode.make_image(fill_color="black",
                          back_color="white").convert('RGBA')

center = ((QRimg.size[0] - logo.size[0]) // 2,
          (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, center, mask=logo)

QRimg.save('./QRcode/QR-tu.png')
QRimg.show()
