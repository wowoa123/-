# -*- coding:gbk -*-

class Station():
    def __init__(self, angle, name):
        self.angle = angle
        self.name = name
        
    def setTarget(self, target):
        self.preTarget = target[0]
        self.nextTarget = target[1]
