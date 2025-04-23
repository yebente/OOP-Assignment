# Base Superhero class
class Superhero:
    def __init__(self, name, power_level, origin):
        self.name = name
        self._power_level = power_level  # Encapsulated attribute
        self.origin = origin

    def show_identity(self):
        return f"My name is {self.name} from {self.origin}."

    def get_power_level(self):
        return self._power_level

    def boost_power(self, amount):
        self._power_level += amount
        print(f"{self.name}'s power boosted to {self._power_level}!")

# Subclass with flying ability
class FlyingHero(Superhero):
    def move(self):
        print(f"{self.name} is flying through the skies! ☁️")

# Subclass with tech gadgets
class TechHero(Superhero):
    def move(self):
        print(f"{self.name} is zooming on a hoverboard! 🛹")

# Creating superhero objects
yebente = FlyingHero("Yebente", 88, "Kisii")
makena = TechHero("Makena", 75, "Nairobi")

print(yebente.show_identity())
yebente.move()
yebente.boost_power(10)

print()

print(makena.show_identity())
makena.move()
print(f"Makena's power level: {makena.get_power_level()}")