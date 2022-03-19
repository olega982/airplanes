# calculate the total capacity and lifting capacity
def calculate_capacity_lifting(airflot):
    total_capacity = 0
    lifting_capacity = 0
    for plane in airflot:
        total_capacity += plane.capacity
        lifting_capacity += plane.lifting_capacity
    print(
        f"Our airflot has {total_capacity} passengers of total capacity and {lifting_capacity} kg of lifting capacity.\n")


# Sort the company's aircraft by range.
def sort_the_aircrafts(airflot):
    fire_jets = []
    private_jets = []
    passenger_jets = []
    for plane in airflot:
        if plane.capacity <= 5:
            fire_jets.append(plane.__repr__())
        elif plane.capacity > 5 and plane.capacity <= 100:
            private_jets.append(plane.__repr__())
        elif plane.capacity > 100:
            passenger_jets.append(plane.__repr__())
    return print(f"Now we have the following airflot:"
                 f"\n Passenger jets: {passenger_jets}"
                 f"\n Private jets: {private_jets}"
                 f"\n Fire jets: {fire_jets}")


# Find an aircraft in the company that matches the specified range of parameters.
def find_the_aircraft(airflot, passangers, year):
    appropriate_planes = []
    for plane in airflot:
        if str(plane.capacity) == passangers and str(plane.year) == year:
            appropriate_planes.append(plane.__repr__())
    if appropriate_planes:
        return print(f" You are looking for: {appropriate_planes}")
    print(" We have no appropriate planes in the airpark.")


