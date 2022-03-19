from create_airflot import Garage
import actions

my_flot = Garage.create_garage().get_garage()
print("\nHello, welcome to 'Letun' airport.Please,follow the instructions:"
      "\nEnter '1' if you want to see an airflot jets in different range." \
      "\nEnter '2' if you want to calculate the aiflot lifting capacity" \
      "\nEnter '3' if you want to find the jet according to the human crew and year."
      "\nIf you want to quit, enter 'q'")

while True:
    action = input("Enter your command:")

    if action == '1':
        actions.sort_the_aircrafts(my_flot)
    elif action == "2":
        actions.calculate_capacity_lifting(my_flot)
    elif action == "3":
        passengers = input(f"Please, enter the number of passengers:")
        production_year = input(f"Please, enter the production year:")
        actions.find_the_aircraft(my_flot, passengers, production_year)
    elif action == "q":
        break
    else:
        print("Please, read the instruction, your operation number is not valid.")
