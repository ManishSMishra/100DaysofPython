# Inheritence

class Animal:
    def __init__(self) -> None:
        self.num_eyes=2

    def breathe(self):
        print("Inhale, Exhale.")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    def breathe(self):
        super().breathe()
        print("Breathing with Gills under water")
    def swim(self):
        print("Mowing in water.")


fish=Fish()

fish.swim()
print(fish.num_eyes)
fish.breathe()