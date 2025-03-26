import qrcode

# Create a QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Define the vCard data
vcard = """BEGIN:VCARD
VERSION:4.0
FN:Erhan BARAN
ORG:Erhan BARAN
TITLE:CEO
TEL;TYPE=WORK,VOICE:(555) 555-5555
EMAIL;TYPE=PREF,INTERNET:john.smith@example.com
URL:https://www.linkedin.com/in/erhan-baran/
END:VCARD"""

# Add the vCard data to the QR code object
qr.add_data(vcard)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code_vcard.png")