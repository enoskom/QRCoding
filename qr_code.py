import qrcode
from qrcode.exceptions import DataOverflowError
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr_code(data, output_filename, box_size=10, border=4):
    try:
        # QR kodu nesnesi oluştur (varsayılan hata düzeltme seviyesi L)
        qr = qrcode.QRCode(
            version=1,  # QR kodu boyutu (başlangıçta 1)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi (L - en düşük)
            box_size=box_size,  # Kutuların boyutu
            border=border,  # Sınır kalınlığı
        )
        
        # QR koduna veri ekle
        qr.add_data(data)
        qr.make(fit=True)

        # QR kodu görselini oluştur (varsayılan renk siyah ve arka plan beyaz)
        img = qr.make_image(fill='black', back_color='white')

        # QR kodunu kaydet
        img.save(output_filename)

        print(f"QR kodu başarıyla '{output_filename}' olarak kaydedildi.")
        img.show()
    except DataOverflowError:
        print("Veri çok büyük, daha düşük hata düzeltme seviyesi seçilmesi gerekebilir veya veriyi kısaltmayı deneyin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def decode_qr_code(input_filename):
    try:
        # Resmi aç
        img = Image.open(input_filename)

        # QR kodunu çöz
        decoded_objects = decode(img)

        # Çözülen QR kodları
        if decoded_objects:
            for obj in decoded_objects:
                print(f"QR kodu verisi: {obj.data.decode('utf-8')}")
        else:
            print("QR kodu tespit edilmedi.")
    except Exception as e:
        print(f"QR kodu çözme sırasında bir hata oluştu: {e}")

# Kullanıcıya seçenekler sun
choice = input("QR kodu üretmek mi yoksa çözmek mi istersin? (yap/çöz): ").lower()

if choice == 'yap':
    # QR kodu oluştur
    user_input = input("QR kodu oluşturmak için bir veri gir (URL, metin vb.): ")
    output_filename = input("QR kodunu kaydetmek için dosya adını gir (örneğin: qrcode.png): ")
    generate_qr_code(user_input, output_filename)
elif choice == 'çöz':
    # QR kodunu çöz
    input_filename = input("Çözmek için bir dosya adı gir (örn. qrcode.png): ")
    decode_qr_code(input_filename)
else:
    print("Geçersiz seçim, lütfen 'yap' veya 'çöz' yaz.")
