# -*- coding:GBK -*-

class Angle():
  def __init__(self, angle, minute, second):
    self.angle = int(angle)
    self.minute = int(minute)
    self.second = float(second)
    
  def __str__(self):
    return str(self.angle) + '°' + str(self.minute) + "'" + str(self.second) + '"'
    
  def __le__(self, ang):
    pass
          
  def __add__(self, ang):
    self.second += ang.second
    if (self.second >= 60):
      self.second -= 60
      self.minute += 1
    self.minute += ang.minute
    if (self.minute >= 60):
      gelf.minute -= 60
      self.angle += 1
    self.angle += ang.angle
    if (self.angle >= 360):
      self.angle -= 360
      
  def __sub__(self, ang):
    self.second -= ang.second
    if (self.second < 0):
      self.second+= 60
      self.minute -= 1
    self.minute -= ang.minute
    if (self.minute < 0):
      self.minute += 60
      self.angle -= 1
    self.angle -= ang.angle