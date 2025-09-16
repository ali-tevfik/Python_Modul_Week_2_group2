def zaman():
    """Bugünün tarihi ve 2 hafta sonrası"""
    bugun = datetime.datetime.now()
    iki_hafta_sonra = bugun + datetime.timedelta(weeks=2)
    return bugun.strftime("%d-%m-%Y %H:%M"), iki_hafta_sonra.strftime("%d-%m-%Y %H:%M")