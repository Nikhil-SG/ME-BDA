class Node:
    def __init__(self, event_data, event_time, event_name, num_guests):
        self.event_data = event_data
        self.event_time = event_time
        self.event_name = event_name
        self.num_guests = num_guests
        self.left = None
        self.right = None

class EventManager:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add_event(self, event_data, event_time, event_name, num_guests):
        def add_event_helper(node, event_data, event_time, event_name, num_guests):
            if node is None:
                return Node(event_data, event_time, event_name, num_guests)

            if event_time < node.event_time:
                # Check for minimum time gap
                if node.event_time - event_time < 3:
                    return None  # Cannot add event due to time conflict
                node.left = add_event_helper(node.left, event_data, event_time, event_name, num_guests)
            elif event_time > node.event_time:
                # Check for minimum time gap
                if event_time - node.event_time < 3:
                    return None  # Cannot add event due to time conflict
                node.right = add_event_helper(node.right, event_data, event_time, event_name, num_guests)
            else:
                return None  # Cannot add two events at the same time

            # Check for maximum events per day
            if node.left and node.right:
                return None  # Cannot add more events on this day

            return node

        self.root = add_event_helper(self.root, event_data, event_time, event_name, num_guests)

    def cancel_event(self, event_time):
        def cancel_event_helper(node, event_time):
            if node is None:
                return None

            if event_time < node.event_time:
                node.left = cancel_event_helper(node.left, event_time)
            elif event_time > node.event_time:
                node.right = cancel_event_helper(node.right, event_time)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.event_data = successor.event_data
                    node.event_time = successor.event_time
                    node.event_name = successor.event_name
                    node.num_guests = successor.num_guests
                    node.right = cancel_event_helper(node.right, successor.event_time)

            return node

        self.root = cancel_event_helper(self.root, event_time)

    def display_events_descending_order(self):
        def in_order_descending(node):
            if node is None:
                return
            in_order_descending(node.right)
            print(f"Event Time: {node.event_time}, Event Name: {node.event_name}, Number of Guests: {node.num_guests}")
            in_order_descending(node.left)

        in_order_descending(self.root)

    def delete_completed_events(self):
        def delete_completed_events_helper(node):
            if node is None:
                return None

            node.left = delete_completed_events_helper(node.left)
            node.right = delete_completed_events_helper(node.right)

            if node.event_data is None:  # Assuming event data is None if completed
                return None

            return node

        self.root = delete_completed_events_helper(self.root)

if __name__ == "__main__":
    event_manager = EventManager()

    # Add events
    event_manager.add_event("Meeting", 9, "Project Meeting", 3)
    event_manager.add_event("Class", 9, "ADS Class", 30)
    event_manager.add_event("Workshop", 14, "Gen AI Workshop", 30)
    event_manager.add_event("Exam", 19, "ADS Exam", 30)  # This event will be rejected due to time conflict

    # Display events
    print("Events:")
    event_manager.display_events_descending_order()

    # Cancel an event
    event_manager.cancel_event(14)  # Cancel the workshop

    # Display events after cancellation
    print("\nEvents after cancellation:")
    event_manager.display_events_descending_order()

    # Delete completed events (assuming event_data is None for completed)
    event_manager.delete_completed_events()

    # Display events after deletion
    print("\nEvents after deleting completed events:")
    event_manager.display_events_descending_order()