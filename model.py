from random import randint

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0,360)

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360
        return self.orientation

class Engine(object):
    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    def updateModel(self,dt):
        if(self.theTank.contents != 0):
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        elif(self.theTank.contents == 0):
            self.currentRpm = 0

class Gearbox(object):

    def __init__(self):
        self.wheels = {"frontLeft": Wheel(), "frontRight": Wheel(), "rearLeft": Wheel(), "rearRight": Wheel()}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        if(self.currentGear == len(self.gears)-1 or self.clutchEngaged == True):
            pass
        else:
            self.currentGear += 1

    def shiftDown(self):
        if(self.currentGear == 0 or self.clutchEngaged == True):
            pass
        else:
            self.currentGear -= 1

    def rotate(self, revolutions):
        if(self.clutchEngaged == True):
            for key in self.wheels:
                self.wheels[key].rotate(revolutions * self.gears[self.currentGear])

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0

    def refuel(self):
        self.contents = self.capacity

class Car(object):

    def __init__(self):
        self.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)

if __name__ == '__main__':
    pass
