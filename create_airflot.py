from privat_jet import PrivetJet
from passanger_jet import PassengerJet
from fire_jet import FireJet


class Garage:
    __park = None

    @staticmethod
    def create_garage():
        if Garage.__park is None:
            Garage.__park = [PrivetJet("steals_1", 17, 2000, 2010, 100000, "big seats", "drinks", "sleeping bad"),
                             PrivetJet("privat_1", 20, 1200, 2011, 134000, "big seats", "drinks", "sleeping bad"),
                             FireJet("mig_21", 2, 1200, 2011, 150000, " air- ground bombs", "air-air bombs"),
                             FireJet("mig_27", 2, 1500, 2011, 180000, "air-air bombs"),
                             PassengerJet("boeing_787", 780, 9000, 2018, 17800000, "Moscow-Tashkent"),
                             PassengerJet("boeing_747", 747, 8000, 2014, 19900000, "Minsk-Tbilisi")]
        return Garage

    @staticmethod
    def get_garage():
        return Garage.__park


#a = print(Garage.create_garage().get_garage())
#b = Garage.create_garage()
#print(id(a), id(b))
