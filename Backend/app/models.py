from datetime import datetime

class Administrator:
    def __init__(self, ime, prezime, adresa, grad, drzava, broj_telefona, email, lozinka, korisnicko_ime):
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.grad = grad
        self.drzava = drzava
        self.broj_telefona = broj_telefona
        self.email = email
        self.lozinka = lozinka
        self.korisnicko_ime = korisnicko_ime

    def potvrdi_registraciju(self, korisnik):
        """
        Potvrdjuje zahtev za registraciju korisnika
        """
        korisnik.registrovan = True
        # Implementacija za slanje email notifikacije korisniku
        print(f"Korisnik {korisnik.korisnicko_ime} je uspesno registrovan.")

    def odbij_registraciju(self, korisnik):
        """
        Odbija zahtev za registraciju korisnika
        """

        korisnik.registrovan = False
        # Implementacija za slanje obavestenja korisniku
        print(f"Korisnik {korisnik.korisnicko_ime} je odbijen za registraciju.")

    def dodaj_temu(self, naziv, opis):
        """
        Dodaje novu temu
        """

        # Pretpostavka: Teme se cuvaju u bazi
        nova_tema = {"naziv":naziv, "opis":opis}
        # Dodavanje u bazu ili listu
        print(f"Nova tema '{naziv}' je uspesno dodata.")
        return nova_tema
    
    def izmeni_temu(self, tema_id, novi_podaci):
        """
        Menja postojecu temu na osnovu ID-a
        """

        # Pretpostavka: Teme se pretrazuju kroz bazu na osnovu ID-a
        # Implementacija za izmenu teme
        print(f"Tema sa ID-em {tema_id} je uspesno izmenjena.")
        return True
    
    def obrisi_temu(self, tema_id):
        """
        Brise temu na osnovu ID-a
        """

        # Pretpostavka: Teme se brisu iz baze
        # Implementacija za brisanje teme
        print(f"Tema sa ID-em {tema_id} je uspesno obrisana.")
        return True
    
class Korisnik:
    def __init__(self, ime, prezime, adresa, grad, drzava, broj_telefona, email, lozinka, korisnicko_ime):
        self.ime = ime
        self.prezime = prezime
        self.adresa = adresa
        self.grad = grad
        self.drzava = drzava
        self.broj_telefona = broj_telefona
        self.email = email
        self.lozinka = lozinka
        self.korisnicko_ime = korisnicko_ime

    def registruj_se(self, podaci):
        """
        Registruje korisnika sa datim podacima.
        """

        # Implementacija za cuvanje korisnika u bazi
        print(f"Korisnik {podaci['korisnicko_ime']} je registrovan.")
        return True
    
    def prijavi_se(self, korisnicko_ime, lozinka):
        """
        Prijavljuje korisnika na osnovu email-a i lozinke.    
        """

        # Implementacija provere u bazi za email i lozinku
        print(f"Korisnik {korisnicko_ime} uspesno prijavljen.")
        return True
    
    def izmeni_nalog(self, novi_podaci):
        """
        Menja korisnicke podatke.
        """

        # Azuriranje korisnickih podataka
        self.__dict__.update(novi_podaci)
        # Implementacija izmene u bazi
        print(f"Nalog korisnika {self.korisnicko_ime} uspesno azuriran")
        return True
    
    def kreiraj_diskusiju(self, naziv, tema, tekst):
        """
        Kreira novu diskusiju
        """

        nova_diskusija = {"naziv": naziv, "tema": tema, "tekst" : tekst, "autor": self.korisnicko_ime}
        # Implementacija dodavanja diskusije u bazu
        print(f"Kreirana je nova diskusija '{naziv}'.")
        return nova_diskusija
    
    def izmeni_diskusiju(self, diskusija_id, novi_podaci):
        """
        Menja postojecu diskusiju
        """

        # Azuriranje diskusije u bazi
        print(f"Diskusija sa ID-em {diskusija_id} je izmenjena.")
        return True
    
    def obrisi_diskusiju(self, diskusija_id):
        """
        Brise diskusiju
        """

        # Implementacija brisanja diskusije iz baze
        print(f"Diskusija sa ID-em {diskusija_id} je obrisana.")
        return True
    
    def postavi_komentar(self, diskusija_id, tekst):
        """
        Postavlja komentar na diskusiju
        """

        komentar = {"diskusija_id": diskusija_id, "tekst": tekst, "autor": self.korisnicko_ime}
        # Implementacija dodavnaja komentara u bazu
        print(f"Postavljen je komentar na diskusiju {diskusija_id}.")
        return komentar
    
    def obrisi_komentar(self, komentar_id):
        """
        Brise komentar
        """

        # Implementacija brisanja komentara iz baze
        print(f"Komentar sa ID-em {komentar_id} je obrisan")
        return True
    
    def like_diskusija(self, diskusija_id):
        """
        Postavlja lajk na diskusiju
        """

        # Implementacija azuriranja broja lajkova u bazi za diskusiju
        print(f"Diskusija  {diskusija_id} je lajkovana.")
        return True
    
    def dislike_diskusija(self, diskusija_id):
        """
        Postavlja dislike na diskusiju
        """

        # Azuriranje broja dislajkova u bazi za diskusiju
        print(f"Diskusija {diskusija_id} je dislajkovana")
        return True
    def pomene_korisnika(self, komentar_id, korisnik_id):
        """
        Pominje drugog korisnika u komentaru
        """

        # Implementacija slanja obavestenja korisniku
        print(f"Korisnik {korisnik_id} je pomenut u komentaru {komentar_id}")
        return True
    
