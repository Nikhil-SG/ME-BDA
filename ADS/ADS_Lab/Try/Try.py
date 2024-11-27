class Vehicle:
    def __init__(self, vehicle_number, vehicle_type, valet_amount):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.valet_amount = valet_amount
        self.two_way_code = 0  # Initialize two-way code to 0

    def toll_rate(self):
        rates = {
            'car': 40,
            'LCV': 70,
            'Bus': 150,
            'two_wheeler': 0
        }
        return rates.get(self.vehicle_type, 0)


class TollCollectionSystem:
    def __init__(self):
        self.vehicles = {}

    def register_vehicle(self, vehicle_number, vehicle_type, valet_amount):
        if vehicle_number not in self.vehicles:
            self.vehicles[vehicle_number] = Vehicle(vehicle_number, vehicle_type, valet_amount)

    def vehicle_present(self, vehicle_number):
        if vehicle_number not in self.vehicles:
            # Create vehicle if not present
            print(f"Vehicle {vehicle_number} not found. Registering...")
            self.register_vehicle(vehicle_number, 'car', 0)  # Default values for registration
        return self.vehicles[vehicle_number]

    def first_toll(self, vehicle_number, vehicle_type, way):
        vehicle = self.vehicle_present(vehicle_number)
        vehicle.vehicle_type = vehicle_type  # Update vehicle type if necessary
        toll = vehicle.toll_rate()

        if way == 'two-way':
            toll *= 1.8  # Apply 1.8 times toll for two-way
            vehicle.two_way_code = 1  # Set two-way code
        else:
            vehicle.two_way_code = 0  # Reset two-way code for one-way

        if vehicle.valet_amount >= toll:
            vehicle.valet_amount -= toll
            return way
        else:
            raise ValueError("Insufficient valet amount for toll payment.")

    def sec_to_toll(self, vehicle_number):
        vehicle = self.vehicle_present(vehicle_number)
        if vehicle.two_way_code == 1:
            # Reset two-way code after return journey
            vehicle.two_way_code = 0
            return "Two-way toll paid."
        else:
            return "One-way toll paid."


# Example usage
if __name__ == "__main__":
    toll_system = TollCollectionSystem()

    # Register vehicles
    toll_system.register_vehicle('ABC123', 'car', 100)

    # First toll payment
    try:
        way = toll_system.first_toll('ABC123', 'car', 'two-way')
        print(f"First toll for {way}: {toll_system.vehicles['ABC123'].valet_amount} left in valet.")
        
        # Check second toll
        print(toll_system.sec_to_toll('ABC123'))
        print(f"Valet amount after return: {toll_system.vehicles['ABC123'].valet_amount} left in valet.")
        
    except ValueError as e:
        print(e)
