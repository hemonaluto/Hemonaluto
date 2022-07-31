"""Element module"""
import json


class Element:
    """Class to initialize any element with its own name and description"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.visible = True

    def __iter__(self):
        yield from {
            "name": self.name,
            "description": self.description,
            "visible": self.visible
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """Serialize self"""
        return self.__str__()
