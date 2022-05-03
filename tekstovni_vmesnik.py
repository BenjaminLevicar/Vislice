import model

def izpis_igre(igra):
    preostali_poiskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()
    return(
        '============================================\n'
        'Število preostalih poskusov: {} \n'.format(preostali_poiskusi) +
        'Pravilni del gesla: {} \n'.format(igra.pravilni_del_gesla()) + 
        'Neuspeli poskusi: {} \n'.format(igra.nepravilni_ugibi())

    )

def izpis_zmage(igra):
    return 'Čestitam! Uganil si geslo {}'.format(igra.geslo)

def izpis_poraza(igra):
    return 'Porabil si vse poskuse. Geslo je {}'.format(igra.geslo)

def zahtevaj_vnos():
    return input('Ćrka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break