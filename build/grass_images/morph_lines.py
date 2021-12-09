"""
@file morph_lines_detection.py
@brief Use morphology transformations for extracting horizontal and vertical lines sample code
"""
import numpy as np
import sys
import cv2 as cv
from IPython import embed

def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)
def main(argv):
    # [load_image]
    # Check number of arguments
    if len(argv) < 1:
        print ('Not enough parameters')
        print ('Usage:\nmorph_lines_detection.py < path_to_image >')
        return -1
    # Load the image
    src = cv.imread(argv[0], cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image: ' + argv[0])
        return -1
    # Show source image
    cv.imshow("src", src)
    # [load_image]
    # [gray]
    # Transform source image to gray if it is not already
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src
    # Show gray image
    show_wait_destroy("gray", gray)
    # th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY); 
    # cv2.imwrite("opencv-threshold-example.jpg", dst); 

    # # Thresholding with maxValue set to 128
    # th, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY); 
    # cv2.imwrite("opencv-thresh-binary-maxval.jpg", dst); 

    # # Thresholding with threshold value set 127 
    # th, dst = cv2.threshold(src,127,255, cv2.THRESH_BINARY); 
    # cv2.imwrite("opencv-thresh-binary.jpg", dst); 

    # Thresholding using THRESH_BINARY_INV 
    # th, dst = cv2.threshold(gray,127,255, cv2.THRESH_BINARY_INV); 
    # cv2.imwrite("opencv-thresh-binary-inv.jpg", dst); 

    # # Thresholding using THRESH_TRUNC 
    # th, dst = cv2.threshold(src,127,255, cv2.THRESH_TRUNC); 
    # cv2.imwrite("opencv-thresh-trunc.jpg", dst); 

    # # Thresholding using THRESH_TOZERO 
    th, dst = cv.threshold(gray,127,255, cv.THRESH_TOZERO); 
    # cv2.imwrite("opencv-thresh-tozero.jpg", dst); 

    # # Thresholding using THRESH_TOZERO_INV 
    # th, dst = cv2.threshold(src,127,255, cv2.THRESH_TOZERO_INV); 
    # cv2.imwrite("opencv-thresh-to-zero-inv.jpg", dst);
    show_wait_destroy("binary_filter", dst)
    # embed()
    
    # [gray]
    # [bin]
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    # Show binary image
    show_wait_destroy("binary", bw)
    # [bin]
    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    # [init]
    # [horiz]
    # Specify size on horizontal axis
    cols = horizontal.shape[1]
    horizontal_size = cols // 30
    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
    # Apply morphology operations
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)
    # Show extracted horizontal lines
    show_wait_destroy("horizontal", horizontal)
    # [horiz]
    # [vert]
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows // 30
    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))
    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)
    # Show extracted vertical lines
    show_wait_destroy("vertical", vertical)
    # [vert]
    # [smooth]
    # Inverse vertical image
    vertical = cv.bitwise_not(vertical)
    show_wait_destroy("vertical_bit", vertical)
    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''
    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges", edges)
    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)
    # Step 3
    smooth = np.copy(vertical)
    # Step 4
    smooth = cv.blur(smooth, (2, 2))
    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]
    # Show final result
    show_wait_destroy("smooth - final", vertical)
    # [smooth]
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])