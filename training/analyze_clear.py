import pandas as pd

course=pd.read_csv("Data/course.csv")
course_new=course[(course.course_type=="专业必修")|(course.course_type=="公共必修")|(course.course_type=="公共选修")|(course.course_type=="专业选修")]
course_new.to_csv("course_new.csv",encoding="utf-8")