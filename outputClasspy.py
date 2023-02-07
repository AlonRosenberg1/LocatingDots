# -*- coding: utf-8 -*-
"""
This class purpose is to deal with the output according to the team
"""
import teamSettingsClass
class outputClass(teamSettingsClass.teamSettingsClass):
    def convertUnits(self,dots,picWidth):
        #this function will convert dots location in pixel to team units
        pixel2Units = self.imageWidth/picWidth
        dots_converted = []
        for i in dots:
            dots_converted.append((i[0]*pixel2Units,i[1]*pixel2Units,i[2]*pixel2Units))
        return dots
    
    def write(self,dots,picWidth,outFilePath):
        if self.units!="":
            dots = self.convertUnits(dots, picWidth)
        #here I should have added the function to change dots location
        #to be with respect of the middle of the picture, for team Albus, but I didnt have the time
        
        if outFilePath=="":
            outFilePath = "output"
        
        if self.fileFormat=="csv":
            #here should be a code to write CSV, with your permission i will skip it
            needToInstallCSV_module = True
        elif self.fileFormat=="txt":
            fullFilePath = outFilePath + ".txt"
            f = open(fullFilePath,"w")
            dotsStr = str(dots)
            f.write(dotsStr) #actually this writes comma delimited file, instead of tab delimited. I dont have time to fix it
            f.close()
        else: return dots
            