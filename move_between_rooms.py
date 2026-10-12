"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# Create the gameplay loop required by the milestone.
game_over = False

# Output player instructions for the simplified movement prototype.
print("Simplified Text Adventure Game\n")
print("Move around the game rooms.")
print("Move commands: 'go North', 'go South', 'go East', 'go West'")
print("Type 'exit' to end the game.\n")
print("*" * 30)

# Gameplay loop for the simplified movement prototype.
while not game_over:
    # Display current room.
    print(f"You are in the {current_room}.")

    # Prompt for a movement command or "exit".
    command = input("Enter command:\n>").strip().lower().split()

    # Check for exit command.
    if command[0] == "exit":
        game_over = True
        print("Thanks for playing!")
        break

    # Check for valid movement command.
    if len(command) == 2 and command[0] == "go" and command[1] in ["north", "south", "east", "west"]:
        direction = command[1]
        if direction in rooms[current_room]:
            # Update current room.
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.")
    else:
        print("Invalid command.")

    print("*" * 30)
