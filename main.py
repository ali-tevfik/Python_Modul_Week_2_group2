import datetime
from myTime import zaman
from uye import *
from kitap import *

def mainMenu():
    while True:
        print("""
        HALK KÜTÜPHANESİNE HOŞGELDİNİZ

        1 - Üyelik İşlemleri
        2 - Kitap İşlemleri
        3 - Çıkış
        """)
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            uyelik_islemleri()
        elif secim == "2":
            kitap_islemleri()
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Hatalı giriş! Tekrar deneyiniz.")

def uyelik_islemleri():
    while True:
        print("""
        ÜYELİK İŞLEMLERİ MENÜSÜ

        1 - Üye Ekle
        2 - Üye Sil
        3 - Üye Listele
        4 - Üye Ara
        5 - Ana Menüye Dön
        """)
        secim = input("İşlem seçiniz: ")

        if secim == "1":
           uye_ekle()
        elif secim == "2":
           uye_sil()
        elif secim == "3":
           uyeleri_listele()
        elif secim == "4":
            uye_ara()
        elif secim == "5":
            break
        else:
            print("Hatalı seçim!")

def kitap_islemleri():
    while True:
        print("""
        KİTAP İŞLEMLERİ MENÜSÜ

        1 - Kitap Ekle
        2 - Kitap Sil
        3 - Kitap Listele
        4 - Kitap Ara
        5 - Kitap Ödünç Ver
        6 - Kitap Geri Al
        7 - Ana Menüye Dön
        """)
        secim = input("Islem seçiniz: ")

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitap_sil()
        elif secim == "3":
            kitap_listele()
        elif secim == "4":
           kitap_ara()
        elif secim == "5":
            baslangic, bitis = zaman()
            print(f"Kitap ödünç verildi. Başlangıç: {baslangic}, Teslim tarihi: {bitis}")
        elif secim == "6":
            print("Kitap geri alındı.")
        elif secim == "7":
            break
        else:
            print("Hatalı seçim!")

mainMenu()