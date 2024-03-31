from ddd.domain.model.entity import Entity


class Vehicle(Entity):
    def __init__(self, id, color):
        self.id = id
        self.color = color

    def __eq__(self, other):
        if not isinstance(other, Vehicle):
            return False
        return self.id == other.id and self.color == other.color
