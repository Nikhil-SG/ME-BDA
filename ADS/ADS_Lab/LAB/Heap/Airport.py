class Event:
    def __init__(self, timestamp, aircraft_number, event_type):
        self.timestamp = timestamp
        self.aircraft_number = aircraft_number
        self.event_type = event_type

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class AirTrafficControlSimulation:
    def __init__(self):
        self.event_queue = []

    def insert_event(self, timestamp, aircraft_number, event_type):
        new_event = Event(timestamp, aircraft_number, event_type)
        self.event_queue.append(new_event)
        self.event_queue.sort()  

    def extract_next_event(self):
        if self.event_queue:
            return self.event_queue.pop(0)  
        else:
            return None  

if __name__ == "__main__":
    sim = AirTrafficControlSimulation()
    sim.insert_event(10, 'A123', 'takeoff')
    sim.insert_event(2, 'B700', 'landing')
    sim.insert_event(5, 'C789', 'takeoff')
    sim.insert_event(5, 'B456', 'landing')
    sim.insert_event(8, 'C666', 'takeoff')
    sim.insert_event(1, 'A111', 'landing')
    sim.insert_event(3, 'B222', 'takeoff')
    
    next_event = sim.extract_next_event()
    while next_event:
        print(f"Next Event: Time={next_event.timestamp}, Aircraft={next_event.aircraft_number}, Type={next_event.event_type}")
        next_event = sim.extract_next_event()
