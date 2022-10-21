from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, num_satellite):
        self.id = id
        self.name = name
        self.description = description
        self.num_satellite = num_satellite

planets = [
    Planet(1, "Mercury", "mostly of rock", 0),
    Planet(2, "Venus", "temperature is higher than 850F", 0),
    Planet(3, "Earth", "our planet", 1),
    Planet(4, "Mars", "red planet", 2),
    Planet(5, "Jupiter", "gas giant planet", 63),
    Planet(6, "Saturn", "most colorful planet", 56),
    Planet(7, "Uranus", "night and day lasts 42 years", 21),
    Planet(8, "Neptune", "most distant planet", 13)
]

planets_bp = Blueprint("planets", __name__,url_prefix="/planets")
@planets_bp.route('', methods=['GET'])
def get_all_planets():
    result = []
    for planet in planets:
        planet_dict = {"id":planet.id, "name":planet.name,
                    "description":planet.description, 
                    "num_satellite":planet.num_satellite}
        result.append(planet_dict)

    return jsonify(result), 200

@planets_bp.route('/<planet_id>', methods = ['GET'])
def get_one_planet(planet_id):

    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"msg": f"invalid data type: {planet_id}"}),400
        
    chosen_planet = None
    for planet in planets:
        if planet.id == planet_id:
            chosen_planet = planet 
    if chosen_planet is None:
        return jsonify({"msg": f"Could not find the planet with the id: {planet_id}"}), 404

    return_chosen_planet = {
        "id": chosen_planet.id,
        "name": chosen_planet.name,
        "description": chosen_planet.description,
        "num_satellite": chosen_planet.num_satellite
    }

    return jsonify(return_chosen_planet), 200