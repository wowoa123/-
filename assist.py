# -*- coding:gbk -*-
import Angle
import re

"""norely"""
def compare(ang1, ang2):
  pass
  
def getStationName(fileContent):
  pattern = '<td width=30% valign=left><p align=left>测站：(.*)</td>'
  reObj = re.compile(pattern)
  name = reObj.findall(fileContent)
  return name[0]
    
def getTargetName(fileContent):
  pattern = '<td valign=center><palign=center>(方1|方2|1#基|2#基|2#|3#|0#)</td>'
  reObj = re.compile(pattern)
  targetName = reObj.findall(fileContent)
  return targetName
    
def getAngle(fileContent, name):
  pattern = '<.*><.*>(\d{2，3}).*(\d{2}).*(\d{2}\.\d).*<.*>'
  reObj= re.compile(pattern)
  angleData = reObj.findall(fileContent)
  if (name == '1#基'):
    angle = []
    for i in angleData:
      angle.append(Angle.Angle(i[0], i[1], i[2]))
    return angle
  else:
    return Angle.Angle(angleData[1][0], angleData[1][1], angleData[1][2])


"""rely one or more"""
def compareAbs(ang1, ang2):
  pass

def getStartFile(dataFile, f1_2):
  pass
