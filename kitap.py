# import os
# import json

# # JSON dosyasını oku
# def kitapOku(kitap):
#     """Verilen JSON dosyasını okuyup Python dict olarak döndürür."""
#     with open(kitap, "r", encoding="utf-8") as f:
#         veri = json.load(f)
#     return veri


# oku = kitapOku("kitap.json")

# print(oku)

# # JSON dosyasına yaz

# def json_yaz(kitap, yaz):
#     """Verilen veriyi JSON dosyasına kaydeder."""
#     with open(kitap, "w", encoding="utf-8") as f:
#         json.dump(yaz, f, indent=4, ensure_ascii=False) 



# # Kaydedilecek veri
# yaz = {
#   "isim": "Ahmet111",
#   "yas": 30,
#   "sehir": "İstanbul"
# }
# oku.append({"isim": "Ahmet111",
#   "yas": 30,
#   "sehir": "İstanbul"})   

# # Fonksiyonu kullanarak data.json’a yaz
# json_yaz("kitap.json", oku)

# print(yaz)

import os
import json

DOSYA = "kitap.json"

# Dosya kontrolü ve oluşturma
def dosya_kontrol():
    """kitap.json dosyası yoksa oluşturur."""
    if not os.path.exists(DOSYA):
        with open(DOSYA, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4, ensure_ascii=False)

# JSON oku
def kitap_oku():
    """kitap.json içeriğini okur ve liste olarak döndürür."""
    with open(DOSYA, "r", encoding="utf-8") as f:
        return json.load(f)

# JSON yaz
def kitap_yaz(veri):
    """Listeyi kitap.json dosyasına yazar."""
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=4, ensure_ascii=False)

# Kitap ekle (isim kontrolü yaparak)
def kitap_ekle(kitap_adi, yazar, yayinevi, dil, fiyat, barkod=None):
    veri = kitap_oku()
    for kitap in veri:
        if kitap["Kitap_Adi"].lower() == kitap_adi.lower():
            print(f"⚠️ '{kitap_adi}' zaten kayıtlı.")
            return
    veri.append({
        "Barkod": barkod if barkod else 0,  # opsiyonel
        "Kitap_Adi": kitap_adi,
        "Yazar": yazar,
        "Yayinevi": yayinevi,
        "Dil": dil,
        "Fiyat": fiyat
    })
    kitap_yaz(veri)
    print(f"✅ '{kitap_adi}' eklendi.")

# Kitap sil (isim ile)
def kitap_sil(kitap_adi):
    veri = kitap_oku()
    yeni_veri = [k for k in veri if k["Kitap_Adi"].lower() != kitap_adi.lower()]
    if len(veri) == len(yeni_veri):
        print(f"⚠️ '{kitap_adi}' bulunamadı.")
    else:
        kitap_yaz(yeni_veri)
        print(f"🗑️ '{kitap_adi}' silindi.")

# Kitap ara (isim ile, parça eşleşme)
def kitap_ara(aranan):
    veri = kitap_oku()
    bulunan = [k for k in veri if aranan.lower() in k["Kitap_Adi"].lower()]
    return bulunan

# Kitap güncelle (isim ile)
def kitap_guncelle(kitap_adi, yeni_bilgi: dict):
    veri = kitap_oku()
    bulundu = False
    for kitap in veri:
        if kitap["Kitap_Adi"].lower() == kitap_adi.lower():
            kitap.update(yeni_bilgi)
            bulundu = True
            break
    if bulundu:
        kitap_yaz(veri)
        print(f"✏️ '{kitap_adi}' güncellendi.")
    else:
        print(f"⚠️ '{kitap_adi}' bulunamadı.")

# Kitap sayısı
def kitap_sayisi():
    veri = kitap_oku()
    return len(veri)

# ------------------- ÖRNEK KULLANIM -------------------
if __name__ == "__main__":
    dosya_kontrol()

    # Kitap ekleme
    kitap_ekle("İnce Memed", "Yaşar Kemal", "YKY", "Türkçe", 45.5, 9789754700114)

    # Kitap sayısı
    print("📚 Toplam kitap:", kitap_sayisi())

    # Arama
    print("🔍 Arama sonucu:", kitap_ara("Hazan"))

    # Güncelleme (örnek: fiyat değiştirme)
    kitap_guncelle("Okçu'nun Yolu", {"Fiyat": 29.99})

    # Silme
    kitap_sil("Yanlış Hayat Doğru Yaşanmaz")

    # Son kitap listesi
    print("📖 Güncel Liste:", kitap_oku())
