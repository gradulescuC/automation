# Definiti o clasa Vehicul care sa ia urmatoarele atribute: viteza_maxima si distranta_parcursa


class Vehicle:
    def __init__(self, max_speed, mileage):
        self._max_speed = max_speed
        self._mileage = mileage

    def calculeaza_timp(self,_max_speed,distanta):
        return int(distanta) /int(_max_speed)

max_speed = input("Introduceti viteza maxima a masinii ")
mileage = input("Introduceti kilometrajul masinii ")
distanta = input("Introduceti distanta intre cele doua locatii ")
autobuz = Vehicle(max_speed,mileage)
print(f"Autobuzul poate sa ajunga pana la {max_speed} kilometri pe ora si are o distanta totala parcursa de {autobuz._mileage} de kilometri")
print(f"Autobuzul poate ajunge la destinatie in {autobuz.calculeazaTimp(max_speed,distanta)} ore")
