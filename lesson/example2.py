class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def display_temperature(self):
        fahrenheit = self.celsius_to_fahrenheit()
        print(f"Temperature: {self.celsius}°C = {fahrenheit}°F")


# Example usage
temperature_celcius = 25
temperature = Temperature(temperature_celcius)
temperature.display_temperature()
