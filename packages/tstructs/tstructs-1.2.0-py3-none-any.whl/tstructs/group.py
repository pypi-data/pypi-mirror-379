import random

class CellGroup:
    """
    Represents a group of cell types with a contiguous range of type indices.
    Provides methods to retrieve types in the range, random types, and group information.
    """
    def __init__(self, group_name:str, start_type:int, end_type:int):
        """
        Initialize a CellGroup.
        
        Args:
            group_name (str): Name of the group (must be non-empty).
            start_type (int): The starting type index (inclusive).
            end_type (int): The ending type index (exclusive).
        Raises:
            ValueError: If group_name is empty or start_type > end_type.
        """
        if group_name == "":
            raise ValueError("group name must be non-empty")
        self.group_name = group_name

        #error checking
        if start_type > end_type:
            raise ValueError("end type is meant to be larger than start type")
        
        self.start_type = start_type
        self.end_type = end_type

        if start_type > end_type:
            raise ValueError("end type is meant to be larger than start type")
        self.start_type = start_type
        self.end_type = end_type

    def get_types_in_range(self) -> list[int]:
        """
        Returns a list of type indices in the group range.
        
        Returns:
            list[int]: List of type indices from start_type to end_type (exclusive).
        """
        values = [t+self.start_type for t in range(self.end_type)]
        return values
    
    def __repr__(self):
        """
        Return a string representation of the CellGroup.
        """
        return f"{self.group_name} ({self.start_type}-{self.end_type})"
    
    @property
    def n(self):
        """
        Number of types in the group.
        
        Returns:
            int: The number of types in the group.
        """
        return self.end_type - self.start_type
    
    def __len__(self):
        """
        Return the number of types in the group (for len()).
        """
        return self.n()
    
    def get_random_type(self) -> int:
        """
        Return a random type index from the group.
        
        Returns:
            int: A random type index in the range [start_type, end_type].
        """
        i = random.randint(self.start_type, self.end_type)
        return i

    def get_number_of_random_types(self, num_types:int) -> list[int]:
        """
        Return a list of random type indices from the group.
        
        Args:
            num_types (int): Number of random types to generate (must be > 0).
        Returns:
            list[int]: List of random type indices.
        Raises:
            ValueError: If num_types <= 0.
        """
        if num_types <= 0:
            raise ValueError("num_types must be greater than 0")
        tile_list = [self.get_random_type() for _ in range(num_types)]
        return tile_list
