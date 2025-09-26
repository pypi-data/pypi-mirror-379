from .region import Region
from .coord import Coordinate

class ChunkedRegion(Region):
    """
    A subclass of Region that represents a chunked region.
    Each chunk is of size chunk_size x chunk_size.
    """
    def __init__(self, region_size: int, chunk_size: int, region_location:Coordinate=(0,0)):
        """
        Initialize a ChunkedRegion object.

        :param region_size: The size (width, length, height) of the region. Must be positive.
        :type region_size: int
        :param chunk_size: The size of each chunk within the region. Must be positive and divide region_size evenly.
        :type chunk_size: int
        :param region_location: The coordinate location of the region (default is (0, 0)).
        :type region_location: Coordinate or tuple[int, int]
        :raises ValueError: If chunk_size is not a positive integer or does not divide region_size evenly.
        """
        super().__init__(region_size, region_location=region_location)
        self.chunk_size = chunk_size

        # error check
        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be a positive integer")
        if self.region_size % self.chunk_size != 0:
            raise ValueError("chunk_size must divide region_size evenly")

    @property
    def chunks_per_side(self):
        """
        int: The number of chunks along one side of the region.
        """
        return self.region_size // self.chunk_size

    @property
    def total_chunks(self):
        """
        int: The total number of chunks in the region.
        """
        return self.chunks_per_side * self.chunks_per_side
    
    def get_chunk_coordinates(self, loc:Coordinate) -> Coordinate:
        """
        Get the chunk coordinates for a given location within the region.
        """
        return Coordinate(loc.x // self.chunk_size, loc.y // self.chunk_size)
    
    def get_chunks_in_area(self, start:Coordinate, end:Coordinate) -> list[Coordinate]:
        """
        Get all chunk coordinates that intersect with the given area.

        :param start: The starting coordinate of the area.
        :type start: Coordinate
        :param end: The ending coordinate of the area.
        :type end: Coordinate
        :return: A list of chunk coordinates that intersect with the area.
        :rtype: list[Coordinate]
        """
        start_chunk = self.get_chunk_coordinates(start)
        end_chunk = self.get_chunk_coordinates(end)

        chunks = []
        for cx in range(start_chunk.x, end_chunk.x + 1):
            for cy in range(start_chunk.y, end_chunk.y + 1):
                if 0 <= cx < self.chunks_per_side and 0 <= cy < self.chunks_per_side:
                    chunks.append(Coordinate(cx, cy))
        
        return chunks

if __name__ == "__main__":
    print("Starting tests for Chunk region...")

    # Basic test for ChunkedRegion
    print("Testing ChunkedRegion...")
    region_size = 16
    chunk_size = 4
    region_location = Coordinate(0, 0)
    cr = ChunkedRegion(region_size, chunk_size, region_location=region_location)
    print(f"Chunks per side: {cr.chunks_per_side}")
    print(f"Total chunks: {cr.total_chunks}")

    # Test get_chunk_coordinates
    loc = Coordinate(5, 7)
    chunk_coord = cr.get_chunk_coordinates(loc)
    print(f"Chunk coordinates for {loc}: {chunk_coord}")

    # Test get_chunks_in_area
    start = Coordinate(2, 2)
    end = Coordinate(10, 10)
    chunks_in_area = cr.get_chunks_in_area(start, end)
    print(f"Chunks in area from {start} to {end}: {chunks_in_area}")

    print("Tests completed.")
