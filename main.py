from escpos.printer import Win32Raw

printer_name = "POS-80C"

# Buraya kendi Wi-Fi bilgilerinizi girin
WIFI_SSID = ""
WIFI_PASSWORD = ""

# Telefonların otomatik bağlanması için gereken standart format
wifi_qr_string = f"WIFI:T:WPA;S:{WIFI_SSID};P:{WIFI_PASSWORD};;"

try:
    p = Win32Raw(printer_name)

    # Üst Bilgi Yazıları
    p.set(align='center', double_height=True, double_width=True)
    p.text("KABLOSUZ AG\n")
    p.text("BAGLANTISI\n\n")

    p.set(align='center', normal_textsize=True)
    p.text("Baglanmak icin telefonunuzun\n")
    p.text("kamerasini okutunuz.\n\n")

    # DÜZELTİLEN SATIR: native=False yapıldı ve boyut 6 olarak ayarlandı
    p.qr(wifi_qr_string, ec=0, size=6, model=2, native=False)

    # Alt Bilgi
    p.text("\n\n")
    p.text(f"Ag Adi: {WIFI_SSID}\n")
    p.text("-" * 32 + "\n")
    p.text("Hos Geldiniz!\n\n\n\n")

    # Kağıdı Kes
    p.cut()
    print("Wi-Fi QR kod fişi başarıyla yazdırıldı!")

except Exception as e:
    print(f"Yazıcıya bağlanılamadı veya hata oluştu: {e}")