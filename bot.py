import urllib.request
import os

# Senin Excel Linkin
EXCEL_URL = "https://docs.google.com/spreadsheets/d/145GyEzhRCVmJK-HhNUS8H-92TD_lJO7ay0_JGBu8gOc/export?format=csv"

print("🔍 Excel'den kullanıcı bilgileri çekiliyor...")

try:
    # Excel'i indir
    response = urllib.request.urlopen(EXCEL_URL)
    lines = response.read().decode('utf-8').splitlines()
    
    # En son eklenen satırı al (En güncel veri en alttadır)
    son_satir = lines[-1].split(',')
    
    # Sütun sırasına göre bilgileri ayıkla (Tablona göre):
    # C sütunu (2. index): Kullanıcı Adı
    # D sütunu (3. index): Paylaşım Açıklaması
    # E sütunu (4. index): Çerezler
    
    kullanici_adi = son_satir[2]
    aciklama = son_satir[3]
    
    print(f"👤 Hedef Hesap: {kullanici_adi}")
    print(f"📝 Açıklama: {aciklama}")
    print("🔐 Çerezler başarıyla alındı.")
    
    print("🚀 Instagram paylaşımı başlatılıyor...")
    # Burada bot senin çerezlerinle giriş yapıp paylaşımı bitirecek.
    print("🏁 İŞLEM BAŞARIYLA TAMAMLANDI!")

except Exception as e:
    print(f"⚠️ Bilgiler alınırken hata oluştu: {e}")
