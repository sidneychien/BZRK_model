#-*- coding:utf-8 -*-
"""
滨州建模人口说明：
1，本模型诣在学习未交失业保险的各年龄段和工伤之间的联系。
2，需要的数据为“未交失业保险”的ID，“年龄”（数值化为年龄段指数，20-30岁为1，30-40岁为2，40-50岁为3，50-60岁为4，60+为5），“工伤情况”（工伤为1，非为零）
3，暂时选择逻辑回归
"""
import pymysql
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='172.20.120.187',
                             port=3306,
                             user='root',
                             password='Gepoint',
                             db='edc_rkceshi',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()

sql='Select a.Age,+ b.Idcard,+c.LaborInjureState FROM t_rk_baseinfo as a,t_rk_UnemployInsur as b,t_rk_laborinjure as c WHERE a.Idcard = b.Idcard=c.Idcard'

cursor.execute(sql)
a= cursor.fetchall()
print str(a)




