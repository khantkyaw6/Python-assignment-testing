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

        return {"message": "Car info updated successfully"}


class CarSystem:
    def __init__(self):
        self.cars = []

        self.cars.append(CarInfo("Toyota", 2018, 40000, car_id="1"))
        self.cars.append(CarInfo("Honda", 2020, 30000, car_id="2"))

    def display_all_cars(self):
        if self.cars:
            found_cars = [car.display_info() for car in self.cars]
            return {
                "message": "All list",
                "data": found_cars,
                "total_car": len(found_cars),
            }
        else:
            return {"message": "No Car Data found"}

    def add_car(self, name, year, price):
        car = CarInfo(name, year, price)
        self.cars.append(car)
        return {"message": "Car added"}

    def find_car_by_id(self, car_id):
        for car in self.cars:
            if str(car.id) == car_id:
                return car  # Return the CarInfo object, not the dictionary
        return None  # Return None if no car is found

    def delete_car(self, car_id):
        car = self.find_car_by_id(car_id)
        if car:
            self.cars.remove(car)
            return {"message": f"Car with ID {car_id} has been deleted."}
        else:
            return {"message": "Car not found"}

    def update_car_info(self, car_id, name=None, year=None, price=None):
        car = self.find_car_by_id(car_id)
        if car:
            return car.update_info(name=name, year=year, price=price)
        return {"message": f"No Car found with that id: {car_id}"}


myCarSystem = CarSystem()
print("All List \n", myCarSystem.display_all_cars())
myCarSystem.add_car("Ford", 2021, 25000)
print("Updated Car List \n", myCarSystem.display_all_cars())
print("Find By Id \n", myCarSystem.find_car_by_id("1"))

# Find the ID of the last added car (Ford) and update it
ford_id = myCarSystem.cars[-1].id
print("Find by Id\n", myCarSystem.find_car_by_id(str(ford_id)))

# Update car info for the Toyota with ID "1"
update_result = myCarSystem.update_car_info(
    "1", name="Toyota Corolla", year=2019, price=38000
)
print("Update Result \n", update_result)

# Display the updated list
print("Updated Car List \n", myCarSystem.display_all_cars())

# Delete a car by ID
delete_result = myCarSystem.delete_car("3")
print("Delete Result \n", delete_result)

# Display the list after deletion
print("Car List After Deletion \n", myCarSystem.display_all_cars())
