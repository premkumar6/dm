import pandas as pd
from sklearn.metrics import pairwise_distances

d2={"x":[0,1,0,1,0,1,0,0,0,1],"y":[0,1,0,0,0,1,1,0,0,0]}
data2=pd.DataFrame(d2)
print(data2)
#%%
ans1=pairwise_distances(data2.to_numpy(),metric="jaccard")
print(ans1)
#%%
def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count

X="0101010001"
Y="0100011000"
  
print("Haming Dist is ",hammingDist(X, Y))
#%%