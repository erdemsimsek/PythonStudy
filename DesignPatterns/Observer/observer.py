from abc import ABC, abstractmethod
import threading
import random

newDataArrived = threading.Lock()

class IObserver(ABC):

    @abstractmethod
    def update(self):
        pass


class IDisplay(ABC):

    @abstractmethod
    def showMessage(self):
        pass


class IObservable(ABC):

    @abstractmethod
    def addIObserver(self, observer):
        pass

    @abstractmethod
    def removeIObserver(self, observer):
        pass

    @abstractmethod
    def notifyIObserver(self):
        pass


class WeatherStation(IObservable):

    def __init__(self):
        self.__observerList = []
        threading.Timer(1, self.notifyIObserver).start()

    def addIObserver(self, observer):
        self.__observerList.append(observer)

    def removeIObserver(self, observer):
        self.__observerList.remove(observer)

    def notifyIObserver(self):
        for entity in self.__observerList:
            entity.update()
        threading.Timer(1, self.notifyIObserver).start()
        newDataArrived.release()

    def getTemperature(self):
        return random.randint(10, 30)


class PhoneDisplay(IObserver, IDisplay):

    def __init__(self, observable):
        self.__observable = observable
        self.__val = 0

    def update(self):
        self.__val = self.__observable.getTemperature()

    def showMessage(self):
        print("Phone Display Temperature " + str(self.__val) + "C")

    @property
    # Getter function
    def observable(self):
        return self.__observable

    # Setter function
    @observable.setter
    def observable(self, observable):
        self.__observable = observable


class WindowDisplay(IObserver, IDisplay):

    def __init__(self, observable):
        self.__observable = observable
        self.__val = 0

    def update(self):
        self.__val = self.__observable.getTemperature()

    def showMessage(self):
        print("Window Display Temperature " + str(self.__val) + "C")

    @property
    # Getter function
    def observable(self):
        return self.__observable

    # Setter function
    @observable.setter
    def observable(self, observable):
        self.__observable = observable


weatherStation = WeatherStation()
phoneDisplay = PhoneDisplay(weatherStation)
windowDisplay = WindowDisplay(weatherStation)

weatherStation.addIObserver(phoneDisplay)
weatherStation.addIObserver(windowDisplay)


while (1):
    newDataArrived.locked()
    phoneDisplay.showMessage()
    windowDisplay.showMessage()

