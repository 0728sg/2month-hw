class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_hero_name(self):
        print(self.name)

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} - Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Clark Kent', 'Superman',
                 'Super Strength', 100, 'Up, up and away!')

hero.print_hero_name()
print(hero)
print(len(hero))
hero.double_health_points()
print(hero.health_points)
