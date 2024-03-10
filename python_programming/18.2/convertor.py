def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


def c_to_f(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit


def mph_to_kph(mph):
    kph = mph * 1.6
    return kph


def kph_to_mph(kph):
    mph = kph / 1.6
    return mph


def kg_to_stone(kg):
    stone = kg * 0.15
    return stone


def stone_to_kg(stone):
    kg = stone / 0.15
    return kg


def kg_to_lbs(kg):
    lbs = kg * 2.2
    return lbs


def lbs_to_kg(lbs):
    kg = lbs / 2.2
    return kg


def stone_to_lbs(stone):
    lbs = stone * 14
    return lbs


def lbs_to_stone(lbs):
    stone = lbs / 14
    return stone


def main():
    type_of_conversion = input("type of conversion is: \n1. f to c \n2. c to f \n3. mph to kph \n4. kph to mph "
                               "\n5. kg to stone \n6. stone to kg \n7. kg to lbs \n8. lbs to kg "
                               "\n9. stone to lbs \n10. lbs to  stone \n")

    value = float(input("value is: "))

    print(type_of_conversion)
    if type_of_conversion == '1':
        c = f_to_c(value)
        print(f"your converted value is {c}")
    elif type_of_conversion == '2':
        f = c_to_f(value)
        print(f"your converted value is {f}")
    elif type_of_conversion == '3':
        kph = mph_to_kph(value)
        print(f"your converted value is {kph}")
    elif type_of_conversion == '4':
        mph = kph_to_mph(value)
        print(f"your converted value is {mph}")
    elif type_of_conversion == '5':
        stone = kg_to_stone(value)
        print(f"your converted value is {stone}")
    elif type_of_conversion == '6':
        kg = stone_to_kg(value)
        print(f"your converted value is {kg}")
    elif type_of_conversion == '7':
        lbs = kg_to_lbs(value)
        print(f"your converted value is {lbs}")
    elif type_of_conversion == '8':
        kg = lbs_to_kg(value)
        print(f"your converted value is {kg}")
    elif type_of_conversion == '9':
        lbs = stone_to_lbs(value)
        print(f"your converted value is {lbs}")
    elif type_of_conversion == '10':
        stone = lbs_to_stone(value)
        print(f"your converted value is {stone}")
    else:
        print("error")


if __name__ == "__main__":
    main()