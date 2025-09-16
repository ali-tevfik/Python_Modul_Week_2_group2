import os
import json

DOSYA = "kitap.json"

# ------------------- Temel Fonksiyonlar -------------------

def dosya_kontrol():
    """kitap.json dosyası yoksa oluşturur."""
    if not os.path.exists(DOSYA):
        with open(DOSYA, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

def kitap_oku():
    """kitap.json içeriğini okur ve liste olarak döndürür."""
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

def kitap_yaz(veri):
    """Listeyi kitap.json dosyasına yazar."""
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=4, ensure_ascii=False)

def kitap_ekle():
    kitap_adi = input("kitap adi")
    yazar= input("kitap yazar")
    yayinevi= input("kitap yayinevi")
    dil= input("kitap dil")
    fiyat= input("kitap fiyat")
    barkod= input("kitap barkod")
    veri = kitap_oku()
    for kitap in veri:
        if kitap["Kitap_Adi"].lower() == kitap_adi.lower():
            print(f"⚠️ '{kitap_adi}' zaten kayıtlı.")
            return
    veri.append({
        "Barkod": barkod if barkod else 0,
        "Kitap_Adi": kitap_adi,
        "Yazar": yazar,
        "Yayinevi": yayinevi,
        "Dil": dil,
        "Fiyat": fiyat
    })
    kitap_yaz(veri)
    print(f"✅ '{kitap_adi}' eklendi.")

def kitap_listele():
    veri = kitap_oku()
    for kitap in veri:
        print(f"Kitap ismi {kitap}")

def kitap_sil():
    kitap_adi =input("Silincek kitap adi")
    veri = kitap_oku()
    yeni_veri = [k for k in veri if k["Kitap_Adi"].lower() != kitap_adi.lower()]
    if len(veri) == len(yeni_veri):
        print(f"⚠️ '{kitap_adi}' bulunamadı.")
    else:
        kitap_yaz(yeni_veri)
        print(f"🗑️ '{kitap_adi}' silindi.")

def kitap_ara():
    aranan =input("Arancak kitap adi")
    veri = kitap_oku()
    bulunan = [k for k in veri if k["Kitap_Adi"].lower() == aranan.lower()]
    print(bulunan)

def kitap_guncelle():
    veri = kitap_oku()
    kitap_adi =input("guncellenecek kitap adi")
    bulundu = False
    for kitap in veri:
        if kitap["Kitap_Adi"].lower() == kitap_adi.lower():
            bulundu = True
            break
    if bulundu:
        kitap_yaz(veri)
        print(f"✏️ '{kitap_adi}' güncellendi.")
    else:
        print(f"⚠️ '{kitap_adi}' bulunamadı.")

def kitap_sayisi():
    return len(kitap_oku())

if __name__ == "__main__":
    menu()
