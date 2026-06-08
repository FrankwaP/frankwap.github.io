import qrcode

url = "https://frankwap.github.io/"
img = qrcode.make(url)
img.save("cv_qr_code.png")
