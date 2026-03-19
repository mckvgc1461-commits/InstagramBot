import os
import json
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from playwright.sync_api import sync_playwright

def sistemi_baslat():
    # 1. Google Sheets Bağlantısı (Excel'i açar)
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_json = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    
    # Formun bağlı olduğu tablonun adını buraya yaz
    sheet = client.open("Instagram Paylaşım Paneli (Yanıtlar)").sheet1
    veriler = sheet.get_all_records()

    for i, satir in enumerate(veriler, start=2):
        # Sadece "BEKLEMEDE" olanları paylaş
        if satir.get('Durum') == "BEKLEMEDE":
            musteri_user = satir['Instagram Kullanıcı Adı']
            musteri_cerez = satir['Çerez Kodu (Cookie)']
            foto_url = satir['Fotoğrafı Buraya Yükle']
            aciklama = satir['Paylaşım Açıklaması']
            
            print(f"👤 Şu an {musteri_user} hesabı için işlem yapılıyor...")

            # 2. Müşterinin Çerezini Geçici Dosyaya Yaz
            with open("current_session.json", "w") as f:
                f.write(musteri_cerez)

            # 3. Instagram Paylaşım Motoru (Playwright)
            try:
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    # Müşterinin oturumuyla tarayıcıyı açar
                    context = browser.new_context(storage_state="current_session.json")
                    page = context.new_page()
                    
                    page.goto("https://www.instagram.com/")
                    print(f"✅ {musteri_user} olarak giriş yapıldı.")

                    # --- FOTOĞRAFI YÜKLEME ADIMLARI BURAYA GELECEK ---
                    # (Butonlara tıklama, fotoğrafı seçme vs.)
                    
                    browser.close()

                # 4. Excel'i Güncelle (Durumu OK yap)
                sheet.update_cell(i, 6, "OK") # 6. sütun 'Durum' sütunu olmalı
                print(f"✨ {musteri_user} paylaşımı başarıyla tamamlandı!")

            except Exception as e:
                print(f"❌ {musteri_user} paylaşımında hata: {e}")
                sheet.update_cell(i, 6, "HATA")

if __name__ == "__main__":
    sistemi_baslat()
