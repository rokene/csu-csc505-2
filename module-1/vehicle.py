class Vehicle:
  def __init__(self, make, model, year, color, engine_size, horsepower, seating_capacity):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self.engine_size = engine_size
    self.horsepower = horsepower
    self.seating_capacity = seating_capacity

  def display_info(self):
    print(f"Make: {self.make}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")
    print(f"Color: {self.color}")
    print(f"Engine Size: {self.engine_size}L")
    print(f"Horsepower: {self.horsepower} HP")
    print(f"Seating Capacity: {self.seating_capacity} passengers")
