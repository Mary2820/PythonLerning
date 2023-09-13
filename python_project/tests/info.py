
class Location:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class New:
    @staticmethod
    def get_location():
        return Location(0, 12, 3)


m = New.get_location()
print(f"x: {m.x}, y: {m.y}, z: {m.z}")
print(m)