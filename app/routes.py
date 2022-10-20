from flask import Blueprint

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


