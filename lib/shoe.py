class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    def cobble(self):
        self.condition = "New"
        return "Your shoe is as good as new!"
