import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

#need to import csv, can read them out of pandas

data = ('/Users/kiranweston/Documents/University/Year 4/Effects of morphing wing/Data 1 - Hawk Imaging 14_11_22/Flight data/10 Nov 2022 - Test data/TeST.csv')
df= pd.read_csv(data, header = None)
print(df)

n = len(df.columns)
m = (n-1)/3
print(n,m)


print(df2)
#print(df[1][0])

#for i in range(int(m)):
    #plt.plot(df, x=1 +3*i, y=2+3*i)


#plt.show()




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
    #
