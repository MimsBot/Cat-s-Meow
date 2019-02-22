class Cat:
    def __init__(self, name, favorite_food, gender):
        self.name = name
        self.favorite_food = favorite_food
        self.gender = gender
    def __str__(self):
        return f"{self.name} is a cat. {self.pronoun()} eats {self.favorite_food}"
    def pronoun(self):
        if self.gender == "male":
            return "he"
        else:
            return "she"

cat1 = Cat('Felix', 'kibble', "male")
print(cat1)

cat2 = Cat('MessyFace','kibble', "female")
print(cat2)
