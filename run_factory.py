# import our class
from factory_class import Factory

# instantiate our class so we can use it
factory_instance = Factory()
# while loop so we can keep prompting the user for input if they want to keep making bread
while True:
    # takes input for ingredients
    water_string = input('Please insert your water. (Type "water").').lower()
    bread_string = input('Please insert your bread. (Type "bread").').lower()
    print(factory_instance.make_naan(water_string,bread_string))
    # check if the user wants to make more bread
    again = input('would you like to make more bread?').lower()
    if again == 'no':
        break
    else:
        continue

