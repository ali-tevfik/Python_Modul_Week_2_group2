import json
import os

UYE_DOSYA = "uye.json"
KITAP_DOSYA = "kitap.json"

# ------------------ DOSYA OLUŞTURMA ------------------
def dosya_olustur(dosya):
    if not os.path.exists(dosya):
        with open(dosya, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

dosya_olustur(UYE_DOSYA)
dosya_olustur(KITAP_DOSYA)

# ------------------ JSON İŞLEMLERİ ------------------
def json_oku(dosya):
    """Dosyayı oku ve liste döndür. Bozuk veya string elemanları temizle."""
    with open(dosya, "r", encoding="utf-8") as f:
        try:
            veri = json.load(f)
        except json.JSONDecodeError:
            print(f"{dosya} okunamadı veya bozuk!")
            return []
    
    temiz_veri = []
    if isinstance(veri, list):
        for k in veri:
            if isinstance(k, dict):
                temiz_veri.append(k)
            elif isinstance(k, str):
                try:
                    k = json.loads(k)
                    if isinstance(k, dict):
                        temiz_veri.append(k)
                except json.JSONDecodeError:
                    continue
    return temiz_veri

def json_yaz(dosya, veri):
    """Veriyi JSON olarak dosyaya yazar."""
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=4, ensure_ascii=False)

# ------------------ ÜYE İŞLEMLERİ ------------------
def uyeleri_listele():
    uyeler = json_oku(UYE_DOSYA)
    print("\n--- ÜYELER ---")
    if not uyeler:
        print("Kayıtlı üye yok.\n")
        return
    for u in uyeler:
        print(f"ID: {u['id']}, Ad: {u['uye_adi']}, Tel: {u['tel']}, Adres: {u['adress']}")
    print()

def uye_ekle():
    uyeler = json_oku(UYE_DOSYA)
    try:
        id_no = int(input("Üye ID: "))
    except ValueError:
        print("Geçersiz ID! Sayı olmalı.\n")
        return
    isim = input("Üye adı: ")
    try:
        tel = int(input("Telefon: "))
    except ValueError:
        print("Geçersiz telefon numarası! Sadece sayı girin.\n")
        return
    adres = input("Adres: ")
    uyeler.append({"id": id_no, "uye_adi": isim, "tel": tel, "adress": adres})
    json_yaz(UYE_DOSYA, uyeler)
    print(f"{isim} başarıyla eklendi.\n")

def uye_ara():
    uyeler = json_oku(UYE_DOSYA)
    isim = input("Aranacak üye adı: ")
    bulunan = [u for u in uyeler if isim.lower() in u["uye_adi"].lower()]
    if bulunan:
        for u in bulunan:
            print(f"ID: {u['id']}, Ad: {u['uye_adi']}, Tel: {u['tel']}, Adres: {u['adress']}")
    else:
        print("Üye bulunamadı.\n")

def uye_sil():
    uyeler = json_oku(UYE_DOSYA)
    try:
        id_no = int(input("Silinecek üye ID: "))
    except ValueError:
        print("Geçersiz ID! Sayı olmalı.\n")
        return
    yeni = [u for u in uyeler if u["id"] != id_no]
    if len(yeni) < len(uyeler):
        json_yaz(UYE_DOSYA, yeni)
        print(f"ID {id_no} silindi.\n")
    else:
        print("Üye bulunamadı.\n")

