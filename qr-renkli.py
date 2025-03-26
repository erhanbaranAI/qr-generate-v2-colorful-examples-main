import qrcode
from PIL import Image, ImageDraw

# QR kod verisi
data = "https://www.robobax.com/tr"

# QR kodu oluştur
qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# QR kodu siyah-beyaz (grayscale) oluştur
qr_img = qr.make_image(fill_color="black", back_color="white").convert("L")

# Boyutları al
width, height = qr_img.size

# Gradyan renkler (üstten alta geçiş)
gradient_colors = ["#1b1ac2", "#730de1", "#8c09e9", "#c501fc"]

# Gradyan arka plan oluştur
gradient = Image.new("RGB", (width, height), color=0)
draw = ImageDraw.Draw(gradient)

# Geçiş noktaları
segments = len(gradient_colors) - 1
segment_height = height // segments

# Renk geçişlerini hesapla
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

for i in range(segments):
    start_color = hex_to_rgb(gradient_colors[i])
    end_color = hex_to_rgb(gradient_colors[i + 1])
    for y in range(segment_height):
        ratio = y / segment_height
        r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
        g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
        b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
        draw.line(
            [(0, i * segment_height + y), (width, i * segment_height + y)],
            fill=(r, g, b)
        )

# Son gradyanlı QR kodu oluştur
final_img = Image.composite(gradient, Image.new("RGB", (width, height), "white"), qr_img)

# Kaydet
output_path = "robobaxQR_gradyan_custom.png"
final_img.save(output_path)

