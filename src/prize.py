class Prize:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description} - {self.value}"