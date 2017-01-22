import pandas as pd
import random
N=20
M=1000
data=([[random.random() for i in range(N)] for j in range(M)])

df = pd.DataFrame(data)
df.to_csv('HW3.csv', index=False, header=False)
