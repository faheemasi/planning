import matplotlib.pyplot as plt
import numpy as numpy


#reading the input file of x,y points
def x_y_list(filePath):
  file_rd = open(filePath)
  x_axis_val = []
  y_axis_val = []
  for i,line in enumerate(file_rd.readlines()):
    index,x_val,y_val = line.split(' ')
    x_axis_val.append(float(x_val.replace('x:','')))
    y_axis_val.append(float(y_val.replace('y:','')))

  return(x_axis_val,y_axis_val)

x_axis_val,y_axis_val = x_y_list('path.txt')

fig,axis = plt.subplots(2,2,figsize=(10,10))
axis[0,0].scatter(x_axis_val,y_axis_val)
plt.show()