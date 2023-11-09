import qrcode

# Input URL
url = input("Enter the URL: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the URL data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="#720000", back_color="transparent")

# Save the image to a file
img.save("qr_code.png")

print("QR code saved as qr_code.png")
