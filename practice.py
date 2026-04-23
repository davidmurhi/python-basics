class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}")


dog1 = dog("Chickpea", "poodle")
dog1.bark()
dog1.describe()
