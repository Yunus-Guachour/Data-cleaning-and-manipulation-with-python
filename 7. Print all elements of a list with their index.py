#7.Print all elements of a list with their index

list_of_cars = ['BMW', 'Mercedes', 'Porche', 'Lamborghini', 'Ford']
for index, list_of_cars in enumerate(list_of_cars, start = 1):
    print(index, list_of_cars)
