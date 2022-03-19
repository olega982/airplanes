from airplane_common import Airplane


class PrivetJet(Airplane):
    def __init__(self, model, capacity, lifting_capacity, year, miles, *comforts):
        self.comforts = comforts
        super(PrivetJet, self).__init__(model, capacity, lifting_capacity, year, miles)

    def print_uniq_description(self):
        print(f"Our private jet include {self.comforts}")
