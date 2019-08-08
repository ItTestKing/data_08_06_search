# 导入tkinter模块，以及导入ttk模块，tkinter是python结合tk的标准接口，ttk是TK8.5之后加入的“主题化工具包”
from tkinter import *
from tkinter import ttk
from search import Search
from read import ReadFile


# 定义的计算函数，完成英尺到米的换算
def calculate(*args):
    try:

        Search().search_file_name = feet.get()
        meters.set(Search().search_begin())
    except ValueError:
        print("输入不正确")


'''
创建了一个主窗口；
主窗口标题为：“Free to Meters”
通过ttk.Frame创建了一个框架容器；所以界面内容都放在框架中，并把框架放在主窗口root中；
通过grid指定框架的位置，以及对齐方式：sticky说明使用罗盘式方位，控件将要如何在网格单元格里排放（NWES分别表示上左右下）；
columnconfigure方法告诉tk自适应宽度；
rowconfigure方法告诉tk自适应高度
'''
root = Tk()
root.title("搜索文件")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=40, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="开始搜索", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="输入文件或路径").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="搜索结果").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

'''
检查框架内的所有控件，并在每个控件之间增加一点距离，使他们看起来没那么拥挤；
告诉tk把注意力转移到我们的输入框上；也就是说在开始的时候，光标默认会在输入框，当用户输入的时候不需要去单击
告诉tk用户按下了回车键和单击计算按钮是一样的，会调用计算程序段
'''
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)

# tk让他的事件循环，这样才能让所有的事件运行
root.mainloop()


