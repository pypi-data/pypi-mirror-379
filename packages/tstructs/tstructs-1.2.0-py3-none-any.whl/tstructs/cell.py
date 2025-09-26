from .properties import CellProperties, CellProperty

class Cell:
    def __init__(self, type:int, name:str, group:int, properties:CellProperties=None):
        """
        Initialize a Cell.

        :param name: The name of the cell.
        :param type: The type index of the cell.
        :type type: int
        :param group: The group index of the cell.
        :type group: int
        :param properties: The properties associated with the cell.
        :type properties: CellProperties or None
        """
        self.type = type
        self.name = name
        self.group = group
        self.properties = properties

if __name__ == "__main__":
    print("Testing module Cell.py ...")

    # Example 1: Cell with no properties
    air_cell = Cell(type=0, name="Air", group=0)

    # Example 2: Cell with a single property
    solid_cell = Cell(
        type=1,
        name="Stone",
        group=0,
        properties=CellProperties({
            "hardness": CellProperty("hardness", 10)
        })
    )

    # Example 3: Cell with multiple properties
    water_cell = Cell(
        type=2,
        name="Water",
        group=1,
        properties=CellProperties({
            "liquid": CellProperty("liquid", True),
            "density": CellProperty("density", 1.0),
            "color": CellProperty("color", "blue")
        })
    )

    # Example 4: Cell with boolean and string properties
    lava_cell = Cell(
        type=3,
        name="Lava",
        group=1,
        properties=CellProperties({
            "liquid": CellProperty("liquid", True),
            "hot": CellProperty("hot", True),
            "color": CellProperty("color", "red")
        })
    )

    # Print out the cells and their properties
    def print_cell(cell):
        print(f"Cell: {cell.name} (type={cell.type}, group={cell.group})")
        if cell.properties:
            for prop in cell.properties.values():
                print(f"  - {prop.name}: {prop.value}")
        else:
            print("  (no properties)")
        print()

    for c in [air_cell, solid_cell, water_cell, lava_cell]:
        print_cell(c)

    print("Testing module Cell.py ... done.")
    