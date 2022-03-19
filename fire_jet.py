from airplane_common import Airplane


class FireJet(Airplane):
    def __init__(self, model, capacity, lifting_capacity, year, miles, *weapon):
        self.weapon = weapon
        super(FireJet, self).__init__(model, capacity, lifting_capacity, year, miles)

    def show_the_weapon(self):
        print(f"The airplane follow the {self.weapon}")