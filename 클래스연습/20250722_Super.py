class Animal:
    def __init__(self, name):
        self.name = name
        print(f"내 이름은 {self.name}(이)야.")

    def speak(self):
        print("안녕!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        super().speak()
        print("멍!")

d = Dog("비누")
d.speak()