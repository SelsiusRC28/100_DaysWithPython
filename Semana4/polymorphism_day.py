import random


class Animal:
    def make_sound(self):
        return("This is the sound....")
        
class Dog(Animal):
    def make_sound(self):
        return("Wau Wau Wau")
class Cat(Animal):
    def make_sound(self):
        return("Miau Miau Miau")
class Cow(Animal):
    def make_sound(self):
        return ("Muuu Muuu Muuu")


class SimulatorSoundAnimal:
    def __init__(self):
        self.animals = []
    
    def add_sound(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Created {animal.__class__.__name__} succesfully")
        else:
            print("Animal invalit")
        
    def show_sounds(self):
        if self.animals:
            print("\n ----- Animals -----")
            for index, animal in enumerate(self.animals, start=1):
                print(f"{index}. {animal.make_sound()}")
        else :
            print("\n No have animals :(")
    
    def delete_animal(self, posicion):
        if self.animals:
            self.animals.pop(posicion-1)
            print("Sound Deleted")
        else:
            print("\n No have animals :(")
    
    def random_sound(self):
        if self.animals:
            random_integer = random.randint(0, len(self.animals)-1)
            animal = self.animals[random_integer]
            print(animal.make_sound())
        else:
            print("\n No have animals :(")

            
#Main

simulator = SimulatorSoundAnimal()

while True:
    print("\n ------ Simulator ---------")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Cow")
    print("4. Show Sounds")
    print("5. Exit")
    print("6. Delete Animal")
    print("7. Random Sound")
    
    choise = int(input("Enter your choise 1-5: ").strip())
    
    if choise == 1:
        simulator.add_sound(Dog())
    elif choise == 2:
        simulator.add_sound(Cat())
    elif choise == 3:
        simulator.add_sound(Cow())
    elif choise == 4:
        simulator.show_sounds()
    elif choise == 5:
        break
    elif choise == 6:
        simulator.show_sounds()
        print("\n ------- Delete one animal ---------")
        option = int(input("Enter you posicion: ").strip()) 
        simulator.delete_animal(option)
    elif choise == 7:
        simulator.random_sound()
        
    else:
        print("Invalit choise. Please try again.")