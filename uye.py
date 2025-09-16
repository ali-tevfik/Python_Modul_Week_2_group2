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

# ------------------ KİTAP İŞLEMLERİ ------------------
def kitaplari_listele():
    kitaplar = json_oku(KITAP_DOSYA)
    if not kitaplar:
        print("Kayıtlı kitap yok.\n")
        return

    print("\n--- KİTAPLAR ---")
    for k in kitaplar:
        try:
            print(f"Barkod: {k['Barkod']}, Ad: {k['Kitap_Adi']}, Yazar: {k['Yazar']}, "
                  f"Yayinevi: {k['Yayinevi']}, Fiyat: {k['Fiyat']} TL, Dil: {k['Dil']}")
        except KeyError as e:
            print(f"Uyarı: Eksik alan {e} olan kitap atlandı: {k}")
    print()

def kitap_ekle():
    kitaplar = json_oku(KITAP_DOSYA)
    try:
        barkod = int(input("Barkod: "))
    except ValueError:
        print("Geçersiz barkod! Sayı olmalı.\n")
        return
    if any(k['Barkod'] == barkod for k in kitaplar):
        print("Bu barkod zaten mevcut!\n")
        return

    dil = input("Dil: ")
    try:
        fiyat_input = input("Fiyat: ").replace(',', '.')
        fiyat = float(fiyat_input)
    except ValueError:
        print("Geçersiz fiyat! Sayı girin.\n")
        return

    ad = input("Kitap adı: ")
    yayinevi = input("Yayınevi: ")
    yazar = input("Yazar: ")

    kitaplar.append({
        "Barkod": barkod,
        "Dil": dil,
        "Fiyat": fiyat,
        "Kitap_Adi": ad,
        "Yayinevi": yayinevi,
        "Yazar": yazar
    })
    json_yaz(KITAP_DOSYA, kitaplar)
    print(f"{ad} başarıyla eklendi.\n")

def kitap_ara():
    kitaplar = json_oku(KITAP_DOSYA)
    ad = input("Aranacak kitap adı: ")
    bulunan = [k for k in kitaplar if ad.lower() in k["Kitap_Adi"].lower()]
    if bulunan:
        for k in bulunan:
            try:
                print(f"Barkod: {k['Barkod']}, Ad: {k['Kitap_Adi']}, Yazar: {k['Yazar']}, "
                      f"Yayinevi: {k['Yayinevi']}, Fiyat: {k['Fiyat']} TL, Dil: {k['Dil']}")
            except KeyError as e:
                print(f"Uyarı: Eksik alan {e} olan kitap atlandı: {k}")
    else:
        print("Kitap bulunamadı.\n")

def kitap_sil():
    kitaplar = json_oku(KITAP_DOSYA)
    try:
        barkod = int(input("Silinecek kitabın barkod numarası: "))
    except ValueError:
        print("Geçersiz barkod! Sayı olmalı.\n")
        return
    yeni = [k for k in kitaplar if k["Barkod"] != barkod]
    if len(yeni) < len(kitaplar):
        json_yaz(KITAP_DOSYA, yeni)
        print(f"Barkod {barkod} olan kitap silindi.\n")
    else:
        print("Kitap bulunamadı.\n")
