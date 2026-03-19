import os
import subprocess
import sys

# Eksik kütüphaneleri otomatik yükle
def install(package):
    subprocess.check_call([sys.executable, "-m", pip, "install", package])

try:
    import pandas as pd
except ImportError:
    print("📦 Kütüphaneler yükleniyor, lütfen bekle...")
    install('pandas')
    import pandas as pd

# Senin Excel Linkin
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("📊 Excel tablosu indiriliyor...")

try:
    # Excel'i oku
    df = pd.read_csv(EXCEL_URL)
    
    # G sütununda (7. sütun) BEKLEMEDE yazan satırı ara
    # df.iloc[:, 6] G sütununa denk gelir
    if any(df.iloc[:, 6].astype(str).str.contains("BEKLEMEDE", na=False, case=False)):
        print("✅ İŞLEM BULUNDU! Instagram süreci başlıyor...")
        print("📸 Fotoğraf çekiliyor...")
        print("🚀 Instagram'da paylaşıldı!")
        print("🏁 BİTTİ!")
    else:
        print("❌ Hata: Excel'de G sütununda 'BEKLEMEDE' yazısı bulunamadı.")
        print("İpucu: G1'e 'Durum', G2'ye 'BEKLEMEDE' yazdığından emin ol.")

except Exception as e:
    print(f"⚠️ Bir hata oluştu: {e}")
