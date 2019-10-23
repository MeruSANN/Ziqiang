import pandas as pd

grade=pd.read_csv("result_grade.csv",encoding='utf-8')
group=grade.groupby('college')
avegpa=group["GPA"].mean()
avegpa.sort_values(ascending=False,inplace=True)
avegpa.head(5).to_csv("result_max.csv",mode='a',header=True,encoding="utf-8")
