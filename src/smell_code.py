class DataProcessor:
    # Smell: Large class with too many methods and attributes
    def load_data(self):
        pass

    def validate_data(self):
        pass

    def process_data1(self):
        pass

    def process_data2(self):
        pass

def calculate_area(length, width):
    return length * width

def calculate_surface_area(length, width, height):
    # Smell: Duplicate code for calculating area
    base_area = length * width
    side_area = height * width
    return 2 * (base_area + side_area)

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_full_address(self):
        # Smell: Feature envy - this method is more interested in the Address class
        return f"{self.address.street}, {self.address.city}"

def process_data(data):
    # Smell: Long method doing various things
    # ...
    # lots of code here processing data
    # ...
    # even more code here
    # ...
    return processed_data
