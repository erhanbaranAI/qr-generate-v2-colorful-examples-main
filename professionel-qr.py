from PIL import Image, ImageOps
import qrcode

# QR kod verisi
data = "https://www.robobax.com/tr"

# QR kod nesnesi oluştur
qr = qrcode.QRCode(
    version=2,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Renkli QR kod üret (mor-siyah uyumu için)
img = qr.make_image(fill_color="#6C00FF", back_color="#FFFFFF").convert("RGBA")

# Logo'yu yükle
logo_path = "logo.png"
logo = Image.open(logo_path).convert("RGBA")

# Logo boyutunu QR kod oranına göre ayarla
img_w, img_h = img.size
logo_size = img_w // 4
logo = logo.resize((logo_size, logo_size))

# Logo etrafına beyaz kenarlık ekle (daha iyi görünüm için)
logo = ImageOps.expand(logo, border=10, fill='white')

# Yeniden boyutlandır (çerçeve sonrası)
logo = logo.resize((logo_size, logo_size))

# Logoyu QR kodun ortasına yerleştir
logo_w, logo_h = logo.size
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
img.paste(logo, pos, mask=logo)

# Görseli kaydet
output_path = "robobaxQR_estetik.png"
img.save(output_path)