class Diskusija:
    def __init__(self, naziv, tekst, autor, tema):
        self.naziv = naziv
        self.tekst = tekst
        self.autor = autor
        self.tema = tema
        self.datum_kreiranja = datetime.now()
        self.lajkovi = 0
        self.dislajkovi = 0
        self.komentari = []  # Lista za skladistenje komentara

        def dodaj_komentar(self, komentar):
            """
            Dodaje komentar na diskusiju
            """

            self.komentari.append(komentar)
            print(f"Komentar je dodat na diskusiju '{self.naziv}'")
            return komentar
        
        def izmeni_tekst(self, novi_tekst):
            """
            Menja tekst diskusije
            """

            self.tekst = novi_tekst
            print(f"Tekst diskusije '{self.naziv}' je azuriran.")
            return True
        
        def obiris_komentar(self, komentar_id):
            """
            Brise komentar iz diskusije na osnovu ID-a
            """

            for komentar in self.komentari:
                if komentar["id"] == komentar_id:
                    self.komentari.remove(komentar)
                    print(f"Komentar sa ID-em {komentar_id} je obrisan.")
                    return True
            
            print(f"Komentar sa ID-em {komentar_id} nije pronadjen.")
            return False
        
        @staticmethod
        def sortiraj_diskusije(diskusije, kriterijum):
            """
            Sortira listu diskusija prema datom kriterijumu
            Kriterijum moze biti 'naziv', 'datum_kreiranja'. 'lajkovi', 'dislajkovi'
            """

            if kriterijum in ['naziv', 'datum_kreiranja', 'lajkovi', 'dislajkovi']:
                sorted_diskusije = sorted(diskusije, key=lambda d: getattr(d, kriterijum), reverse=(kriterijum in ['lajkovi', 'dislajkovi']))
                print(f"Diskusije su sortirane po '{kriterijum}.")
                return sorted_diskusije
            else:
                print(f"Nevazeci kriterijum za sortiranje: '{kriterijum}'.")
                return diskusije
            
class Komentar:
    def __init__(self, tekst, autor, diskusija):
        self.tekst = tekst
        self.autor = autor
        self.diskusija = diskusija
        self.datum_kreiranja = datetime.now()

    def izmeni_tekst(self, novi_tekst):
        """
        Menja tekst komentara
        """

        self.tekst = novi_tekst
        print(f"Tekst komentara je izmenjen. Novi tekst: '{self.tekst}'")
        return True

    
class Tema:
    def __init__(self, naziv, opis):
        self.naziv = naziv
        self.opis = opis

    @staticmethod
    def dodaj_temu(naziv, opis):
        """
        Dodaje novu temu
        """

        nova_tema = Tema(naziv, opis)
        # Implementacija dodavanja nove teme u bazu
        print(f"Tema '{naziv}' je uspesno dodata.")
        return nova_tema
    
    def izmeni_temu(self, novi_podaci):
        """
        Menja postojecu temu
        """

        if "naziv" in novi_podaci:
            self.naziv = novi_podaci["naziv"]
        if "opis" in novi_podaci:
            self.opis = novi_podaci["opis"]

        print(f"Tema '{self.naziv}' je uspesno izmenjena.")
        return True
    
    def obrisi_temu(self):
        """
        Brise temu iz baze
        """

        # Implementacija brisanja iz baze
        print(f"Tema '{self.naziv}' je uspesno obrisana.")
        return True


class Notifikacija:
    def __init__(self, primalac, tekst):
        self.primalac = primalac    #ID ili korisnicko ime primaoca
        self.tekst = tekst
        self.datum = datetime.now()

    def posalji_notifikaciju(self):
        """
        Salje notifikaciju korisniku
        """

        # Pretpostavka: Slanje obavlja putem emaila ili API-ja
        # Implementacija slanja notifikacije

        print(f"Notifikacija poslata korisniku '{self.primalac}': {self.tekst}")
        return True

