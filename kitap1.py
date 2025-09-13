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

def kitap_ekle(kitap_adi, yazar, yayinevi, dil, fiyat, barkod=None):
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

def kitap_sil(kitap_adi):
    veri = kitap_oku()
    yeni_veri = [k for k in veri if k["Kitap_Adi"].lower() != kitap_adi.lower()]
    if len(veri) == len(yeni_veri):
        print(f"⚠️ '{kitap_adi}' bulunamadı.")
    else:
        kitap_yaz(yeni_veri)
        print(f"🗑️ '{kitap_adi}' silindi.")

def kitap_ara(aranan):
    veri = kitap_oku()
    bulunan = [k for k in veri if aranan.lower() in k["Kitap_Adi"].lower()]
    return bulunan

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

def kitap_sayisi():
    return len(kitap_oku())

# ------------------- Menü Sistemi -------------------

def menu():
    dosya_kontrol()
    while True:
        print("\n📚 Kitap Yönetim Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Ara")
        print("4. Kitap Güncelle")
        print("5. Kitap Sayısı")
        print("6. Tüm Kitapları Listele")
        print("0. Çıkış")

        secim = input("👉 Seçiminizi yapın: ")

        if secim == "1":
            kitap_adi = input("Kitap adı: ")
            yazar = input("Yazar: ")
            yayinevi = input("Yayınevi: ")
            dil = input("Dil: ")
            fiyat = float(input("Fiyat: "))
            barkod = input("Barkod (opsiyonel, boş bırakılabilir): ")
            barkod = int(barkod) if barkod.strip() else None
            kitap_ekle(kitap_adi, yazar, yayinevi, dil, fiyat, barkod)

        elif secim == "2":
            kitap_adi = input("Silmek istediğiniz kitabın adı: ")
            kitap_sil(kitap_adi)

        elif secim == "3":
            aranan = input("Aranacak kitap adı: ")
            bulunan = kitap_ara(aranan)
            if bulunan:
                print("🔍 Bulunan kitaplar:")
                for k in bulunan:
                    print(k)
            else:
                print("❌ Hiç kitap bulunamadı.")

        elif secim == "4":
            kitap_adi = input("Güncellenecek kitap adı: ")
            alan = input("Hangi alanı güncellemek istiyorsunuz? (Yazar, Yayinevi, Dil, Fiyat): ")
            yeni_deger = input("Yeni değer: ")
            if alan.lower() == "fiyat":
                yeni_deger = float(yeni_deger)
            kitap_guncelle(kitap_adi, {alan: yeni_deger})

        elif secim == "5":
            print(f"📚 Toplam kitap sayısı: {kitap_sayisi()}")

        elif secim == "6":
            print("📖 Tüm kitaplar:")
            for k in kitap_oku():
                print(k)

        elif secim == "0":
            print("👋 Programdan çıkılıyor...")
            break

        else:
            print("⚠️ Geçersiz seçim, tekrar deneyin!")

# ------------------- Çalıştır -------------------
if __name__ == "__main__":
    menu()
