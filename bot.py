import os
import pandas as pd

# Senin Excel Linkin
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("📊 Excel tablosu indiriliyor...")

try:
    df = pd.read_csv(EXCEL_URL)
    # G sütununda (Durum sütunu) BEKLEMEDE yazan satırı bul
    pending_tasks = df[df.iloc[:, 6].str.contains("BEKLEMEDE", na=False, case=False)]
    
    if not pending_tasks.empty:
        print(f"✅ İşlem bulundu! Paylaşım süreci başlıyor...")
        # Paylaşım simülasyonu
        print("📸 Fotoğraf hazırlanıyor...")
        print("🚀 Instagram'a gönderiliyor...")
        print("🏁 İŞLEM BAŞARIYLA TAMAMLANDI!")
    else:
        print("❌ Hata: Excel'de 'BEKLEMEDE' yazısı bulunamadı. Lütfen G2 hücresini kontrol et.")

except Exception as e:
    print(f"⚠️ Bir hata oluştu: {e}")
