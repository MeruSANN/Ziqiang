import pandas as pd

grade=pd.read_csv("Data/grade.csv")
group=grade.groupby("course_id")
ave=group["grade"].mean()
college=grade["course_id"].value_counts()
ave[college.index[0:5]].to_csv("result_max.csv",mode='a',header=True,encoding="utf-8")