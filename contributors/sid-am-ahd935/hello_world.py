"""
This is just a demo program for linting
"""


class World:
    """
    And this is a demo class for printing stuff
    """

    def __init__(self, text="World"):
        """
        Constructor Doc String
        """
        self.text = text

    def __str__(self):
        """
        Class Built-in Method Docstring
        """
        return "Hello " + self.text + "!!!"

    def print(self, text):
        """
        Global Method for calling.
        """
        print("This is the text:", text)


def main():
    """
    Main function to run script
    """
    print(World("Aman"))
    World().print("Peanuts in Pumpkins")


if __name__ == "__main__":
    main()
