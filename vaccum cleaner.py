def vacuum_cleaner_agent():
    """
    Simulates a simple intelligent vacuum cleaner agent for a 2-room environment.
    """
    
    # --- Helper function to get valid user input ---
    def get_room_status(room_name):
        """
        Prompts the user for a room's status and ensures valid input.
        """
        while True:
            # Task 2.1: Take input for the status of each room 
            status = input(f"Enter status for Room {room_name} (Dirty/Clean): ").strip().title()
            
            # Use startswith for flexibility (e.g., 'D', 'd', 'Dirty', 'dirty')
            if status.startswith('D'):
                return 'Dirty'
            elif status.startswith('C'):
                return 'Clean'
            else:
                print("Invalid input. Please enter 'Dirty' or 'Clean'.")

    # --- Initialization ---
    
    # 1. Get initial state from the user
    room_status = {
        'A': get_room_status('A'),
        'B': get_room_status('B')
    }
    
    # 2. Set initial condition: Vacuum starts in location A 
    current_location = 'A'
    
    print("\n--- Simulation Started ---")
    print(f"Initial State: {room_status}")
    print(f"Vacuum is starting in Room {current_location}.\n")

    # --- Main Agent Loop ---
    # The process continues until both rooms are clean 
    while not (room_status['A'] == 'Clean' and room_status['B'] == 'Clean'):
        
        print(f"Vacuum is in Room {current_location}.")
        
        # Rule 1: If the current room is dirty, the vacuum cleans it 
        if room_status[current_location] == 'Dirty':
            print(f"Room {current_location} is Dirty. ACTION: Suck dirt.")
            # Update the state
            room_status[current_location] = 'Clean'
            print(f"New State: {room_status}")
        
        # Rule 2: If the current room is clean, it moves to the other room 
        else:
            print(f"Room {current_location} is Clean. ACTION: Move.")
            # Move to the other room
            if current_location == 'A':
                current_location = 'B'
            else:
                current_location = 'A'
                
        print("-" * 25) # Separator for clarity

    # --- Goal State ---
    # Task 2.3: Print the final goal state 
    print("\n--- Simulation Complete ---")
    print("Goal State Reached: Both rooms are clean.")
    print(f"Final State: {room_status}")

# This line calls the function to run the simulation
# when you execute the script.
if __name__ == "__main__":
    vacuum_cleaner_agent()