class Window:
    def draw(self):
        return "Drawing window"

class WindowDecorator:
    def __init__(self, window):
        self._window = window

    def draw(self):
        return self._window.draw()

class BorderDecorator(WindowDecorator):
    def draw(self):
        return f"{self._window.draw()} with border"

class ScrollDecorator(WindowDecorator):
    def draw(self):
        return f"{self._window.draw()} with scroll"

# Uso
window = Window()
bordered_window = BorderDecorator(window)
scrolled_window = ScrollDecorator(bordered_window)
print(scrolled_window.draw())  # Imprime: Drawing window with border with scroll
