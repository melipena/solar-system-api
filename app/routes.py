
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
    name_query_value = request.args.get("name")
    if name_query_value is not None:
        planets = Planet.query.filter_by(name=name_query_value)
    else:
        planets = Planet.query.all()

    result = []
    
    for planet in planets:
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

@planets_bp.route('<planet_id>', methods=['PUT'])
def update_one_planet(planet_id):
    update_planet = get_planet_from_id(planet_id)

    request_body = request.get_json()

    try:
        update_planet.name = request_body["name"]
        update_planet.description = request_body["description"]
        update_planet.num_moon = request_body["num_moon"]
    except KeyError:
        return jsonify({"msg": "Missing attributes"}), 400
    
    db.session.commit()
    return jsonify({"msg": f"Successfully updated planet with id {update_planet.id}"}), 200

@planets_bp.route('/<planet_id>', methods=['DELETE'])
def delete_one_planet(planet_id):
    planet_to_delete = get_planet_from_id(planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return jsonify({"msg": f"Successfully deleted planet with id {planet_to_delete.id}"}), 200        

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

    