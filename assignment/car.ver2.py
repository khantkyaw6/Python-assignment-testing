class Car:
    def __init__(self, brand, model, year, price, quantity):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.quantity = quantity


car_inventory = []


def display_all_cars():
    if car_inventory:
        for car in car_inventory:
            print(
                f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Price: {car.price}, Quantity: {car.quantity}"
            )
    else:
        print("No cars in inventory.")


def total_car():
    total = sum(car.quantity for car in car_inventory)
    print(f"Total number of cars in inventory: {total}")


def add_car(brand, model, year, price, quantity):
    new_car = Car(brand, model, year, price, quantity)
    car_inventory.append(new_car)
    print(f"{brand} {model} added to inventory.")


def search_car_by_brand(brand):
    found = False
    for car in car_inventory:
        if car.brand == brand:
            print(
                f"Found: {car.brand} {car.model}, Year: {car.year}, Price: {car.price}, Quantity: {car.quantity}"
            )
            found = True
        if not found:
            print(f"No cars found for brand: {brand}")


def update_car(brand, model, new_price=None, new_year=None, new_quantity=None):
    for car in car_inventory:
        if car.brand == brand and car.model == model:
            if new_price:
                car.price = new_price
            if new_year:
                car.year = new_year
            if new_quantity:
                car.quantity = new_quantity
            print(f"{brand} {model} updated in inventory.")


add_car("Toyota", "Camry", 2020, 20000, 5)
add_car("Honda", "Civic", 2022, 60000, 2)
display_all_cars()
total_car()
