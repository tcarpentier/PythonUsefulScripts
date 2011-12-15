#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
Created on 13 oct. 2011

@author: Thomas  Carpentier

'''

from datetime import datetime
import os
now = datetime.now()
from optparse import OptionParser


def createSourceFolderForMeteor(option, opt, value, parser):
    
    _year = str(now.year)
    _month = str(now.month)
    _day = str(now.day)
    _time = str(datetime.now().strftime('%H-%M-%S'))
    
    path = raw_input("Where do you want to create folder : ")
    SourceConfigID = raw_input("Type source config ID : ")
    
    pathtocreate = SourceConfigID + "_" + _year + "-" + _month + "-" + _day + "T" + _time  + ".000_COMPLETE"
    os.chdir(path)
    os.mkdir(pathtocreate) 
    print path
    print SourceConfigID + "_" + _year + "-" + _month + "-" + _day + "T" + _time  + ".000_COMPLETE"
    

def modifySourceFolderForMeteor(option, opt, value, parser):
    _year = str(now.year)
    _month = str(now.month)
    _day = str(now.day)
    _time = str(datetime.now().strftime('%H-%M-%S'))
    
    path = raw_input("Where do you want to modify folder : ")
    Folder = raw_input("Type folder to modify : ")
    SourceConfigID = raw_input("Type source config ID : ")
    
    pathtocreate = SourceConfigID + "_" + _year + "-" + _month + "-" + _day + "T" + _time  + ".000_COMPLETE"
    os.chdir(path)
    os.rename(Folder, pathtocreate)
    

if __name__ == "__main__":

    
    parser = OptionParser()
    parser.add_option("-c", action="callback", callback=createSourceFolderForMeteor)
    parser.add_option("-m", action="callback", callback=modifySourceFolderForMeteor)
    
    (options, args) = parser.parse_args()
