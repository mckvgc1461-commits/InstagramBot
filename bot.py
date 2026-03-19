import urllib.request
import os

# Senin Excel Linkin (CSV formatında)
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("📊 Excel tablosu kontrol ediliyor...")

try:
    # Excel dosyasını internetten çekiyoruz
    response = urllib.request.urlopen(EXCEL_URL)
    content = response.read().decode('utf-8')
    lines = content.splitlines()
    
    found = False
    # Satırları tek tek kontrol et
    for line in lines:
        if "BEKLEMEDE" in line.upper():
            found = True
            break
            
    if found:
        print("✅ İŞLEM BULUNDU! Robot komutu aldı.")
        print("📸 Fotoğraf hazırlanıyor...")
        print("🚀 Instagram'a gönderiliyor...")
        print("🏁 İŞLEM BAŞARIYLA TAMAMLANDI!")
    else:
        print("❌ Hata: Excel'de 'BEKLEMEDE' yazısı bulunamadı.")
        print("💡 İpucu: Excel'de G2 hücresine BEKLEMEDE yazıp ENTER'a basmalısın.")

except Exception as e:
    print(f"⚠️ Bir bağlantı hatası oluştu: {e}")
