"""

This file demonstrates:
- Parent and child chapter08_classes
- Single inheritance
- Method overriding
- Using super()
- Polymorphism
- Multiple inheritance

"""

# ==========================================
# PARENT CLASS
# ==========================================

class Animal:
    """Parent class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


# ==========================================
# CHILD CLASSES (SINGLE INHERITANCE)
# ==========================================

class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        print(f"{self.name} says: Meow!")


print("=== SINGLE INHERITANCE ===")

dog = Dog("Buddy")
cat = Cat("Luna")

dog.speak()
cat.speak()

# ==========================================
# USING super()
# ==========================================

class Employee:
    """Parent class."""

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee: {self.name}")


class Developer(Employee):
    """Developer inherits from Employee."""

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display(self):
        super().display()
        print(f"Programming Language: {self.language}")


print("\n=== USING super() ===")

developer = Developer("John", "Python")
developer.display()

# ==========================================
# POLYMORPHISM
# ==========================================

class Bird:
    """Base class."""

    def speak(self):
        print("Bird makes a sound.")


class Parrot(Bird):
    def speak(self):
        print("Parrot says: Hello!")


class Eagle(Bird):
    def speak(self):
        print("Eagle screeches!")


print("\n=== POLYMORPHISM ===")

birds = [
    Parrot(),
    Eagle()
]

for bird in birds:
    bird.speak()

# ==========================================
# MULTIPLE INHERITANCE
# ==========================================

class Camera:
    """Provides camera functionality."""

    def take_photo(self):
        print("Taking a photo...")


class Phone:
    """Provides phone functionality."""

    def make_call(self):
        print("Making a phone call...")


class SmartPhone(Camera, Phone):
    """Inherits from Camera and Phone."""
    pass


print("\n=== MULTIPLE INHERITANCE ===")

iphone = SmartPhone()

iphone.take_photo()
iphone.make_call()

# ==========================================
# AUTOMATION EXAMPLE
# ==========================================

class Browser:
    """Base browser class."""

    def __init__(self, browser_name):
        self.browser_name = browser_name

    def launch(self):
        print(f"Launching {self.browser_name} browser...")


class ChromeBrowser(Browser):
    """Chrome browser."""

    def __init__(self):
        super().__init__("Chrome")


class FirefoxBrowser(Browser):
    """Firefox browser."""

    def __init__(self):
        super().__init__("Firefox")


print("\n=== AUTOMATION EXAMPLE ===")

chrome = ChromeBrowser()
firefox = FirefoxBrowser()

chrome.launch()
firefox.launch()

# ==========================================
# AUTOMATION POLYMORPHISM
# ==========================================

class BaseBrowser:
    """Base browser class for polymorphism."""

    def launch(self):
        raise NotImplementedError("Subclasses must implement launch().")


class Chrome(BaseBrowser):
    def launch(self):
        print("Launching Chrome...")


class Firefox(BaseBrowser):
    def launch(self):
        print("Launching Firefox...")


class Edge(BaseBrowser):
    def launch(self):
        print("Launching Edge...")


print("\n=== AUTOMATION POLYMORPHISM ===")

browsers = [
    Chrome(),
    Firefox(),
    Edge()
]

for browser in browsers:
    browser.launch()

# ==========================================
# AUTOMATION MULTIPLE INHERITANCE
# ==========================================

class ScreenshotMixin:
    """Provides screenshot capability."""

    def take_screenshot(self):
        print("Taking screenshot...")


class LoggerMixin:
    """Provides logging capability."""

    def log(self, message):
        print(f"LOG: {message}")


class TestRunner(ScreenshotMixin, LoggerMixin):
    """Inherits features from multiple chapter08_classes."""

    def run_test(self):
        self.log("Starting Login Test")
        print("Executing Login Test...")
        self.take_screenshot()
        self.log("Login Test Completed")


print("\n=== AUTOMATION MULTIPLE INHERITANCE ===")

runner = TestRunner()
runner.run_test()