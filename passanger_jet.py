from airplane_common import Airplane

class PassengerJet(Airplane):
    def __init__(self, model, capacity, lifting_capacity, year, miles, route):
        self.route = route
        super(PassengerJet, self).__init__(model, capacity, lifting_capacity, year, miles)

    def print_uniq_description(self):
        print(f"Passenger airplane can lift and transfer {self.capacity} people in the one flight.")

    def show_the_route(self):
        print(f"The airplane follow the {self.route}")