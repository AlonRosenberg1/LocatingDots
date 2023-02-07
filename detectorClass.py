# -*- coding: utf-8 -*-
"""
The purpose of this class is to deal with the detection of dots with sub-pixel resolution
"""

import teamSettingsClass
class detectorClass(teamSettingsClass.teamSettingsClass):
    def houghFindCir(self,pic):
        #this function detects the integer pixel location of dots using Hough transform
        import cv2
        #picBlurr = cv2.blur(pic, (3, 3)) #litrature recommands blurring the image. I didnt find it helpful
        #the following params (except for min/max Radius) were found using trail and error using the given picture
        dp = 1 
        minDist = 10 #minimum distance between dots, took for the given image
        dotRadius = self.dotsWidth/2 #team Cedric will have Radius of 0 which means the algorith search for every dot size
        param1=50 
        param2=3
        #minRadius = dotRadius - 1 #the min/max Radius should be as specifed by teams. we allowed some slack (+-1)
        #maxRadius = dotRadius + 1
        """
        the example picture did not fit any team so I used special parameters
        for it. in real operation we should use the now commented max/min Radius
        """
        maxRadius=6
        minRadius=1
        detected_circles = cv2.HoughCircles(pic,cv2.HOUGH_GRADIENT, dp, minDist, param1 = param1,param2 = param2, minRadius = minRadius, maxRadius = maxRadius)
        return detected_circles
        """
        visual check
        only 970 out of ~1300 dots were detected, which is not good
        sadly i dont have time to researc it further
        circles = np.uint16(np.around(detected_circles))
        tmpPic = pic
        for i in circles[0,0:10,:]:
            # draw the outer circle
            cv2.circle(tmpPic,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.imshow('detected circles',tmpPic)
        cv2.waitKey(0)
            
        """
    def get_x_y_co(self,xc,yc,r):
        #this function return the points on the edge of a given circle
        #it is not very good function, as it returns some duplicants pixels, but i dont have time to write something better
        import math
        arr=[]
        for i in range(0,360,5):
            y = yc + r*math.sin(math.radians(i))
            x = xc+ r*math.cos(math.radians(i))
            x=int(x)
            y=int(y)
            arr.append([x,y])
        return arr     
    
    def momentumAdjustment(self,pic,circles):
        import numpy as np 
        maxVal = np.amax(pic)
        invPic = maxVal-pic #invert the picture because we want dark pixel to have more weight
        modCircles = []
        circShape = circles.shape
        for ind in range(circShape[1]):
            #for each circle we calculate its momentoum by sum_i(x(i)*value(i)) / sum_i(value(i))
            nomSumX = 0
            nomSumY = 0
            denomSum = 0
            #ugly workaround for circle at the edges, sorry
            #near the edge circle should not be changed because some of their circle is outside the picture
            if circles[0,ind,0]+circles[0,ind,2] >1599:
                modCircles.append((circles[0,ind,0],circles[0,ind,1],circles[0,ind,2]))
                continue
            if circles[0,ind,0]-circles[0,ind,2] <0:
                modCircles.append((circles[0,ind,0],circles[0,ind,1],circles[0,ind,2]))
                continue
            if circles[0,ind,1]+circles[0,ind,2] >899:
                modCircles.append((circles[0,ind,0],circles[0,ind,1],circles[0,ind,2]))
                continue
            if circles[0,ind,1]-circles[0,ind,2] <0:
                modCircles.append((circles[0,ind,0],circles[0,ind,1],circles[0,ind,2]))
                continue
                
            circlePoints = self.get_x_y_co(circles[0,ind,0],circles[0,ind,1],circles[0,ind,2])
            for point in circlePoints:
                #sum over all the points in the circle
                nomSumX = nomSumX + (point[0]-circles[0,ind,0])*invPic[point[1],point[0]]
                nomSumY = nomSumY + (point[1]-circles[0,ind,1])*invPic[point[1],point[0]]
                denomSum = denomSum + invPic[point[1],point[0]]
            diffX = nomSumX/denomSum
            diffY = nomSumY/denomSum
            modCircleX = circles[0,ind,0] + diffX
            modCircleY = circles[0,ind,1] + diffY
            modCircles.append((modCircleX,modCircleY,circles[0,ind,2]))
        return modCircles
            
           
    def findDots(self,pic):
        circles = self.houghFindCir(pic)
        modCircles = self.momentumAdjustment(pic,circles)
        return modCircles
        
        