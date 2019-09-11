"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    Limo = Car(100, "Limo")
    Limo.add_fuel(20)
    Limo.drive(115)
    print("Limo odometer = ", Limo.odometer)
    print("Limo fuel = ", Limo.fuel)
    my_car.drive(30)
    print(Limo)
    # print(my_car)
    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)
    # print(my_car)




    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()