class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        print(f"\n{self.pet.name} the {self.pet.type} is {self.first_name}'s pet.")

    def walk(self):
        print(f"\nWalking {self.pet.name} the {self.pet.type}")
        self.pet.play()

    def feed(self):
        print(f"\nFeeding {self.pet.name} the {self.pet.type}")
        self.pet.eat()

    def bathe(self):
        print(f"\nBathing {self.pet.name} the {self.pet.type}")
        self.pet.noise()

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
        print(f"{self.sound}!\n")

shelly = Pet("Shelly","turtle","biting fingers", "silence")

lucy = Ninja("Lucy","DuWors","Oreo cookies","shrimp",shelly)

lucy.feed()
lucy.walk()
lucy.bathe()
