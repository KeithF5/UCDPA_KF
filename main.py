import requests
import pandas as pd
import jsonstat
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
url = url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/TEM22/JSON-stat/1.0/'
collection = jsonstat.from_url(url)
#print(collection)
mcar = collection.dataset(0)
#print(mcar)
for d in mcar.dimensions():
    print(d)
#print(mcar.value)
#print(mcar.value(C02437V02947= "Ford"))
df = mcar.to_data_frame()
#print(df)
#print(df.head())
#print(df.dtypes)
Car = df['Car Make']
print(Car.head)
print()rint(max(Car))
print(min(Car))
print(list(Car))
finalcarList=np.unique(Car).tolist()
print(finalcarList)