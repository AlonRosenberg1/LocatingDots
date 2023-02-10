# LocatingDots
 Computer Vision project of locating dots on products
 
 This is an example project for detecting dots on a product for assembly line needs
 the needed resolution in sub pixel scale.
 
 The project is built for 3 teams, each having different specifications:
 ### team 1:
 The dots are about 2 pixels wide and needed resolution is 0.02 pixel. the output should be in mm 
 
 ### team 2 
 The dots are about 50 pixels wide and the needed resolution is 0.1 pixel. The output will be written to CSV file in mm.
 
 ### team 3
 This team supports a varies size of dots and the needed resolution sould be 0.2 pixels. The output should be written to TXT file.
 
 ## Algorithm 
 The Algorithm uses Hough transform to fit circles in the image, then it uses [momentum methood](https://arxiv.org/pdf/1104.3776.pdf) to achive sub pixle resolution 
 
 ## example
 input:
 
 ![example](https://github.com/AlonRosenberg1/LocatingDots/blob/main/dots2.jpg)
 
 output:
 (243.56, 780.27, 29.9), (320.22, 111.97, 29.9), etc...
