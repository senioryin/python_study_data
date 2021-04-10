#coding = utf-8
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = ['思想道德品质','知识结构与储备','思维能力','个性意志','专业兴趣','实践能力','信息加工能力','团队合作','创造力表现','市场意识','风险意识','职业生涯规划']
sizes = [10,9,5,5,5,5,5,5,36,5,5,5]
explode = (0,0,0,0,0,0,0,0,0.1,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("职业院校学生创新能力评估指标")
plt.show()