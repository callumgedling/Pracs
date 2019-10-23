from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5
    def __init__(self, name, fuel, fanciness=1.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return "{} plus flagfall of {}".format(super().__str__(), SilverServiceTaxi.flagfall)



    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()

