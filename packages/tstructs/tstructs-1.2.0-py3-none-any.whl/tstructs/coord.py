class Coordinate(tuple):
	"""A tuple subclass to represent a 2D or 3D coordinate (x, y[, z])."""
	def __new__(cls, *args):
		if len(args) == 2:
			x, y = args
			return super().__new__(cls, (x, y))
		elif len(args) == 3:
			x, y, z = args
			return super().__new__(cls, (x, y, z))
		else:
			raise ValueError("Coordinate must be 2D (x, y) or 3D (x, y, z)")

	@property
	def x(self):
		"""The x component of the coordinate."""
		return self[0]

	@property
	def y(self):
		"""The y component of the coordinate."""
		return self[1]

	@property
	def z(self):
		"""The z component of the coordinate (only for 3D coordinates). Raises AttributeError if 2D."""
		if len(self) == 3:
			return self[2]
		raise AttributeError("This coordinate is 2D and has no 'z' value.")
	
	def __repr__(self):
		if len(self) == 2:
			return f"{self.x}_{self.y}"
		elif len(self) == 3:
			return f"{self.x}_{self.y}_{self.z}"
		return super().__repr__()
	
	def __str__(self):
		return self.__repr__()

# --- Test code for Coordinate class ---
def test_coordinate():
	print("Running module tests...")
	# Test 2D coordinate
	c2 = Coordinate(1, 2)
	assert c2.x == 1, f"Expected x=1, got {c2.x}"
	assert c2.y == 2, f"Expected y=2, got {c2.y}"
	try:
		_ = c2.z
		assert False, "Accessing z on 2D should raise AttributeError"
	except AttributeError:
		pass

	# Test 3D coordinate
	c3 = Coordinate(3, 4, 5)
	assert c3.x == 3, f"Expected x=3, got {c3.x}"
	assert c3.y == 4, f"Expected y=4, got {c3.y}"
	assert c3.z == 5, f"Expected z=5, got {c3.z}"

	# Test error on wrong dimension
	try:
		_ = Coordinate(1)
		assert False, "Should raise ValueError for 1D"
	except ValueError:
		pass
	try:
		_ = Coordinate(1, 2, 3, 4)
		assert False, "Should raise ValueError for 4D"
	except ValueError:
		pass
	print("All Coordinate tests passed.")

if __name__ == "__main__":
	print("Main method running...")
	test_coordinate()