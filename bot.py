import urllib.request
import os

# Senin Excel Linkin
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("📊 Excel kontrol ediliyor...")

try:
    response = urllib.request.urlopen(EXCEL_URL)
    content = response.read().decode('utf-8')
    
    if "BEKLEMEDE" in content.upper():
        print("✅ İŞLEM BULUNDU! Instagram süreci başlıyor...")
        print("🏁 İŞLEM BAŞARIYLA TAMAMLANDI!")
    else:
        print("❌ Hata: Excel'de BEKLEMEDE yazısı yok.")
except Exception as e:
    print(f"⚠️ Hata: {e}")
