class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, price_to_repair_wheels_per_km, brand):
        self.max_fuel_amount = max_fuel_amount  # Maximum fuel capacity in liters
        self.km_per_liter = km_per_liter  # Fuel efficiency: kilometers per liter
        self.price_to_repair_wheels_per_km = price_to_repair_wheels_per_km
        self.brand = brand
        self.current_fuel = max_fuel_amount
        self.wheel_damage = 0
        self.mental_health = 100

    def drive(self, distance, road):
        fuel_needed = distance / self.km_per_liter
        if fuel_needed > self.current_fuel:
            print("Not enough fuel")
            return False

        # Update truck's state
        self.current_fuel -= fuel_needed
        self.wheel_damage += distance * road.wheel_damage_effect
        self.mental_health += road.mental_effect
        self.mental_health = max(0, min(100, self.mental_health))
        print(f"Completed driving {distance} km on {road.name}, Fuel left: {self.current_fuel:.2f} liters,"
              f" Wheel damage: {self.wheel_damage:.2f}, Mental health: {self.mental_health}%")
        return True

    def repair_wheels(self):
        cost = self.wheel_damage * self.price_to_repair_wheels_per_km
        self.wheel_damage = 0
        print(f"Wheels repaired. Cost: ${cost:.2f}")

    def refuel(self):
        needed_fuel = self.max_fuel_amount - self.current_fuel
        self.current_fuel = self.max_fuel_amount
        print(f"Truck refueled with {needed_fuel} liters.")

