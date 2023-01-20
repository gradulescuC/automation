class Car:

		def __init__(self, wheel, speed, color):
				self._speed = speed  # protected class attribute
				self._color = color  # protected class attribute
				self._wheel = wheel  # protected class attribute

peugeot = Car("right", 240, "white")
peugeot.color = "black"
print("peugeot color:", peugeot._color)  # a ramas tot white
peugeot._color = "black"

