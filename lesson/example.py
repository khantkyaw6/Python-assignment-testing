temperature_celcius = 25


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def display_temperature(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature: {celsius} * C = {fahrenheit} F")


display_temperature(temperature_celcius)
