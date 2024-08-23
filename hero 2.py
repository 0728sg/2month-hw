class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def print_hero_name(self):
        print(self.name)

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return f"{self.nickname} - Superpower: {self.superpower}, Health Points: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)
class AirHero(SuperHero):
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def print_fly_status(self):
        if self.fly:
            print("True in the True_phrase")
class EarthHero(SuperHero):
    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def print_fly_status(self):
        if self.fly:
            print("True in the True_phrase")
air_hero = AirHero('Tony stark', 'Iron man', 'no power, he is a power',
                   100, 'I am playboy, phylantrop and millioner', 50)
earth_hero = EarthHero('Diana', 'Wonder Woman', 'Super Strength', 1000,
                       'Truth and justice!', 70)

air_hero.double_health_points()
print(air_hero.health_points)
air_hero.print_fly_status()

earth_hero.double_health_points()
print(earth_hero.health_points)
earth_hero.print_fly_status()
class Villain(SuperHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, multiplier):
        self.damage **= multiplier
villain = Villain('Tanos', 'tanos', 'камни бесконечности', 10000,
                  'я сама неотвратимость', 500)

villain.crit(2)
print(villain.damage)
