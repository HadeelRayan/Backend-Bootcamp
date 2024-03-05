
def main():
    garden = {
        "Tulip": {"sun": "Yes", "rain": "No", "water": "Medium", "wind": "No", "snow level": 6},
        "Lily": {"sun": "Yes", "rain": "No", "water": "High", "wind": "Yes", "snow level": 7},
        "Rose": {"sun": "No", "rain": "Yes", "water": "Low", "wind": "No", "snow level": 5}
    }

    weather_today = input("Describe the weather today sunny or cloudy: ")
    precipitation = int(input("enter precipitation level from 1 to 10: "))
    wind = input("Is it windy today? , please answer Yes or No: ")
    snow_level = int(input("please enter Snow level from 1 to 10: "))

    print("Plants that likes this conditions:")
    for plant, conditions in garden.items():
        if conditions["sun"] == "Yes" and weather_today == "sunny" or (conditions["sun"] == "No" and weather_today == "cloudy"):
            if precipitation <= 3 and conditions["water"] == "Low":
                if wind == conditions["wind"]:
                    print(plant)
                else:
                    print(plant)
            elif 3 < precipitation <= 6 and conditions["water"] == "Medium":
                if wind == conditions["wind"]:
                    print(plant)
                else:
                    print(plant)
            elif 6 < precipitation and conditions["water"] == "High":
                if wind == conditions["wind"]:
                    print(plant)
                else:
                    print(plant)
                    
    print("Plants that cannot survive the snow level:")
    for plant, conditions in garden.items():
        if snow_level > conditions["snow level"]:
            print(plant)


if __name__ == "__main__":
    main()