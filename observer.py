"""
Propósito: Define una dependencia uno-a-muchos entre objetos, de modo que cuando uno de los objetos cambie de estado, todos sus dependientes sean notificados y actualizados automáticamente.
"""
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer received: {message}")

# Uso
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify_observers("Hello Observers!")  # Imprime: Observer received: Hello Observers!
