import random


def negotiation(materials_list, alien_delegations):

    num_convinced = 0

    for alien in alien_delegations:
        print(f"\nalien delegation {alien['name']}:")
        suggestions_left = alien["num_suggestions"]

        while suggestions_left > 0:
            suggested_material = random.choice(materials_list)
            print(f"Suggestion: {suggested_material}")
            if suggested_material in alien["needed_materials"]:
                print("Cooperation achieved.")
                num_convinced += 1
                break
            else:
                print("Trying another suggestion.")
                suggestions_left -= 1

        if suggestions_left == 0:
            print("Failed to convince. Moving to the next delegation.")

    return num_convinced


def main():

    materials_list = [
        "Quantum Crystals", "Plasma Cells", "Neutronium Alloy", "Dark Matter", "Solarite",
        "Gravitonium", "Chronoton Particles", "Nanofibers", "Synthium", "Bio-Organic Gels",
        "Quantum Flux Capacitors", "Hyperium", "Exotic Matter", "Ethereal Energy Crystals",
        "Chronal Steel", "Photonic Resonators", "Voidstone", "Psionic Residue", "Arcane Crystals",
        "Neutrino Disruptors"
    ]

    alien_delegations = [
        {"name": "Zorthian Collective", "needed_materials": random.sample(materials_list, 2), "num_suggestions": 2},
        {"name": "Quasar Consortium", "needed_materials": random.sample(materials_list, 2), "num_suggestions": 3},
        {"name": "Xylurian Union", "needed_materials": random.sample(materials_list, 2), "num_suggestions": 2},
        {"name": "Draconian Empire", "needed_materials": random.sample(materials_list, 2), "num_suggestions": 3}
    ]

    num_convinced = negotiation(materials_list, alien_delegations)
    percentage_convinced = (num_convinced / len(alien_delegations)) * 100

    for alien in alien_delegations:
        if set(alien['needed_materials']).intersection(set(materials_list)):
            print(f"{alien['name']}: {'Convinced'}")
        else:
            print(f"{alien['name']}: {'Not Convinced'}")

    if percentage_convinced >= 70:
        print("Negotiation successful")
    else:
        print("Negotiation failed")


if __name__ == "__main__":
    main()
