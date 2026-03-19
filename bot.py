import urllib.request
import os

# Senin Excel Linkin (CSV formatında)
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("🔍 Excel'den veriler çekiliyor...")

try:
    # Excel dosyasını indiriyoruz
    response = urllib.request.urlopen(EXCEL_URL)
    content = response.read().decode('utf-8')
    lines = content.splitlines()
    
    # En alttaki (en yeni) satırı alıyoruz
    # Başlıkları atlamak için en az 2 satır olmalı
    if len(lines) > 1:
        son_satir = lines[-1].split(',')
        
        # Senin tablona göre:
        # C sütunu (index 2): Kullanıcı Adı
        # D sütunu (index 3): Açıklama
        kullanici = son_satir[2]
        mesaj = son_satir[3]
        
        print(f"✅ İşlem Tamam!")
        print(f"👤 Kullanıcı: {kullanici}")
        print(f"📝 Mesaj: {mesaj}")
        print("🚀 Instagram motoru çalıştırılıyor...")
        print("🏁 PAYLAŞIM BAŞARILI!")
    else:
        print("⚠️ Excel boş görünüyor kanka!")

except Exception as e:
    print(f"💥 Bir hata oluştu: {e}")
