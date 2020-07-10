class Place(object):
    def __init__(self, type):
        self.type = type
    
class Home(Place):
    def __init__(self, owner, type = 0, door = 0, window = 0):
        super().__init__(type)
        self.owner = owner
        self.door = door
        self.window = window

    def PrintName(self):
        print(self.owner + '\'s home', end = '')

    def PrintInfo(self):
        self.PrintName()
        print(':')
        if (self.door == 0):
            print('    Door is closed.')
        elif (self.door == 1):
            print('    Door is open.')
        else:
            print('    Door is locked.')
        if (self.window):
            print('    Window is empty.')
        else:
            print('    Window is complete.')


class Cellar(Place):
    def __init__(self, owner, type = 1, door = 0):
        super().__init__(type)
        self.owner = owner
        self.door = door
    
    def PrintName(self):
        print(self.owner + '\'s cellar', end = '')

    def PrintInfo(self):
        self.PrintName()
        print(':')
        if (self.door == 0):
            print('    Cellar door is closed.')
        elif (self.door == 1):
            print('    Cellar door is open.')
        else:
            print('    Cellar door is locked.')

class OutsideHome(Place):
    def __init__(self, owner, type = 2):
        super().__init__(type)
        self.owner = owner

    def PrintName(self):
        print('outside ' + self.owner + '\'s home', end = '')

class Market(Place):
    def __init__(self, name, type = 3, broken = 0):
        super().__init__(type)
        self.name = name
        self.broken = broken

    def PrintName(self):
        print(self.name, end = '')
    
    def PrintInfo(self):
        self.PrintName()
        if (self.broken):
            print(' is broken.')
        else:
            print(' is open.')

class BlackMarket(Place):
    def __init__(self, name = 'Black Market', type = 4):
        super().__init__(type)
        self.name = name
    
    def PrintName(self):
        print(self.name, end = '')

class Car(Place):
    def __init__(self, owner, type = 5, door_open = 0):
        self.owner = owner
        super().__init__(type)
        self.door_open = door_open
        
    def PrintName(self):
        print(self.owner + '\'s car', end = '')

class OutsideCar(Place):
    def __init__(self, owner, type = 6):
        self.owner = owner
        super().__init__(type)

    def PrintName(self):
        print('outside ' + self.owner + '\'s home', end = '')
    
class AmbushPoint(Place):
    def __init__(self, belong, owner, type = 7):
        super().__init__(type)
        self.belong = belong
        self.owner = owner

    def PrintName(self):
        print(self.owner + '\'s ambush point', end = '')

def main():
    A = Home("hhf")
    A.PrintInfo()
    pass

if __name__ == '__main__':
    main()