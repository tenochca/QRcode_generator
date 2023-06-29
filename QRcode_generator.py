import qrcode

data = 'Hello!'

img = qrcode.make(data)

img.save('C:/Users/tenoc/Pictures/Camera Roll/myqrcode.png')
