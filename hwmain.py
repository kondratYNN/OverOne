class Tomato:
    states = ['too underripe', 'underripe', 'ripe']

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        if not self.is_ripe():
            self._state = self.states[self.states.index(self._state) + 1]

    def is_ripe(self):
        if self._state == self.states[2]:
            print(f'Tomato {self._index} is ripe!')
            return True
        else:
            return False


class TomatoBash:
    def __init__(self, amount):
        self.tomatoes = []
        for one in range(amount):
            tomato = Tomato(one)
            self.tomatoes.append(tomato)

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        result = True
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                result = False
        return result

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()


    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Harvest not ready')

    @staticmethod
    def knowledge_base():
        print('I know what tomato is, hehe')


Gardener.knowledge_base()
plant = TomatoBash(4)
lerim_gardener = Gardener('Lerim', plant)
lerim_gardener.work()
lerim_gardener.harvest()
lerim_gardener.work()
lerim_gardener.harvest()

