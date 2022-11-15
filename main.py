import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import plotly.express as px
import sys
import csv
import numpy as np

#need to import csv, can read them out of pandas
data = ('/Users/kiranweston/Documents/University/Year 4/Effects of morphing wing/Data 1 - Hawk Imaging 14_11_22/Flight data/10 Nov 2022 - Test data/TeST.csv')
df= pd.read_csv(data, header = None)

def plot_coords(frame,data):
    n = len(df.columns)
    m = int((n-1)/3)

    df_new = [[0] * 3 for i in range(int(m))]
    print(df_new)

    spec_row = df[df[0] == frame]
    print(spec_row.head())

    count = 1

    for j in range(0,m):
        for i in range(0,3):
            df_new[j][i] = spec_row.values[0][count]
            count = count+1
    return df_new

frame = 534
test = plot_coords(frame,df)
print(test)

test = np.array(test)
test = test.astype(np.float)
X, Y, Z = test[:,0], test[:,1], test[:,2]
print(test)

# Plot X,Y,Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(X, Y, Z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(X, Y, Z, c='red')
plt.show()



#def plot_coords(frame,data):
 # if [i,frame] = 0
  #else

#pseudocode
    #inputs (frame, data_csv file)
    # want to select row of the csv file according to the frame input
    #Then want to divide the total number of columns -1 by 3 (i.e. the number of actual x y and z coordinates) = col
    #Want to read 3 columns as coordinates for first point
    #i = 2, j = 3, k = 4
    #[i+3,j+3,k+3]
    #Want to do this process col number of times in a loop

#N.B. The For loop pseudocode didn't end up working when we tried it, as for loops don't work with coordinates
    #for i in range(int(m)):
    #plt.plot(df, x=1 +3*i, y=2+3*i)
    #plt.show()
