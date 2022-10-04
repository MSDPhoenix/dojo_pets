class Pet:
    def __init__(self,name,type,tricks,sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 0
        self.energy = 0
        print(f"\n{self.name} is a/an {self.type}")
        print(f"\thealth: {self.health}")
        print(f"\tenergy: {self.energy}")

    def sleep(self):
        self.energy += 25
        print("adding 25 to energy")
        print(f"\tenergy = {self.energy}")

    def eat(self):
        self.energy += 5
        self.health += 10
        print("Adding 5 to energy and 10 to health.")
        print(f"\thealth = {self.health}")
        print(f"\tenergy = {self.energy}")

    def play(self):
        self.health += 5
        print("adding 5 to health")
        print(f"\thealth = {self.health}")

    def noise(self):
        print(f"\t{self.sound} {self.sound}\n")

class IndoorPet(Pet):
    def __init__(self,name,type,tricks,sound,toy):
        super().__init__(name,type,tricks,sound)
        self.toy = toy
    def play(self):
        self.health += 7
        print("adding 7 to health")
        print(f"\thealth = {self.health}")


if __name__ == "__main__":
    print("\npet.py has been run")
else:
    print("\npet.py has been imported")