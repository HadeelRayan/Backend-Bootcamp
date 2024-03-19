class Road:
    def __init__(self, name, terrain_hardness, mental_effect, wheel_damage_effect):
        self.name = name
        self.terrain_hardness = terrain_hardness
        self.mental_effect = mental_effect
        self.wheel_damage_effect = wheel_damage_effect


class AsphaltRoad(Road):
    def __init__(self):
        super().__init__("Asphalt", terrain_hardness=1, mental_effect=2, wheel_damage_effect=0.1)


class GravelRoad(Road):
    def __init__(self):
        super().__init__("Gravel", terrain_hardness=3, mental_effect=-1, wheel_damage_effect=0.5)


class MudRoad(Road):
    def __init__(self):
        super().__init__("Mud", terrain_hardness=5, mental_effect=-3, wheel_damage_effect=1)


class SnowRoad(Road):
    def __init__(self):
        super().__init__("Snow", terrain_hardness=4, mental_effect=-2, wheel_damage_effect=0.7)


class NewRoadType(Road):
    def __init__(self):
        super().__init__("NewRoadType", terrain_hardness=?, mental_effect=?, wheel_damage_effect=?)
