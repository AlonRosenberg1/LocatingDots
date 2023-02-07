# -*- coding: utf-8 -*-
"""
This class purpose is to hold all the settings for all the different teams
It will do input validation and all the team specific class will inherit from it
"""

class teamSettingsClass:
    def __init__(self,team):
        if team == "Albus":
            self.units  = "mm"
            self.fileFormat = "returnVal"
            self.dotsWidth = 2 #dots width in pixels
            self.imageWidth = 10 #in teams units. I assume it is constant per team. later on we can get it per image
        elif team == "Bellatrix":
            self.units  = "mil"
            self.fileFormat = "csv"
            self.dotsWidth = 50 #dots width in pixels
            self.imageWidth = 1000
        elif team == "Cedric":
            self.units  = "" #empty units imply not to convert
            self.fileFormat = "txt"
            self.dotsWidth = 0 #signal dots width is unknown
            
        else: 
            raise NameError("Error using LocatingDots.py - unidentified team name. team must be Albus, Bellatrix or Cedric")
            
            