class Beverage:

    def cost(self):
        raise NotImplemented()


class Espresso(Beverage):

    def cost(self):
        return 1


class AddOns(Beverage):

    def __init__(self, beverage):
        self.__beverage = beverage

    @property
    def beverage(self):
        return self.__beverage

    def cost(self):
        return self.__beverage.cost()


class CaramelAddOn(AddOns):

    def cost(self):
        return 2 + self.beverage.cost()


class ChocolateAddOn(AddOns):

    def cost(self):
        return 3 + self.beverage.cost()


class MilkAddOn(AddOns):

    def cost(self):
        return 1 + self.beverage.cost()


print("Cost of Espresso: 1")
print("Cost of adding Caramel: 2")
print("Cost of adding Chocolate: 3")
print("Cost of adding Milk: 1")
print("-----------------------------------------")

myEspresso = Espresso()
print("Cost of Espresso " + str(myEspresso.cost()))

myEspressoWithCaramel = CaramelAddOn(myEspresso)
print("Cost of Espresso with Caramel " + str(myEspressoWithCaramel.cost()))

myEspressoWithChocolate = ChocolateAddOn(myEspresso)
print("Cost of Espresso with Chocolate " + str(myEspressoWithChocolate.cost()))

myEspressoWithMilk = MilkAddOn(myEspresso)
print("Cost of Espresso with Milk " + str(myEspressoWithMilk.cost()))

myEspressoWithCaramelWithChocolate = ChocolateAddOn(myEspressoWithCaramel)
print("Cost of Espresso with Caramel and Chocolate " + str(myEspressoWithCaramelWithChocolate.cost()))

myEspressoWithCaramelWithMilk = MilkAddOn(myEspressoWithCaramel)
print("Cost of Espresso with Caramel and Milk " + str(myEspressoWithCaramelWithMilk.cost()))

myEspressoWithCaramelWithMilkWithChocolate = MilkAddOn(myEspressoWithCaramelWithChocolate)
print("Cost of Espresso with Caramel, Chocolate and Milk " + str(myEspressoWithCaramelWithMilkWithChocolate.cost()))
