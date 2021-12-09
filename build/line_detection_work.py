# # Python program to illustrate HoughLine
# # method for line detection
# import cv2
# import numpy as np
# from IPython import embed

# # Reading the required image in
# # which operations are to be done.
# # Make sure that the image is in the same
# # directory in which this python program is

# img = cv2.imread('image_1.png')

# # Convert the img to grayscale
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # embed()
# # Apply edge detection method on the image

# # gradient_x = cv2.Sobel(gray, cv2.CV_16S, 1,0, ksize=3, scale=1,delta=0)
# # gradient_y = cv2.Sobel(gray, cv2.CV_16S, 0,1, ksize=3, scale=1,delta=0)
# # abs_gradient_x=cv2.convertScaleAbs(gradient_x)
# # abs_gradient_y=cv2.convertScaleAbs(gradient_y)

# # gradient=cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

# edges = cv2.Canny(gray,50,150,apertureSize = 3)

# # This returns an array of r and theta values
# embed()
# lines = cv2.HoughLines(gray,1,np.pi/180, 150)
# embed()
# # The below for loop runs till r and theta values
# # are in the range of the 2d array
# for line in lines:
#   for r,theta in line:
    
#     # Stores the value of cos(theta) in a
#     a = np.cos(theta)

#     # Stores the value of sin(theta) in b
#     b = np.sin(theta)
    
#     # x0 stores the value rcos(theta)
#     x0 = a*r
    
#     # y0 stores the value rsin(theta)
#     y0 = b*r
    
#     # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
#     x1 = int(x0 + 1000*(-b))
    
#     # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
#     y1 = int(y0 + 1000*(a))

#     # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
#     x2 = int(x0 - 1000*(-b))
    
#     # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
#     y2 = int(y0 - 1000*(a))
    
#     # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
#     # (0,0,255) denotes the colour of the line to be
#     #drawn. In this case, it is red.
#     cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
    
#   # All the changes made in the input image are finally
#   # written on a new image houghlines.jpg
# cv2.imwrite('images_out.jpeg', img)


import cv2
import numpy as np
import math
img = cv2.imread('lmw.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,50,200,apertureSize = 3)

cv2.imwrite('lmw_edge_out.png',edges)

lines = cv2.HoughLines(edges,1,np.pi/180,200,0,0,0,np.pi/5);

if lines is not None:
  for i in range(0, len(lines)):
      rho = lines[i][0][0]
      theta = lines[i][0][1]
      a = math.cos(theta)
      b = math.sin(theta)
      x0 = a * rho
      y0 = b * rho
      pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
      pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
      cv2.line(img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

cv2.imwrite('lmw_out.png',img)





# import cv2
# import numpy as np
# from IPython import embed


# img = cv2.imread('20211207_101033.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.f(edges,1,np.pi/180,300)
# # embed()
# for line in lines:
#   for x1,y1,x2,y2 in line:
#       cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imwrite('20211207_101033_out.jpg',img)