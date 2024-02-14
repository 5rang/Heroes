print("Welcome to the Heroes III game!")
print("In this game, you will choose a hero and embark on a quest to save the kingdom.")
print("The hero you choose will determine your starting stats and abilities.")
print("Choose wisely and good luck on your quest!\n")

heroes = {
    "Warrior": {"strength": 10, "intelligence": 6, "speed": 7},
    "Mage": {"strength": 5, "intelligence": 10, "speed": 8},
    "Archer": {"strength": 7, "intelligence": 8, "speed": 10}
}

while True:
    print("Select a hero:")
    for hero in heroes:
        print(f"{hero}: strength={heroes[hero]['strength']}, intelligence={heroes[hero]['intelligence']}, speed={heroes[hero]['speed']}")
    choice = input("Enter your choice (Warrior/Mage/Archer): ")

    if choice not in heroes:
        print("Invalid choice, try again.\n")
        continue
    else:
        break

hero = heroes[choice]
print(f"You have chosen the {choice}.")
print(f"Strength: {hero['strength']}")
print(f"Intelligence: {hero['intelligence']}")
print(f"Speed: {hero['speed']}")

print("\nYour quest begins now. You must navigate through a dangerous forest to reach the castle and save the kingdom.")
print("On your journey, you will encounter different obstacles.")
print("You will use your stats and abilities to overcome these obstacles and reach the castle.\n")
print(f"You have chosen the {choice}.")
print(f"Strength: {hero['strength']}")
print(f"Intelligence: {hero['intelligence']}")
print(f"Speed: {hero['speed']}")
obstacles = {
    "Goblin ambush": {"strength": 8, "intelligence": 6, "speed": 10},
    "Trap-filled maze": {"strength": 5, "intelligence": 10, "speed": 7},
    "Dragon attack": {"strength": 10, "intelligence": 5, "speed": 8}
}

while True:
    print("You have encountered an obstacle:")
    for obstacle in obstacles:
        print(obstacle)
    choice = input("Enter your choice (Goblin ambush/Trap-filled maze/Dragon attack): ")

    if choice not in obstacles:
        print("Invalid choice, try again.\n")
        continue
    else:
        break

obstacle = obstacles[choice]
print(f"You have chosen to face the {choice}.")
print(f"Strength required: {obstacle['strength']}")
print(f"Intelligence required: {obstacle['intelligence']}")
print(f"Speed required: {obstacle['speed']}")

if hero["strength"] >= obstacle["strength"] and hero["intelligence"] >= obstacle["intelligence"] and hero["speed"] >= obstacle["speed"]:
    print(f"\nYou have successfully overcome the {choice}.")
else:
    print(f"\nYou were not strong enough to overcome the {choice}.")
    print("Your quest has failed.")
    print("Game Over.")
    exit()

print("\nYou continue your journey and reach the castle.")
print("You defeat the evil tyrant and save the kingdom.")
print("Congratulations, you have completed your quest
