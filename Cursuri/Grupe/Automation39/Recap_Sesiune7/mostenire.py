class Cinema:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.filme = []
        self.bilete_vandute = 0
        self.total_incasari = 0

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)

    def rulare_filme(self):
        print('Filmele ruleaza la', self.nume, 'cinema:')
        for film in self.filme:
            print('-', film)

class Film(Cinema):

    def __init__(self, titlu, gen, durata, pret_bilet, locuri_disponibile, capacitate_film, nume, adresa, capacitate):
        super().__init__(nume, adresa, capacitate)
        self.titlu = titlu
        self.genul = gen
        self.durata = durata
        self.pret_bilet = pret_bilet
        self.locuri_disponibile = locuri_disponibile
        self.capacitate_film = capacitate_film

    def _vinde_bilete(self, film):
        if film in self.filme and film.locuri_disponibile > 0:
            film.locuri_disponibile -= 1
            self.bilete_vandute += 1
            self.total_incasari += film.pret_bilet
            print('Bilete in sold pentru', film.titlu)
        else:
            print('Ne pare rau. acest film nu mai ruleaza sau nu mai sunt bilete.')

    # def reseteaza_locuri_film(self):
    #     self.locuri_disponibile = self.capacitate_film

# Instantiem filmul
cinderella = Film('Cinderella', 'Desen_animat',150, 20, 10,100,'Hollywood', 'ParkLake', 150)
avatar = Film("Avatar","Fantasy",180,70,30,300,'Hollywood', 'ParkLake', 150)
# Instantiem Cinematofgraful
cinema1 = Cinema('Hollywood', 'ParkLake', 150)
# Adaug filmul in Cinematograf
cinema1.add_film("cinderella")
cinema1.add_film("avatar")
# Afisam filmele disponibile
cinema1.rulare_filme()

cinema2 = Film('Avatar', 'Fantasy',150, 20, 10,100,'Hollywood', 'ParkLake', 150)
cinema2.add_film("John Which 4")
cinema2.rulare_filme()