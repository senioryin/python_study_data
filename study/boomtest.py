#coding = utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="AdobeHeitiStd-Regular.otf")

x = range(1,61)

#时间
y_1 = [3.8,3.6,3.5,3.5,3.4,3.3,3.3,3.5,3.6,3.6,3.6,3.6,3.6,3.6,3.6]
y_2 = [3.4,3.2,3.1,3.1,3,2.9,2.9,3.1,3.2,3.2,3.2,3.2,3.2,3.2,3.2]
y_3 = [3.4,3.2,3.1,3.1,3,2.9,2.9,3.1,3.2,3.2,3.2,3.2,3.2,3.2,3.2]
y_4 = [3.3,3.1,3,3,2.9,2.8,2.8,3,3.1,3.2,3.1,3.1,3.1,3.1,3.1]

plt.figure(figsize=(20,8),dpi=80)
plt.plot(list(x)[:15],y_1,label="第一泡")
plt.plot(list(x)[15:30],y_2,label="第二泡")
plt.plot(list(x)[30:45],y_3,label="第三泡")
plt.plot(list(x)[45:60],y_4,label="第四泡")
plt.xlabel("次数",fontproperties=my_font)
plt.ylabel("时间",fontproperties=my_font)
plt.title("Boom",fontproperties=my_font)
_xtick_lable = ["第1次{}泡".format(i) for i in range(15)]
_xtick_lable += ["第2次{}泡".format(i) for i in range(15)]
_xtick_lable += ["第3次{}泡".format(i) for i in range(15)]
_xtick_lable += ["第4次{}泡".format(i) for i in range(15)]
plt.xticks(x,_xtick_lable,fontproperties=my_font,rotation=45)

plt.grid()

plt.show()

