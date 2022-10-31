from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planet import Planet

# class Planet():
#     def __init__(self, id, name, description, num_satellite):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_satellite = num_satellite

# planets = [
#     Planet(1, "Mercury", "mostly of rock", 0),
#     Planet(2, "Venus", "temperature is higher than 850F", 0),
#     Planet(3, "Earth", "our planet", 1),
#     Planet(4, "Mars", "red planet", 2),
#     Planet(5, "Jupiter", "gas giant planet", 63),
#     Planet(6, "Saturn", "most colorful planet", 56),
#     Planet(7, "Uranus", "night and day lasts 42 years", 21),
#     Planet(8, "Neptune", "most distant planet", 13)
# ]

planets_bp = Blueprint("planets", __name__,url_prefix="/planets")
@planets_bp.route('', methods=['GET'])
def get_all_planets():
    result = []
    all_planets= Planet.query.all()
    for planet in all_planets:

        result.append(planet.to_dict())

    return jsonify(result), 200

@planets_bp.route('/<planet_id>', methods = ['GET'])
def get_one_planet(planet_id):

    chosen_planet = get_planet_from_id(planet_id)

    return jsonify(chosen_planet.to_dict()), 200

@planets_bp.route('', methods=['POST'])
def create_one_planet():
    request_body = request.get_json()

    new_planet = Planet(name= request_body['name'], 
                        description=request_body['description'],
                        num_moon=request_body['num_moon']
                        )
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({'msg': f"Successfully created Planet with id= {new_planet.id}"}, 201)

# Helper function
def get_planet_from_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({"msg": f"invalid data type: {planet_id}"},400))

    chosen_planet = Planet.query.get(planet_id)
        
    if chosen_planet is None:
        return abort(make_response({"msg": f"Could not find the planet with the id: {planet_id}"}, 404))
    
    return chosen_planet

    