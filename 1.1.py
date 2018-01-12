#-*- coding:utf-8 -*-
"""
滨州建模人口说明：
1.1通过工伤人口的和非工伤人口的基本信息，构建 人口—工伤 模型
此模型诣在学习工伤人口在“年龄”，“性别”，“民族”和“婚龄”方面的倾向性。
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
a = pd.read_csv("t_rkbaseinfo.csv" )
a_1 = a.loc[:, ["Age","Sex","MaritalStatus","Nation","LaborInjureState"]].fillna(0)
b = pd.read_csv("LaborInjure.csv")
b_1 = b.loc[:, ["Age","Sex","MaritalStatus","Nation","LaborInjureState"]].fillna(0)
frame = [a_1,b_1]
c= pd.concat(frame).fillna(0)
e= c.replace(('未说明的婚姻状况','丧偶','离婚','复婚','再婚','汉族'),(0,30,10,20,-10,1))
#print e
e.coloumns = ["Age","Sex","MaritalStatus","Nation"]
e.coloumn = ["LaborInjureState"]
X = e.loc[:,["Age","Sex","MaritalStatus","Nation"]]
y= e["LaborInjureState"]

log =LogisticRegression()
log.fit(X,y)

print log.predict([[3,2,90,3]])




