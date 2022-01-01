import qrcode
try:
    data = input('Enter the data to be encoded: ')
    if len(data) == 0:
        data = 'https://www.youtube.com/channel/UCxro6LYOp3pmmuWDPMg-p1Q'
except:
    print('Error: Invalid input')

qr = qrcode.QRCode( version = 1, box_size = 15, border = 5)

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('./qrcode/qrcode.png')
