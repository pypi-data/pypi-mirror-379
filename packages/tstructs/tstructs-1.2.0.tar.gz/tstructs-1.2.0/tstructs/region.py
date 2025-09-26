from .coord import Coordinate

class Region:
    """
    A class representing a 3D region in a tile map.
    Width, length and height are all the same and defined by region_size.
    """
    def __init__(self, region_size: int, region_location:Coordinate=(0,0)):
        """
        Initialize a Region object.

        :param region_size: The size (width, length, height) of the region. Must be positive.
        :type region_size: int
        :param region_location: The coordinate location of the region (default is (0, 0)).
        :type region_location: Coordinate or tuple[int, int]
        :raises ValueError: If region_size is not a positive integer.
        """

        self.region_size = region_size
        self.region_location = region_location

        # error check
        if self.region_size <= 0:
            raise ValueError("region_size must be a positive integer")

        # sanity check
        if self.region_size >= 2048:
            print("Warning: region_size is very large, this may lead to performance issues.")

    @property
    def name(self):
        """
        str: A string representation of the region's location (region_location).
        """
        return f"Region_{self.region_location}"

    @property
    def n(self):
        """
        int: The size of the region (alias for region_size).
        """
        return self.region_size
    
    def __len__(self):
        """
        Return the size of the region (region_size).

        :return: The size of the region.
        :rtype: int
        """
        return self.n
    
    @property
    def area(self):
        """
        int: The 2D area of the region (width * length).
        """
        return self.region_size * self.region_size

    @property
    def volume(self):
        """
        int: The 3D volume of the region (width * length * height).
        """
        return self.area * self.region_size
    
    def clamp_coordinates(self, start_x, start_y, end_x, end_y):
        """
        Clamp the given coordinates to be within the region bounds.

        :param start_x: The starting x-coordinate.
        :type start_x: int
        :param start_y: The starting y-coordinate.
        :type start_y: int
        :param end_x: The ending x-coordinate.
        :type end_x: int
        :param end_y: The ending y-coordinate.
        :type end_y: int
        :return: Tuple of clamped coordinates (sx, sy, ex, ey).
        :rtype: tuple[int, int, int, int]
        """
        sx = max(0, start_x)
        sy = max(0, start_y)
        ex = min(self.region_size - 1, end_x)
        ey = min(self.region_size - 1, end_y)

        return sx, sy, ex, ey
    
    def __repr__(self):
        """
        Show as Region name for easy identification
        """
        return self.name

    def __str__(self):
        """
        Show as Region name for easy identification
        """
        return self.name

    @property
    def centre(self) -> Coordinate:
        """
        Coordinate: The 2D centre coordinate of the region (as float values).
        """
        cx = self.region_location.x + (self.region_size - 1) / 2
        cy = self.region_location.y + (self.region_size - 1) / 2
        return Coordinate(cx, cy)

    def is_edge(self, x:int, y:int) -> bool:
        """
        Returns True if the (x, y) coordinate is on the edge of the region.
        Edge means x or y is at the minimum or maximum value within the region bounds.
        """
        min_x = self.region_location.x
        min_y = self.region_location.y
        max_x = self.region_location.x + self.region_size - 1
        max_y = self.region_location.y + self.region_size - 1
        return x == min_x or x == max_x or y == min_y or y == max_y

if __name__ == "__main__":
    print("Testing module region.py")

    # Example usage and test code for Region
    # Create a Region instance
    region = Region(region_size=16, region_location=Coordinate(10, 20))
    print("Region name:", region.name)
    print("Region n (size):", region.n)
    print("Region area:", region.area)
    print("Region volume:", region.volume)
    print("Region location:", region.region_location)
    # Test clamping
    clamped = region.clamp_coordinates(-5, 5, 20, 25)
    print("Clamped coordinates:", clamped)
    
    print("Test complete.")
