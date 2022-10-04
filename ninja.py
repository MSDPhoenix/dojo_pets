import pet

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



shelly = pet.Pet("Shelly","turtle","biting fingers", "silence")

kane = pet.IndoorPet("Kane","dog","sit","Wang!","teddy bear")


lucy = Ninja("Lucy","DuWors","Oreo cookies","shrimp",shelly)

lucy.feed()
lucy.walk()
lucy.bathe()

michael = Ninja("Michael","DuWors","coffee","raw chicken leg",kane)

michael.feed()
michael.walk()
michael.bathe()
