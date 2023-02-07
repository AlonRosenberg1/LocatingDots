# -*- coding: utf-8 -*-
"""
Locating dots tool.

Usage:
    LocatingDots(team,outputFilePath,inputFilePath)
    inputs:
    team - team identifier, can be one of "Albus","Bellatrix"
    or "Cedric"
    
    outputFilePath - optional, path where the output file should be written.
    if omitted  or empty string then file output.<ext> will be created in working dir, where ext is the 
    team wanted extension.
    notice - if file is already present it will be overwitten
    
    inputFilePath - optional. if not given, the tool will read from camera.
    if given, the tool will analyze the given picture
    notice - if user want to input file an outputFilePath must be given
"""
def LocatingDots(team,outputFilePath = '',inputFilePath = ''):
    import header as h
    
    inputI = h.inputClass.inputClass(inputFilePath)
    detectorI = h.detectorClass.detectorClass(team)
    outputI = h.outputClasspy.outputClass(team)
    
    #the while is for continous camera capture. if we use only one picture the while ends after one iteration
    out = []
    while inputI.isReady == True:
        pic = inputI.getNew()
        dots = detectorI.findDots(pic)
        tmp, picWidth = pic.shape
        tmp = outputI.write(dots,picWidth,outputFilePath) #if we do not write to file the output is given as retun value
        out.append(tmp)
    return out
    
    
    

