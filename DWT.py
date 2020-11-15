import numpy as np
from numpy import array,argmin
from scipy.spatial.distance import cdist

def traceback(D0, D1, i, j):
    if i == 1 and j == 1:

        return trace

    if D1[i - 1, j] <= D1[i - 1, j - 1] + D0[i, j] and D1[i - 1, j] <= D1[i, j - 1]:
        trace.append([i - 1, j])
        return traceback(D0, D1, i - 1, j)

    if D1[i, j - 1] <= D1[i - 1, j] and D1[i, j - 1] <= D1[i - 1, j - 1] + D0[i, j]:
        trace.append([i, j - 1])
        return traceback(D0, D1, i, j - 1)

    if D1[i - 1, j - 1] + D0[i, j] <= D1[i - 1, j] and D1[i - 1, j - 1] + D0[i, j] <= D1[i, j - 1]:
        trace.append([i - 1, j - 1])
        return traceback(D0, D1, i - 1, j - 1)

r=6
c=4

D0=np.zeros((r+1,c+1))
D0[0,1:]= float("inf")
D0[1:,0]= float("inf")
D1=np.zeros((r+1,c+1))
D1[0,1:]= float("inf")
D1[1:,0]= float("inf")
D0[1:, 1:]=np.array([[2,1,5,1],[3,4,8,2],[5,2,4,3],[4,7,2,4],[1,5,1,6],[2,1,7,5]])
print(D0)

print(min(2*D0[1, 1], D0[1, 0], D0[0 , 1]))
for i in range(1,r+1):
    for j in range(1,c+1):
        # D1[i, j] += min(2*D0[i, j], D0[i-1, j ], D0[i , j-1])
        D1[i, j] = min(D1[i-1,j-1]+2*D0[i, j],   D1[i-1, j ]+D0[i,j],   D1[i , j-1]+D0[i,j])

print(D1)

i, j = array(D0.shape)-1
# print(D0[6,4])


# for k in range(r,0,-1):
#    for q in range(c,0,-1):
trace = []
trace.append([i,j])
traceback(D0,D1,i,j)
print(trace)

