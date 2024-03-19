import json
from roads_utils import Road, AsphaltRoad, GravelRoad, MudRoad, SnowRoad, NewRoadType
import truck_utils as tr


road_type_registry = {
    "Asphalt": AsphaltRoad,
    "Gravel": GravelRoad,
    "Mud": MudRoad,
    "Snow": SnowRoad,
}


def load_roads_from_file(file_path):
    with open(file_path, 'r') as file:
        road_data = json.load(file)

    roads = []
    for road_segment in road_data:
        road_type = road_segment["road_type"]
        length = road_segment["length"]
        road_class = create_road(road_type)

        roads.append((road_class, length))

    return road_data


road_types_config = load_roads_from_file(file_path='road_types_config.json')


def create_road(road_type, road_types_config):
    if road_type in road_types_config:
        name = road_type.
        terrain_hardness = terrain_hardness
        mental_effect = mental_effect
        wheel_damage_effect = wheel_damage_effect
        return Road(name, terrain_hardness, mental_effect, wheel_damage_effect)
    else:
        raise ValueError(f"Unknown road type: {road_type}")
