import qrcode

data = 'https://www.google.com/logos/2010/pacman10-i.html' #data to be encoded in the qrcode

qr = qrcode.QRCode(version = 2, box_size = 10, border = 5) #creating a QRCode object and using qrcode method to modify it.

qr.add_data(data) #adding the specified data using add_data function

qr.make(fit = True) #compiles the data into an array. 
#setting fit to true automaticly sized the qr code accordingly

img = qr.make_image(fill_color = 'green', back_color = 'white') #make_image functin specifies color

img.save('C:/Users/tenoc/Pictures/Camera Roll/myqrcode.png') #save the image to designated file path

