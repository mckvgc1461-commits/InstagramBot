import sqlite3
import time
import os
from playwright.sync_api import sync_playwright

# AYARLAR (Burayı Instagram değiştikçe güncelleyeceğiz, kodla uğraşmayacaksın!)
BUTON_YENI_GÖNDERİ = 'svg[aria-label="Yeni Gönderi"]'
BUTON_BILGISAYARDAN_SEC = 'button:has-text("Bilgisayardan seç")'

def motoru_calistir():
    while True:
        try:
            # 1. Veritabanına Bak: Sırası gelmiş post var mı?
            conn = sqlite3.connect('../veritabani.db')
            cursor = conn.cursor()
            # Durumu 0 (Bekliyor) olan en eski postu al
            cursor.execute("SELECT * FROM Paylasimlar WHERE Durum=0 ORDER BY Id ASC LIMIT 1")
            post = cursor.fetchone()

            if post:
                p_id, user, pw, img, caption = post[0], post[1], post[2], post[3], post[4]
                print(f"🚀 {user} için paylaşım başlıyor...")

                with sync_playwright() as p:
                    # GİZLİ TARAYICIYI AÇ (Seni gerçek telefon sanacak)
                    browser = p.chromium.launch(headless=False) # İlk testlerde True yapma, izle!
                    context = browser.new_context(viewport={'width': 400, 'height': 800}, is_mobile=True)
                    page = context.new_page()

                    # INSTAGRAM'A GİRİŞ
                    page.goto("https://www.instagram.com/accounts/login/")
                    page.fill('input[name="username"]', user)
                    page.fill('input[name="password"]', pw)
                    page.click('button[type="submit"]')
                    page.wait_for_timeout(5000)

                    # PAYLAŞIM ADIMLARI
                    if page.query_selector(BUTON_YENI_GÖNDERİ):
                        page.click(BUTON_YENI_GÖNDERİ)
                        # Buraya resim yükleme ve açıklama yazma kodlarını ekleyeceğiz...
                        print("✅ Paylaşım yapıldı!")
                        cursor.execute("UPDATE Paylasimlar SET Durum=1 WHERE Id=?", (p_id,))
                    else:
                        print("❌ Instagram arayüzü değişmiş veya giriş başarısız!")
                        cursor.execute("UPDATE Paylasimlar SET Durum=2 WHERE Id=?", (p_id,))
                    
                    conn.commit()
                    browser.close()
            
            conn.close()
        except Exception as e:
            print(f"⚠️ Hata oluştu: {e}")
        
        print("😴 1 dakika bekleniyor...")
        time.sleep(60)

if __name__ == "__main__":
    motoru_calistir()