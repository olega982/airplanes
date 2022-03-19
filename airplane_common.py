class Airplane:
    def __init__(self, model, capacity, lifting_capacity, year, miles):
        self.model = model
        self.year = year
        self.miles = miles
        self.capacity = capacity
        self.lifting_capacity = lifting_capacity

    def __repr__(self):
        return f" {self.model}:{self.year}"

    def print_airplane_info(self):
        print(f" This is {self.model} build in {self.year} with the {self.miles} of mileage")

    def update_miles(self, new_milage):
        if self.miles <= new_milage:
            self.miles = new_milage
        else:
            print("You cant roll back the miles!")
