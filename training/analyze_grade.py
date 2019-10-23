import pandas as pd
import json

def G(grd):
    if(grd>=90):return 4.0
    if(grd>=85 and grd<90):return 3.7
    if(grd>=82 and grd<85):return 3.3
    if(grd>=78 and grd<82):return 3.0
    if(grd>=75 and grd<78):return 2.7
    if(grd>=72 and grd<75):return 2.3
    if(grd>=68 and grd<72):return 2.0
    if(grd>=64 and grd<68):return 1.5
    if(grd>=60 and grd<64):return 1.0
    return 0

def crt(grade_):
    GPA=0.0
    usr=grade_['user'][grade_.index[0]]
    for dx in grade_.index:
        row=grade_.ix[dx]
        i=row['course_id']
        c=course[course.id==i]['credit']
        credit[usr]+=c[c.index[0]]
        GPA+=G(row['grade'])*c[c.index[0]]
    frame['GPA'][usr]=GPA/float(credit[usr])

def diff(user):
    college[user["user"][user.index[0]]]=dic2[str(user["shrot_sid"][user.index[0]])]

        
grade=pd.read_csv("Data/grade.csv")
course=pd.read_csv("Data/course.csv")
names=grade['user'].unique()
times=grade['user'].value_counts()
frame=pd.DataFrame(0.0,index=names,columns=['name','ave','credit','college','GPA'])
credit=pd.Series(0.0,index=names)
group=grade.groupby("user")
frame['ave']=group['grade'].mean()
group.apply(crt)
frame['credit']=credit
credit.sort_values(ascending=False,inplace=True)
times.sort_values(ascending=False,inplace=True)
dt={'':[credit.index[0],times.index[0]],
    ' ':[credit[0],times[0]]}
r=pd.DataFrame(dt,index=['最多学分','最多门课'])
r.to_csv("result_max.csv",mode='a',header=True,encoding="utf-8")
#任务二
college={}
dic1=json.loads(open("Data/id_college_map.json").readline())
dic2={}
while len(dic1):
    p=dic1.popitem()
    val=p[1]
    for i in val:
        dic2[i]=p[0]
group.apply(diff)
frame['college']=pd.Series(college)
#匹配学院
frame.to_csv("result_grade.csv",encoding="utf-8")
