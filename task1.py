import pandas as pd


df=pd.read_csv("students_50 (1).csv")
df["Average"] =df[["Math","English","Science"]].mean(axis=1)
df.index = range(1, len(df) + 1)
print(df[["Name","Average"]])
max=pd.DataFrame(df.max())
print ("hight average student : ")
print(max)



