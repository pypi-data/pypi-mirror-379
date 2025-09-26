from typing import Union

class CellProperty:
    """
    Represents a property that can be assigned to a cell type.

    :param name: Name of the property.
    :type name: str
    :param value: Value of the property (str, bool, int, or float).
    :type value: str | bool | int | float
    """
    def __init__(self, name: str, value: Union[str, bool, int, float]):
        """
        Initialize a CellProperty.

        :param name: Name of the property.
        :type name: str
        :param value: Value of the property (str, bool, int, or float).
        :type value: str | bool | int | float
        """
        if not isinstance(value, (str, bool, int, float)):
            raise TypeError("value must be of type str, bool, int, or float")
        self.name = name
        self.value = value

class CellProperties(dict):
    """
    A dictionary-like container for CellProperty objects.

    Inherits from dict. Accepts dict or iterable of (name, CellProperty) pairs.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize CellProperties.

        :param args: Arguments for dict initialization.
        :param kwargs: Keyword arguments for dict initialization.
        """
        super().__init__(*args, **kwargs)

    def add(self, property: CellProperty):
        """
        Add a CellProperty to the collection.

        :param property: The CellProperty to add.
        :type property: CellProperty
        """
        self[property.name] = property

    def get(self, name: str) -> 'CellProperty | None':
        """
        Get a CellProperty by name.

        :param name: Name of the property.
        :type name: str
        :return: The CellProperty if found, else None.
        :rtype: CellProperty or None
        """
        return super().get(name, None)

    def remove(self, name: str):
        """
        Remove a CellProperty by name.

        :param name: Name of the property to remove.
        :type name: str
        """
        if name in self:
            del self[name]

    def __repr__(self):
        """
        Return a string representation of the CellProperties object.

        :return: String representation.
        :rtype: str
        """
        return f"CellProperties({len(self)} properties)"
    
    @property
    def n(self):
        """
        Return the number of properties.

        :return: Number of properties.
        :rtype: int
        """
        return len(self)

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create CellProperties from a dictionary.

        :param data: Dictionary of property names and values.
        :type data: dict
        :return: CellProperties instance.
        :rtype: CellProperties
        """
        props = cls()
        for name, value in data.items():
            props.add(CellProperty(name, value))
        return props

    def copy(self):
        """
        Return a shallow copy of the CellProperties.

        :return: A copy of the CellProperties.
        :rtype: CellProperties
        """
        return CellProperties(super().copy())

    def __eq__(self, value):
        """
        Check equality with another CellProperties object.

        :param value: Object to compare.
        :type value: Any
        :return: True if equal, False otherwise.
        :rtype: bool
        """
        if not isinstance(value, CellProperties):
            return False
        return dict(self) == dict(value)

    def number_of_properties(self) -> int:
        """
        Return the number of properties.

        :return: Number of properties.
        :rtype: int
        """
        return len(self)
