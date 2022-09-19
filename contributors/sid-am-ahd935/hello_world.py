class World:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "Hello " + self.text + "!!!"


if __name__ == "__main__":
    print(World('Aman'))


