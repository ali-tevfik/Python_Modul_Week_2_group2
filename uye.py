import sqlite3
import json
import os

# ---------------------------
# Veritabanı Bağlantısı
# ---------------------------
def baglanti():
    return sqlite3.connect("kutuphane.db")

# ---------------------------
# Tablo Oluşturma
# ---------------------------
def tablolar_olustur():
    conn = baglanti()
    cursor = conn.cursor()

    # Üyeler tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS uyeler (
        id INTEGER PRIMARY KEY,
        ad TEXT NOT NULL,
        tel TEXT,
        adress TEXT
    )
    """)

    # Kitaplar tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kitaplar (
        id INTEGER PRIMARY KEY,
        ad TEXT NOT NULL
    )
    """)

    # Emanetler tablosu
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emanetler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uye_id INTEGER,
        kitap_id INTEGER,
        FOREIGN KEY (uye_id) REFERENCES uyeler(id),
        FOREIGN KEY (kitap_id) REFERENCES kitaplar(id)
    )
    """)

    # Eğer eski uyeler tablosu varsa eksik sütunları ekle
    try:
        cursor.execute("ALTER TABLE uyeler ADD COLUMN tel TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        cursor.execute("ALTER TABLE uyeler ADD COLUMN adress TEXT")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()

# ---------------------------
# JSON'dan Veri Yükleme
# ---------------------------
def jsondan_veri_yukle():
    if not os.path.exists("uye.json"):
        print("⚠️ uye.json bulunamadı, veri yüklenmedi.")
        return

    with open("uye.json", "r", encoding="utf-8") as f:
        uyeler = json.load(f)

    conn = baglanti()
    cursor = conn.cursor()

    for u in uyeler:
        try:
            cursor.execute(
                "INSERT INTO uyeler (id, ad, tel, adress) VALUES (?, ?, ?, ?)",
                (u["id"], u["uye_adi"], str(u["tel"]), u["adress"])
            )
        except sqlite3.IntegrityError:
            # Aynı ID varsa hata verme
            pass

    conn.commit()
    conn.close()
    print("✅ uye.json'daki üyeler yüklendi.")

# ---------------------------
# Üye İşlemleri
# ---------------------------
def uye_ekle(ad, tel, adress):
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO uyeler (ad, tel, adress) VALUES (?, ?, ?)", (ad, tel, adress))
    conn.commit()
    conn.close()
    print(f"✅ Üye eklendi: {ad}")

def uye_ara(kelime):
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM uyeler WHERE ad LIKE ?", (f"%{kelime}%",))
    sonuc = cursor.fetchall()
    conn.close()
    return sonuc

def uye_sil(uye_id):
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM uyeler WHERE id=?", (uye_id,))
    conn.commit()
    conn.close()
    print(f"🗑️ {uye_id} ID'li üye silindi.")

def uyeleri_listele():
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM uyeler")
    uyeler = cursor.fetchall()
    conn.close()
    return uyeler

# ---------------------------
# Emanet İşlemleri
# ---------------------------
def kitap_ver(uye_id, kitap_id):
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emanetler WHERE kitap_id=?", (kitap_id,))
    if cursor.fetchone():
        print("⚠ Bu kitap zaten ödünç verilmiş!")
    else:
        cursor.execute("INSERT INTO emanetler (uye_id, kitap_id) VALUES (?, ?)", (uye_id, kitap_id))
        conn.commit()
        print("✅ Kitap ödünç verildi.")
    conn.close()

def kitap_iade(kitap_id):
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emanetler WHERE kitap_id=?", (kitap_id,))
    conn.commit()
    conn.close()
    print("✅ Kitap iade edildi.")

def kitap_takibi():
    conn = baglanti()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT uyeler.ad, uyeler.tel, kitaplar.ad
    FROM emanetler
    JOIN uyeler ON emanetler.uye_id = uyeler.id
    JOIN kitaplar ON emanetler.kitap_id = kitaplar.id
    """)
    kayitlar = cursor.fetchall()
    conn.close()

    return kayitlar

# ---------------------------
# Menü41
# ---------------------------
def menu():
    tablolar_olustur()
    jsondan_veri_yukle()

    while True:
        print("\n Lütfen Yapmak istediğiniz seçimin kodunu giriniz.")
        print("-  ÜYELER            = 1             =   KİTAP ÖDÜNÇ VERME = 5")
        print("-  ÜYE EKLE          = 2             =   KİTAP İADE        = 6")
        print("-  ÜYE ARA           = 3             =   KİTAP TAKİBİ      = 7")
        print("-  ÜYE SİL           = 4             =   ÇIKIŞ             = 0")
        print("--------------------------------------")

        secim = input("Seçiminiz: ")

        if secim == "1":
            for u in uyeleri_listele():
                print(f"{u[0]} - {u[1]} | Tel: {u[2]} | Adres: {u[3]}")

        elif secim == "2":
            ad = input("Üye adı: ")
            tel = input("Telefon: ")
            adress = input("Adres: ")
            uye_ekle(ad, tel, adress)

        elif secim == "3":
            kelime = input("Aranacak kelime: ")
            for u in uye_ara(kelime):
                print(f"{u[0]} - {u[1]} | Tel: {u[2]} | Adres: {u[3]}")

        elif secim == "4":
            uye_id = int(input("Silinecek üye ID: "))
            uye_sil(uye_id)

        elif secim == "5":
            uye_id = int(input("Üye ID: "))
            kitap_id = int(input("Kitap ID: "))
            kitap_ver(uye_id, kitap_id)

        elif secim == "6":
            kitap_id = int(input("İade edilecek kitap ID: "))
            kitap_iade(kitap_id)

        elif secim == "7":
            kayitlar = kitap_takibi()
            for k in kayitlar:
                print(f"{k[0]} ({k[1]}) → {k[2]}")

        elif secim == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    menu()
