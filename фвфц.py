class Lion:
    def __init__(self, name, age):
        self.kind = "felines"
        self.name = name
        self.age = age

    def roar(self):
        print(f"{self.name} Лев ричить!")

    def sleep(self):
        print(f"{self.name} Лев спить.")

class Tiger(Lion):
    def __init__(self, name, age, stripes):
        super().__init__(name, age)
        self.stripes = stripes

    def hunt(self):
        print(f"{self.name} Тигр полює на здобич.")

    def swim(self):
        print(f"{self.name} Тигр плаває у воді.")

class Cat(Tiger):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age, stripes=False)
        self.fur_color = fur_color

    def purr(self):
        print(f"{self.name} Кіт муркоче.")

    def play(self):
        print(f"{self.name} кіт грається з іграшкою.")

lion = Lion(input("Введіть ім'я лева"), 5)
tiger = Tiger(input("Введіть ім'я тигра"), 7, True)
cat = Cat(input("Введіть ім'я кота"), 2, "Gray")

lion.roar()
lion.sleep()

tiger.roar()
tiger.hunt()
tiger.swim()

cat.roar()
cat.purr()
cat.play()
