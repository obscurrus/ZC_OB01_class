class Warrior():
    def __init__(self, name, power, endurance, color ):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.color = color

    def sleep(self):
        print(f'{self.name} лег спать')
        self.endurance += 2

    def eat(self):
        print(f'{self.name} хавает')
        self.power += 2

    def hit(self):
        print(f'{self.name} машет битой')

    def walk(self):
        print(f'{self.name} че-то бродит, грусть наводит')

    def info(self):
        print(f'Wrs name {self.name}')
        print(f'Wrs power {self.power}')
        print(f'Wrs endurance {self.endurance}')
        print(f'Wrs color {self.color}')