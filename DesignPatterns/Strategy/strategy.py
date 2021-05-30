from abc import ABC, abstractmethod


class IFlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        pass


class IQuackBehaviour(ABC):

    @abstractmethod
    def quack(self):
        pass


class IDisplayBehaviour(ABC):

    @abstractmethod
    def display(self):
        pass


class SimpleFlyBehavior(IFlyBehavior):

    def fly(self):
        print("Simple Fly Behavior")


class NoFlyBehavior(IFlyBehavior):

    def fly(self):
        print("No Fly Behavior")


class SimpleQuackBehavior(IQuackBehaviour):

    def quack(self):
        print("Simple Quack Behavior")


class NoQuackBehavior(IQuackBehaviour):

    def quack(self):
        print("No Quack Behavior")


class SimpleDisplayBehavior(IDisplayBehaviour):

    def display(self):
        print("Simple Display Behavior")


class NoDisplayBehavior(IDisplayBehaviour):

    def display(self):
        print("No Display Behavior")


class Duck:

    def __init__(self, IFly, IQuack, IDisplay):
        self.__fly = IFly
        self.__quack = IQuack
        self.__display = IDisplay

    def do_fly(self):
        self.__fly.fly(self)

    def do_quack(self):
        self.__quack.quack(self)

    def do_display(self):
        self.__display.display(self)

    @property
    # Getter Function for fly interface
    def fly(self):
        return self.__fly

    @fly.setter
    # Setter Function for fly interface
    def fly(self, IFly):
        self.__fly = IFly

    @property
    # Getter Function for quack interface
    def quack(self):
        return self.__quack

    @quack.setter
    # Setter Function for quack interface
    def quack(self, IQack):
        self.__quack = IQack

    @property
    # Getter Function for display interface
    def display(self):
        return self.__display

    @display.setter
    # Setter Function for display interface
    def display(self, IDisplay):
        self.__display = IDisplay


RubberDuck = Duck(NoFlyBehavior, NoQuackBehavior, SimpleDisplayBehavior)

print("---------------------------")
print(RubberDuck.fly)
RubberDuck.do_fly()

print("---------------------------")
print(RubberDuck.quack)
RubberDuck.do_quack()

print("---------------------------")
print(RubberDuck.display)
RubberDuck.do_display()

print("---------------------------")
RubberDuck.fly = SimpleFlyBehavior
print(RubberDuck.fly)
RubberDuck.do_fly()
