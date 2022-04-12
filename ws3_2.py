from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from sklearn import feature_selection
from sklearn.metrics import matthews_corrcoef
data1 = pd.DataFrame({"height":[158,162,170,175,180],"weight":[55,66,75,78,90]})
print(data1)
scaler = StandardScaler()
scaler.fit(data1)
normalized=scaler.transform(data1)

normalized=normalized.reshape(2,5)
normalized=normalized.astype(int)
print(normalized)
pearson=matthews_corrcoef(normalized[0],normalized[1])
print(pearson)
print(data1.cov())