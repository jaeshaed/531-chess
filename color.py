class Color:
    def __init__(self, name, hex_code):
        self.name = name
        self.hex_code = hex_code

    def __str__(self):
        return f"Color: {self.name}, Hex: {self.hex_code}"

white = Color("White", "#FFFFFF")
black = Color("Black", "#000000")