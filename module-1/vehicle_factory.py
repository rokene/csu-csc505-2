from vehicle import Vehicle

class VehicleFactory:
    def produce_vehicle(self, make, model, year, color, engine_size, horsepower, seating_capacity):
        return Vehicle(make, model, year, color, engine_size, horsepower, seating_capacity)
