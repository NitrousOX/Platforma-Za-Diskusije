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

    def get_ime(self):
        return self.ime
    def set_ime(self, ime):
        self.ime = ime
    
    def get_prezime(self):
        return self.prezime
    def set_prezime(self, prezime):
        self.prezime = prezime
    
    def get_adresa(self):
        return self.adresa
    def set_adresa(self, adresa):
        self.adresa = adresa
    
    def get_grad(self):
        return self.grad
    def set_grad(self, grad):
        self.grad = grad

    def get_drzava(self):
        return self.drzava
    def set_drzava(self, drzava):
        self.drzava = drzava
    
    def get_broj_telefona(self):
        return self.broj_telefona
    def set_broj_telefona(self, broj_telefona):
        self.broj_telefona = broj_telefona
    
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    
    def get_lozinka(self):
        return self.lozinka
    def set_lozinka(self, lozinka):
        self.lozinka = lozinka
    
    def get_korisnicko_ime(self):
        return self.korisnicko_ime
    def set_korisnicko_ime(self, korisnicko_ime):
        self.korisnicko_ime = korisnicko_ime
    
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

    def get_ime(self):
        return self.ime
    def set_ime(self, ime):
        self.ime = ime
    
    def get_prezime(self):
        return self.prezime
    def set_prezime(self, prezime):
        self.prezime = prezime
    
    def get_adresa(self):
        return self.adresa
    def set_adresa(self, adresa):
        self.adresa = adresa
    
    def get_grad(self):
        return self.grad
    def set_grad(self, grad):
        self.grad = grad

    def get_drzava(self):
        return self.drzava
    def set_drzava(self, drzava):
        self.drzava = drzava
    
    def get_broj_telefona(self):
        return self.broj_telefona
    def set_broj_telefona(self, broj_telefona):
        self.broj_telefona = broj_telefona
    
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    
    def get_lozinka(self):
        return self.lozinka
    def set_lozinka(self, lozinka):
        self.lozinka = lozinka
    
    def get_korisnicko_ime(self):
        return self.korisnicko_ime
    def set_korisnicko_ime(self, korisnicko_ime):
        self.korisnicko_ime = korisnicko_ime
    
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

        def get_naziv(self):
            return self.naziv
        def set_naziv(self, naziv):
            self.naziv = naziv

        def get_tekst(self):
            return self.tekst
        def set_tekst(self, tekst):
            self.tekst = tekst

        def get_autor(self):
            return self.autor
        def set_autor(self, autor):
            self.autor = autor

        def get_tema(self):
            return self.tema
        def set_tema(self, tema):
            self.tema = tema

        def get_datum_kreiranja(self):
            return self.datum_kreiranja
        def set_datum_kreiranja(self, datum_kreiranja):
            self.datum_kreiranja = datum_kreiranja

        def get_lajkovi(self):
            return self.lajkovi
        def set_lajkovi(self, lajkovi):
            self.lajkovi = lajkovi

        def get_dislajkovi(self):
            return self.dislajkovi
        def set_dislajkovi(self, dislajkovi):
            self.dislajkovi = dislajkovi

        def get_komentari(self):
            return self.komentari
        def set_komentari(self, komentari):
            self.komentari = komentari
            
class Komentar:
    def __init__(self, tekst, autor, diskusija):
        self.tekst = tekst
        self.autor = autor
        self.diskusija = diskusija
        self.datum_kreiranja = datetime.now()

    def get_tekst(self):
        return self.tekst
    def set_tekst(self, tekst):
        self.tekst = tekst

    def get_autor(self):
        return self.autor
    def set_autor(self, autor):
        self.autor = autor

    def get_diskusija(self):
        return self.diskusija
    def set_diskusija(self, diskusija):
        self.diskusija = diskusija

    def get_datum_kreiranja(self):
        return self.datum_kreiranja
    def set_datum_kreiranja(self, datum):
        self.datum_kreiranja = datum

    

    
class Tema:
    def __init__(self, naziv, opis):
        self.naziv = naziv
        self.opis = opis

    def get_naziv(self):
        return self.naziv
    def set_naziv(self, naziv):
        self.naziv = naziv

    def get_opis(self):
        return self.opis
    def set_opis(self, opis):
        self.opis = opis
        


class Notifikacija:
    def __init__(self, primalac, tekst):
        self.primalac = primalac    #ID ili korisnicko ime primaoca
        self.tekst = tekst
        self.datum = datetime.now()

    def get_primalac(self):
        return self.primalac
    def set_primalac(self, primalac):
        self.primalac = primalac

    def get_tekst(self):
        return self.tekst
    def set_tekst(self, tekst):
        self.tekst = tekst
    
    def get_datum(self):
        return self.datum
    def set_datum(self, datum):
        self.datum = datum
    


