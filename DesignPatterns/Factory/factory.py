import random
from abc import ABC, abstractmethod


class IAnimal(ABC):

    @abstractmethod
    def getAnimal(self):
        pass


class Dog(IAnimal):

    def getAnimal(self):
        print("Dog")


class Cat(IAnimal):

    def getAnimal(self):
        print("Cat")


class Duck(IAnimal):

    def getAnimal(self):
        print("Duck")


class AnimalFactory:

    def getCreateAnimal(self):
        raise NotImplementedError


class BalancedAnimalFactory(AnimalFactory):
    animalCount = {}

    def __init__(self):
        self.animalCount["Dog"] = 0
        self.animalCount["Cat"] = 0
        self.animalCount["Duck"] = 0

    def getCreateAnimal(self):
        temp = min(self.animalCount.values())
        res = [key for key in self.animalCount if self.animalCount[key] == temp]
        self.animalCount[res[0]] = self.animalCount[res[0]] + 1

        if res[0] == "Dog":
            return Dog()

        if res[0] == "Cat":
            return Cat()

        if res[0] == "Duck":
            return Duck()


class RandomizedAnimalFactory(AnimalFactory):

    def __init__(self):
        #self.classList = [globals()["Dog"], globals()["Cat"], globals()["Duck"]]
        self.classList = [Dog, Cat, Duck]

    def getCreateAnimal(self):
        return self.classList[random.randint(0, len(self.classList) - 1)]()


print("BalancedAnimalFactory")

bAF = BalancedAnimalFactory()

animal1 = bAF.getCreateAnimal()
animal2 = bAF.getCreateAnimal()
animal3 = bAF.getCreateAnimal()

animal1.getAnimal()
animal2.getAnimal()
animal3.getAnimal()

print("--------------------------------")

rAF = RandomizedAnimalFactory()

animal4 = rAF.getCreateAnimal()
animal5 = rAF.getCreateAnimal()
animal6 = rAF.getCreateAnimal()

animal4.getAnimal()
animal5.getAnimal()
animal6.getAnimal()
