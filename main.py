# -*- coding:gbk -*-
from __future__ import with_statement
import assist as st
import Angle
import os
import re

def main():
  fileList= os.listdir('./电子手簿')
  dataFile = []
  for i in fileList:
    pattern = '.*.htm'
    if (re.compile(pattern).match(i)):
      dataFile.append('./电子手簿/' + i)
  
  
  angleList = []
  for fileName in dataFile:
    with open(fileName.decode('gbk'), 'rw+') as f:
      fileContent = ''
      for line in f:
        fileContent = fileContent + line
      stationName = st.getStationName(fileContent)
      if (stationName == '1#基'):
        ang = st.getAngle(fileContent, stationName)
        angleList.append(ang[1])
        angleList.append(ang[2])
      else:
        angleList.append(st.getAngle(fileContent, stationName))
