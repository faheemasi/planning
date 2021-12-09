
import matplotlib.pyplot as plt
import numpy as np
from IPython import embed
import math


def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
    '''
    Adapted and modifed to get the unknowns for defining a parabola:
    http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
    '''

    denom = (x1-x2) * (x1-x3) * (x2-x3)
    A = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
    B = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
    C = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1)
         * y2+x1 * x2 * (x1-x2) * y3) / denom

    return A, B, C


def circle_points(point_a, point_b, radius, point_distance=0.2):
	center_x = (point_a[0]+point_b[0])/2.0
	center_y = (point_a[1]+point_b[1])/2.0
	y_range = []
	x_range = []
	if(abs(point_a[0]-point_b[0]) > abs(point_a[1]-point_b[1])):
		if(point_b[0] > point_a[0]):
			x_range = np.arange(point_a[0], point_b[0], point_distance)
		else:
			x_range = np.arange(point_b[0], point_a[0], point_distance)
		for x in x_range:
			y = np.sqrt(radius**2-(x-center_x)**2) + center_y
			y_range.append(y)
	else:
		if(point_b[1] > point_a[1]):
			y_range = np.arange(point_a[1], point_b[1], point_distance)
		else:
			y_range = np.arange(point_b[1], point_a[1], point_distance)
		for y in y_range:
			x = np.sqrt(radius**2-(y-center_y)**2)+center_x
			x_range.append(x)
	embed()
	return (x_range, y_range)


  # Define your three known points
x1, y1 = [2.0, 11.0]
x2, y2 = [-4.0, 35.0]
x3, y3 = [0.0, -5.0]

# points set
segment_a = [[0.0, 2.0], [10.0, 12.0]]
x_a = [segment_a[0][0], segment_a[1][0]]
y_a = [segment_a[0][1], segment_a[1][1]]

segment_c = [[10.0, 16.0], [0.0, 6.0]]
x_c = [segment_c[0][0], segment_c[1][0]]
y_c = [segment_c[0][1], segment_c[1][1]]


slope_a = (y_a[0]-y_a[1])/(x_a[0]-x_a[1])

slope_c = slope_a
slope_b = -1.0 / slope_a

y_intercept_a = y_a[0]-slope_a*x_a[0]
y_intercept_c = y_c[0]-slope_c*x_c[0]

# y intercept of line perpendicular to line a'c and passing through edge point of c
y_intercept_b_a = y_c[0] - slope_b * x_c[0]
# y intercept of line perpendicular to line a'c and passing through edge point of a
y_intercept_b_c = y_a[1] - slope_b * x_a[1]

xb1 = (y_intercept_b_a - y_intercept_a)/(slope_a - slope_b)
yb1 = slope_b * xb1 + y_intercept_b_a
pointb1 = (xb1, yb1)

xb2 = (y_intercept_b_c - y_intercept_c)/(slope_c-slope_b)
yb2 = slope_b*xb2+y_intercept_b_c
pointb2 = (xb2, yb2)


x_c_val = []  # circle values
y_c_val = []  # circle values

if(xb1 - x_a[1]) * slope_a > 0:
	point = pointb1
	radius = np.sqrt( ( (point[0]-segment_a[1][0])**2 + (point[1]-segment_a[1][0])**2 ) )
	x_c_val,y_c_val=circle_points(point,segment_a[1],radius,point_distance=0.2)
else:
	point = pointb2
	radius = np.sqrt( ( (point[0]-segment_c[c][0])**2 + (point[1]-segment_c[0][0])**2 ) )
	x_c_val,y_c_val=circle_points(point,segment_c[0],radius,point_distance=0.2)


# equation of circle and drawing the blob


# Calculate the unknowns of the equation y=ax^2+bx+c
# a,b,c=calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

# Define x range for which to calc parabola

# x_pos=np.arange(-30,30,1)
# y_pos=[]

# #Calculate y values
# for x in range(len(x_pos)):
# 	x_val=x_pos[x]
# 	y=(a*(x_val**2))+(b*x_val)+c
# 	y_pos.append(y)


ax = plt.gca()
plt.axes().set_aspect('equal')
# plt.plot(x_pos, y_pos, linestyle='-.', color='black') # parabola line
plt.plot(x_a, y_a)
plt.plot(x_c, y_c)

print(point)

ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
# plt.scatter(xb1, yb1, color='red') # parabola points
plt.scatter(point[0], point[1], color='green')
plt.scatter(x_c_val, y_c_val, color='red')
embed()
# plt.scatter(x_pos, y_pos, color='gray') # parabola points
# plt.scatter(x1,y1,color='r',marker="D",s=50) # 1st known xy
# plt.scatter(x2,y2,color='g',marker="D",s=50) # 2nd known xy
# plt.scatter(x3,y3,color='k',marker="D",s=50) # 3rd known xy
plt.show()
