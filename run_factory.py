from factory_class import Factory


factory_instance = Factory()
while True:
    water_string = input('Please insert your water. (Type "water").').lower()
    bread_string = input('Please insert your bread. (Type "bread").').lower()
    print(factory_instance.make_naan(water_string,bread_string))
    again = input('would you like to make more bread?').lower()
    if again == 'no':
        break
    else:
        continue

