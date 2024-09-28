import uuid


class CarInfo:
    def __init__(self, name, year, price, car_id=None):
        self.id = car_id if car_id else uuid.uuid4()
        self.name = name
        self.year = year
        self.price = price

    def display_info(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "year": self.year,
            "price": self.price,
        }

    def update_info(self, name=None, year=None, price=None):
        if name:
            self.name = name
        if year:
            self.year = year
        if price:
            self.price = price


class CarSystem:
    def __init__(self):
        self.cars = []

        self.cars.append(CarInfo("Toyota", 2018, 40000, car_id="1"))
        self.cars.append(CarInfo("Honda", 2020, 30000, car_id="2"))

    def display_all_cars(self):
        if self.cars:
            found_cars = [car.display_info() for car in self.cars]
            return {"message": "All list", "data": found_cars}
        else:
            return {"message": "No Car Data found"}

    def add_car(self, name, year, price):
        car = CarInfo(name, year, price)
        self.cars.append(car)

    def find_car_by_id(self, car_id):
        for car in self.cars:
            if str(car.id) == car_id:
                return car.display_info()
        return {"Message": f"No Car found with that id: {car_id}"}

    def delete_car(self, car_id):
        car = self.find_car_by_id(car_id)
        if car:
            self.cars.remove(car)
            return {"message": f"Car with ID {car_id} has been deleted."}
        else:
            return {"message": "Car not found"}


myCarSystem = CarSystem()
print("All List \n", myCarSystem.display_all_cars())
myCarSystem.add_car("Ford", 2021, 25000)
print("Updated Car List \n", myCarSystem.display_all_cars())
print("Find By Id \n", myCarSystem.find_car_by_id("1"))


ford_id = myCarSystem.cars[-1].id
print("Find by Id\n", myCarSystem.find_car_by_id(str(ford_id)))
