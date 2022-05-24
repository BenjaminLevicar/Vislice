import random
import json


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK ='S'
ZMAGA = 'W'
PORAZ = 'L'

DATOTEKA_Z_BESDAMI = 'besede.txt'
DATOTEKA_S_STANJEM = 'stanje.json'

class Igra:


    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        self.crka = [] if crke == None else crke

    def napacne_crke(self):
        seznam_napacnih_crk = []
        for element in self.crka:
            if element not in self.geslo:
                seznam_napacnih_crk.append(element)
        return seznam_napacnih_crk

    def pravilne_crke(self):
        seznam_pravilnih_crk = []
        for element in self.crka:
            if element in self.geslo:
                seznam_pravilnih_crk.append(element)
        return seznam_pravilnih_crk

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for element in self.geslo:
            if element not in self.crka:
                return False
        return True
     
    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        beseda_zaenkrat = ''
        for element in self.geslo:
            if element in self.crka:
                beseda_zaenkrat += element + ' '
            else:
                beseda_zaenkrat += '_ '
        return beseda_zaenkrat.strip()
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
        
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crka:
            return PONOVLJENA_CRKA
        else:
            self.crka.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open(DATOTEKA_Z_BESDAMI, encoding='utf-8') as f:
    bazen_besed = [vrstica.strip().upper() for vrstica in f]

def nova_igra():
    return Igra(random.choice(bazen_besed))

class Vislice:

    def __init__(self) -> None:
        self.igre ={}
        self.datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteki()
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]  # _ je notri saj potrebujemo samo prvi element v slovarju
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteki()

    def zapisi_igre_v_datoteki(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.geslo, igra.crka, stanje)
                for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(geslo, crke), stanje)
                for id_igre, (geslo, crke, stanje) in igre.items()}

