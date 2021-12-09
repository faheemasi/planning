import cv2
import numpy as np
from IPython import embed


def show_wait_destroy(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyWindow(winname)


# # for sensitivity in range()
# frame = cv2.imread('image_1_cut.png')
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# for i in range(7):
#   for j in range(7):
#     for k in range(7):
#       sens_h= 2*i
#       sens_s= 2*j
#       sens_v= 4*k

#       lower = (61-sens_h, min((250-sens_s*2),0), min((51-sens_v),0) ) 
#       upper = (61+sens_h, max((250+sens_s*2),255), max((51+sens_v),255) )

#       # preparing the mask to overlay
#       mask = cv2.inRange(hsv, lower, upper)
        
#       # The black region in the mask has the value of 0,
#       # so when multiplied with original image removes all non-blue regions
#       result = cv2.bitwise_and(frame, frame, mask = mask)

#       cv2.imwrite('result/result_sens_h{}_sens_s{}_sens_v{}.jpg'.format(sens_h,sens_s,sens_v),result)


# # show_wait_destroy('frame', frame)
# # show_wait_destroy('mask', mask)
# # show_wait_destroy('result', result)
# # embed()
 

import cv2
import numpy as np
from IPython import embed

def check_candidate(b_image,x,y):
  checking if previous pixels are not black
  checking if front pixels are black
  checking if below pixels are black
  checking if upper pixel are green



img_rd = cv2.imread('result/result_sens_h12_sens_s12_sens_v24.jpg',cv2.IMREAD_GRAYSCALE)
(thresh,binary_image) = cv2.threshold(img_rd,1,255,cv2.THRESH_BINARY)
img_row,img_col = binary_image.shape

print(binary_image.shape)
# embed()
mask = np.zeros((img_row,img_col))

filter_width_half = 50
filter_height_half  = 50 
threshold=1600

for row in range(filter_width_half,img_row-filter_width_half):
  for col in range(filter_height_half,img_col-filter_height_half):
    wind_img = binary_image[row-filter_width_half:row+filter_width_half,col-filter_height_half:col+filter_height_half]
    pixel_sum = np.sum(wind_img>0)
    if(pixel_sum>threshold):
      mask[row,col]=1
      # embed()

result = np.multiply(mask,img_rd)
show_wait_destroy('result', result)



