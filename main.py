import qrcode
qr = qrcode.QRCode()
qr.add_data('https://www.youtube.com/channel/UCLJiABSd-uulY0TNv1wLJaA')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="pink")

img.save('qrcode.png')