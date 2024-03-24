#!/usr/bin/env python3

from vehicle_factory import VehicleFactory

def main():
  # Create a vehicle factory
  factory = VehicleFactory()

  # Produce vehicles
  ford_f150 = factory.produce_vehicle("Ford", "F-150", 2022, "Red", 5.0, 400, 5)
  mustang = factory.produce_vehicle("Ford", "Mustang", 2021, "Blue", 5.0, 450, 4)
  toyota_camry = factory.produce_vehicle("Toyota", "Camry", 2020, "White", 2.5, 206, 5)
  honda_civic = factory.produce_vehicle("Honda", "Civic", 2019, "Black", 1.5, 174, 5)

  # Display vehicle information
  ford_f150.display_info()
  print("---")
  mustang.display_info()
  print("---")
  toyota_camry.display_info()
  print("---")
  honda_civic.display_info()

if __name__ == "__main__":
  main()
