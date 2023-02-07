# -*- coding: utf-8 -*-
"""
this class purpose is to deal with picture acquisition and interface 
with the camera 
"""
class camClass:
    """
    here will be the API for the Besler camera needed for the projecy
    I dont think the goal of this test is to implement Besler camera API so i will leave it empty
    I assume the API can get one picture every time and has a finished flag.
    one also must implemet a wait method to hold the code untill a new item is ready
    """
    pass


class inputClass:
    
    def __init__(self,inputFilePath):
        self.isReady = True # a flag indicating we need to do another picture
        if inputFilePath=="": #if filepath is empty it means we need to use the camera 
            self.fromCam = True
            self.cam = camClass()
        else:               #if file is given it means we need to load file
            self.fromCam = False
            self.inputFilePath = inputFilePath
            
    def getNew(self):
        import cv2
        if self.fromCam == True:
            print("press the enter key to take picture")
            pic = camClass.capture() 
        else: 
            pic = cv2.imread(self.inputFilePath, cv2.IMREAD_COLOR)
            pic = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY) #work with graysacle for easier implementation. one can research if the color data improves detection
            self.isReady = False #will cause to work on only one file
        return pic    
            
            
        
            
            
            
        