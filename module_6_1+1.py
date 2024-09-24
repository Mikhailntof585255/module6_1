class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    eduble = False
    def __init__(self, food):
        self.food = food

class Flower(Plant):
    def eat(self, name, food):
        self.food = food

class Fruit(Plant):
    eduble = True
    def eat(self, name, food):
        self.food = food


class Predator(Animal):
    def eat(self, food):
        self.food = food
        if p1.eduble == True:
            print(f"{self.name} съел {p1.food} ")
            fed = True
        else:
            print(f"{self.name} не стал есть {p1.food}")
            elive = False

class Mammal(Animal):
    def eat(self, food):
        self.food = food
        if p2.eduble == True:
            print(f"{self.name} съел {p2.food} ")
            fed = True
        else:
            print(f"{self.name} не стал есть {p2.food}")
            elive = False


a1 = Predator("Волк с Уолл_Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")
print(a1.name)
# print(a2.name)
print(p1.food)
# print(p2.food)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
print(a1.alive)
print(a2.fed)
