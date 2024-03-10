import random
import time
import math
import json
import requests


class Spaceship:
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = fuel
        self.health = health

    def __str__(self):
        return f"Spaceship's name: {self.name}: Fuel level:{self.fuel}, Health rate:{self.health}"


def launch_spaceship(name):
    print(f"Launching {name}")
    time.sleep(3)
    print(f"{name} launched")


def encounter_event(spaceship):
    event = random.choice(["Asteroid Field", "Space Pirates", "Alien Diplomacy", "Black Hole"])
    print(f"{spaceship.name} Encountering {event}")
    time.sleep(10)
    if event == "Black Hole":
        spaceship.health -= 50
    else:
        spaceship.health -= 20
    print(f"{spaceship.name} new health rate is {spaceship.health}")


def fetch_galactic_weather():
    try:
        #response = requests.get("http://api.openweathermap.org/data/2.5/weather?")
        #response.raise_for_status()  # Raises an HTTPError for bad responses
        #weather_data = response.json()
        #weather = weather_data.get("weather", "unknown")  # Default to 'unknown' if not found
        weather = random.choice(["sunny", "windy", "cloudy", "rainy", "partly cloudy", "snowing"])
        print(f"Galactic weather is {weather}")
        return weather
    except requests.RequestException as e:
        print(f"Failed to fetch galactic weather: {e}")
        return "error"


def explore_galaxy(spaceship):
    exploring = True
    while exploring and spaceship.fuel > 0:
        spaceship.fuel -= 10
        print(f"{spaceship.name} is Exploring new sector, Fuel remaining: {spaceship.fuel}")

        encounter_event(spaceship)
        if spaceship.health > 0:
            print(f"{spaceship.name} survived")
        else:
            print(f"{spaceship.name} has been destroyed")
            break

        choice = input("Do you want to continue exploring? (yes/no): ")
        if choice == 'no':
            exploring = False

    if spaceship.fuel <= 0:
        print(f"{spaceship.name} ran out of fuel")
    else:
        print(f"{spaceship.name} Returning to base")


def save_game(player_spaceship):
    game_data = {
        "name": player_spaceship.name,
        "fuel": player_spaceship.fuel,
        "health": player_spaceship.health
    }
    with open("game_save.json", "w") as file:
        json.dump(game_data, file)
    print("Game saved.")


def load_game(player_spaceship):
    with open("game_save.json", "r") as file:
        game_data = json.load(file)
    player_spaceship.name = game_data["name"]
    player_spaceship.fuel = game_data["fuel"]
    player_spaceship.health = game_data["health"]
    print("Game loaded.")
    return player_spaceship


def start_new_day(player_spaceship):
    print("A new day begins in the galaxy")
    weather = fetch_galactic_weather()
    choice = input("Do you want to start playing today? (yes/no): ")
    if choice == 'yes':
        return True
    else:
        return False


def main():

    print("Welcome to Galactic Spaceship")
    player_spaceship = Spaceship("Galactic Spaceship", 100, 100)
    choice = input("do you want to load a previously saved game state? (yes/no):")
    if choice == "yes":
        player_spaceship = load_game(player_spaceship)
    print(player_spaceship.__str__())

    while True:
        start_game = start_new_day(player_spaceship)
        if not start_game:
            continue
        launch_spaceship(player_spaceship.name)
        explore_galaxy(player_spaceship)

        if player_spaceship.health <= 0 or player_spaceship.fuel <= 0:
            break

        choice = input("do you want to save this game state? (yes/no):")
        if choice == "yes":
            save_game(player_spaceship)

    print("Game over, Goodbye")


if __name__ == "__main__":
    main()
