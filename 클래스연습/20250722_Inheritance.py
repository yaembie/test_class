class Animal:
    def __init__(self):
        self.name = "name"

    def speak(self):
        print(f"내 이름은 {self.name}(이)야.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        if name != '':
            self.name = name

    def speak(self):
        super().speak()
        print("멍!")


d = Dog("흰둥")
d.speak()
