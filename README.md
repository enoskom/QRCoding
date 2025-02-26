# QRCoding
QR Code Generator and Decoder

Bu Python projesi, QR kodları oluşturmanızı ve mevcut QR kodlarını çözmenizi sağlar. qrcode ve pyzbar gibi popüler kütüphaneleri kullanarak, QR kodlarını hızlı bir şekilde üretebilir ve çözebilirsiniz. Bu araç, kullanıcıya iki ana seçenek sunar: bir QR kodu oluşturmak veya bir QR kodunu çözmek.
Özellikler

    QR kodu oluşturma: Kullanıcıdan alınan veri ile QR kodu üretilir.
    QR kodu çözme: QR kodu içeren bir görsel dosyasını çözerek, kodun içerdiği veriyi ekrana yazdırır.
    Hata düzeltme seviyesi ve kutu boyutları gibi parametrelerle QR kodu özelleştirilebilir.
    Python qrcode ve pyzbar kütüphanelerini kullanarak hızlı ve güvenilir QR kodu işlemleri.

Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

    qrcode: QR kodları oluşturmak için kullanılır.
    pyzbar: QR kodlarını çözmek için kullanılır.
    Pillow: Görselleri işlemek için kullanılır.

Kütüphaneleri yüklemek için terminalden şu komutları çalıştırabilirsiniz:

pip install qrcode[pil] pyzbar Pillow

Kullanım
QR Kodu Oluşturma

QR kodu oluşturmak için aşağıdaki adımları izleyin:

    QR kodu üretmek mi yoksa çözmek mi istersin? (yap/çöz) sorusuna yap yazın.
    QR kodu için bir veri girin (örneğin, bir URL veya metin).
    QR kodunu kaydetmek için bir dosya adı belirleyin (örneğin, qrcode.png).

QR Kodu Çözme

QR kodunu çözmek için şu adımları izleyin:

    QR kodu üretmek mi yoksa çözmek mi istersin? (yap/çöz) sorusuna çöz yazın.
    Çözmek istediğiniz QR kodu görselinin dosya adını girin (örneğin, qrcode.png).

Örnek

QR kodu oluşturma:

QR kodu üretmek mi yoksa çözmek mi istersin? (yap/çöz): yap
QR kodu oluşturmak için bir veri gir (URL, metin vb.): https://www.example.com
QR kodunu kaydetmek için dosya adını gir (örneğin: qrcode.png): qrcode.png
QR kodu başarıyla 'qrcode.png' olarak kaydedildi.

QR kodu çözme:

QR kodu üretmek mi yoksa çözmek mi istersin? (yap/çöz): çöz
Çözmek için bir dosya adı gir (örn. qrcode.png): qrcode.png
QR kodu verisi: https://www.example.com

Hata Yönetimi

    Veri Çok Büyük: Eğer veri QR koduna sığmazsa, DataOverflowError hatası alınır. Bu durumda, daha düşük hata düzeltme seviyesi seçilebilir veya veri kısaltılabilir.
    QR Kodu Bulunamadı: QR kodu görselinde bir QR kodu tespit edilmezse, "QR kodu tespit edilmedi." mesajı görüntülenir.
    Diğer Hatalar: Çeşitli hatalar için genel bir hata mesajı gösterilir.
