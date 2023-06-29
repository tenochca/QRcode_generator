import qrcode

data = 'Hello!'

qr = qrcode.QRCode(version = 2, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red', back_color = 'green')

img.save('C:/Users/tenoc/Pictures/Camera Roll/myqrcode2.png')
