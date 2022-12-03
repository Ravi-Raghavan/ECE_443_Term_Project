import pandas as pd  
import numpy as np  

time_index = pd.date_range("1/01/2021", periods=6, freq="W")

df = pd.DataFrame(index=time_index);
print(df)
    
df["Sales"] = [5.0,4.0,np.nan,np.nan,1.0,np.nan];
print(df)



