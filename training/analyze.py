import pandas as pd
course=pd.read_csv("Data/course.csv")
count_type=course["course_type"].value_counts()
count_college=course["college"].value_counts()
count_instructor=course["instructor"].value_counts()
type_sum=count_type.sum()
frame_course=pd.DataFrame(columns=['amount','percentage'])
frame_course['amount']=count_type
for i in count_type.index:
    frame_course['percentage'][i]='{:.2f}%'.format(count_type[i]/type_sum*100)
dt={'':[count_college.index[0],count_instructor.index[0]],
    ' ':[count_college[0],count_instructor[0]]}
r=pd.DataFrame(dt,index=['开课最多学院','开课最多老师'])
frame_course.to_csv("result_course.csv",encoding="utf-8")
r.to_csv("result_course.csv",mode='a',header=True,encoding="utf-8")
