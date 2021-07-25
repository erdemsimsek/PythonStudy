from threading import Lock, Thread

class SingletonMeta(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:

            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                self._instances[self] = instance

        return self._instances[self]


class Singleton(metaclass=SingletonMeta):
    value : str  = None

    def __init__(self, value : str) -> None:
        self.value = value

    def some_business_logic(self):
        pass

def test_singleton(value : str) ->None:
    singleton = Singleton(value)
    print(singleton.value)

process1 = Thread(target=test_singleton, args=("FOO",))
process2 = Thread(target=test_singleton, args=("BAR",))
process1.start()
process2.start()