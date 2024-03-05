
def set_of_rules(users, user_profile):
    for user in users:
        if (user["gender"] != user_profile["gender"] and
                20 <= user["age"] <= 30 and
                user["favorite_food"] in [user_profile["favorite_food"], "Burger"]):
            return user["name"]
    return None


def create_user():
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = int(input("Enter your age: "))
    profession = input("Enter your profession: ")
    favorite_tv_show = input("Enter your favorite TV show: ")
    favorite_food = input("Enter your favorite food: ")

    user_profile = {
        "name": name,
        "gender": gender,
        "age": age,
        "profession": profession,
        "favorite_tv_show": favorite_tv_show,
        "favorite_food": favorite_food
    }
    return user_profile


def main():
    users = [
        {
            "name": "Abed",
            "gender": "male",
            "age": 26,
            "profession": "Engineer",
            "favorite_tv_show": "Breaking bad",
            "favorite_food": "Burger"
        },
        {
            "name": "Adham",
            "gender": "male",
            "age": 25,
            "profession": "Engineer",
            "favorite_tv_show": "Game of Thrones",
            "favorite_food": "Pizza"
        },
        {
            "name": "Yasmeen",
            "gender": "female",
            "age": 23,
            "profession": "Engineer",
            "favorite_tv_show": "Friends",
            "favorite_food": "Burger"
        },
        {
            "name": "Hadeel",
            "gender": "female",
            "age": 24,
            "profession": "Engineer",
            "favorite_tv_show": "Dark",
            "favorite_food": "Burger"
        }
    ]

    user_profile = create_user()
    matched_profile = set_of_rules(users, user_profile)

    if matched_profile:
        print("You matched with", matched_profile)
    else:
        print("no match found")


if __name__ == "__main__":
    main()
