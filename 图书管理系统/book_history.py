import psycopg2
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


# win = tk.Tk()
# win.geometry('1000x800')

class book_history:
    def __init__(self, win):
        self.win = win
        tk.Label(win, text='图书id：').grid(row=0, column=0)
        self.book_idStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.book_idStringvar).grid(row=0, column=1)

        tk.Label(win, text='图书名：').grid(row=1, column=0)
        self.nameStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.nameStringvar).grid(row=1, column=1)

        tk.Label(win, text='借阅者id：').grid(row=2, column=0)
        self.useridStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.useridStringvar).grid(row=2, column=1)

        tk.Label(win, text='借阅者名字：').grid(row=3, column=0)
        self.usernameStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.usernameStringvar).grid(row=3, column=1)
        # tk.Label(win, text='出版社：').grid(row=3, column=0)
        # self.pressStringvar = tk.StringVar()
        # pressChosen = ttk.Combobox(win, width=17, textvariable=self.pressStringvar)
        # pressChosen['values'] = ("清华出版社", "北大出版社", "桂电出版社")  # 设置下拉列表的值
        # pressChosen.grid(row=3, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        # pressChosen.current(2)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        tk.Label(win, text='借阅开始时间：').grid(row=4, column=0)
        self.begin_timeStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.begin_timeStringvar).grid(row=4, column=1)
        # tk.Label(win, text='类别：').grid(row=4, column=0)
        # self.typeStringvar = tk.StringVar()
        # typeChosen = ttk.Combobox(win, width=17, textvariable=self.typeStringvar)
        # typeChosen['values'] = ("计算机类", "编程类", "文学类")  # 设置下拉列表的值
        # typeChosen.grid(row=4, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        # typeChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        tk.Label(win, text='借阅结束时间：').grid(row=5, column=0)
        self.end_timeStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.end_timeStringvar).grid(row=5, column=1)

        tk.Label(win, text='状态：').grid(row=6, column=0)
        self.statusStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.statusStringvar).grid(row=6, column=1)

        self.get_root()

        self.tree = ttk.Treeview(win)
        self.tree['column'] = ('图书id', '图书名', '借阅者id', '借阅者名字', '借阅开始时间', '借阅结束时间', '状态')
        self.tree.column('图书id', width=100)
        self.tree.column('图书名', width=100)
        self.tree.column('借阅者id', width=100)
        self.tree.column('借阅者名字', width=100)
        self.tree.column('借阅开始时间', width=100)
        self.tree.column('借阅结束时间', width=100)
        self.tree.column('状态', width=100)
        self.tree.heading('图书id', text='图书id')
        self.tree.heading('图书名', text='图书名')
        self.tree.heading('借阅者id', text='借阅者id')
        self.tree.heading('借阅者名字', text='借阅者名字')
        self.tree.heading('借阅开始时间', text='借阅开始时间')
        self.tree.heading('借阅结束时间', text='借阅结束时间')
        self.tree.heading('状态', text='状态')
        self.tree.grid(row=10, column=0, columnspan=10)

    def select(self):
        xh = self.useridStringvar.get()
        # 创建会话连接
        conn = psycopg2.connect(dbname="postgres",
                                user="tom",
                                password="Huawei_123",
                                host="192.168.56.101",
                                port="26000")
        # 编码
        conn.set_client_encoding('utf8')
        # 创建游标
        cursor = conn.cursor()
        if len(xh) == 0:
            c = cursor.execute('select * from book_history')
        else:
            print('select * from book_history where name like "%' + xh + '%"')
            c = cursor.execute("select * from book_history where name = '{}'".format(xh))

        list_re = cursor.fetchall()
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for i in range(len(list_re)):
            self.tree.insert('', i, text=i, values=(
                list_re[i][0], list_re[i][1], list_re[i][2], list_re[i][3], list_re[i][4], list_re[i][5], list_re[i][6]))
        conn.close()

    def insert(self):
        # 创建会话连接
        conn = psycopg2.connect(dbname="postgres",
                                user="tom",
                                password="Huawei_123",
                                host="192.168.56.101",
                                port="26000")
        # 编码
        conn.set_client_encoding('utf8')
        # 创建游标
        cursor = conn.cursor()
        cursor.execute("insert into book_history values ('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}')".format(
            self.book_idStringvar.get(), self.nameStringvar.get(), self.useridStringvar.get(), self.usernameStringvar.get(),
            self.begin_timeStringvar.get(), self.end_timeStringvar.get(), self.statusStringvar.get()))
        conn.commit()
        self.tree.insert('', 'end',
                         value=[self.book_idStringvar.get(), self.nameStringvar.get(), self.useridStringvar.get(), self.usernameStringvar.get(),
            self.begin_timeStringvar.get(), self.end_timeStringvar.get(), self.statusStringvar.get()])
        tk.messagebox.showinfo('提示', self.nameStringvar.get() + '信息插入成功！')
        conn.close()

    def update(self):
        xh = [self.book_idStringvar.get(), self.nameStringvar.get(), self.useridStringvar.get(), self.usernameStringvar.get(),
            self.begin_timeStringvar.get(), self.end_timeStringvar.get(), self.statusStringvar.get()]
        # 创建会话连接
        conn = psycopg2.connect(dbname="postgres",
                                user="tom",
                                password="Huawei_123",
                                host="192.168.56.101",
                                port="26000")
        # 编码
        conn.set_client_encoding('utf8')
        # 创建游标
        cursor = conn.cursor()
        cursor.execute(
            "update book_history set book_id='{0}',name='{1}',userid='{2}',username='{3}',begin_time='{4}', end_time='{5}', status='{6}' where userid = '{7}'".format(
                                                                                                                 xh[0],
                                                                                                                 xh[1],
                                                                                                                 xh[2],
                                                                                                                 xh[3],
                                                                                                                 xh[4],
                                                                                                                 xh[5],
                                                                                                                 xh[6],
                                                                                                                 xh[0]))
        conn.commit()
        tk.messagebox.showinfo('提示', xh[0] + '信息更新成功！')
        conn.close()

    def delete(self):
        xh = self.useridStringvar.get()
        # 创建会话连接
        conn = psycopg2.connect(dbname="postgres",
                                user="tom",
                                password="Huawei_123",
                                host="192.168.56.101",
                                port="26000")
        # 编码
        conn.set_client_encoding('utf8')
        # 创建游标
        cursor = conn.cursor()
        cursor.execute("delete from book_history where name = '{}'".format(xh))
        conn.commit()
        tk.messagebox.showinfo('提示', xh + '信息删除成功！')
        conn.close()

    def clear(self):
        self.book_idStringvar.set('')
        self.nameStringvar.set('')
        self.useridStringvar.set('')
        self.usernameStringvar.set('')
        self.begin_timeStringvar.set('')
        self.end_timeStringvar.set('')
        self.statusStringvar.set('')


    def get_root(self):
        win = self.win
        tk.Button(win, text='清空', width=10, height=1, command=self.clear).grid(row=8, column=0, pady=5)
        tk.Button(win, text='查询', width=10, height=1, command=self.select).grid(row=8, column=1, pady=5)
        tk.Button(win, text='插入', width=10, height=1, command=self.insert).grid(row=8, column=2, pady=5)
        tk.Button(win, text='更新', width=10, height=1, command=self.update).grid(row=8, column=3, pady=5)
        tk.Button(win, text='删除', width=10, height=1, command=self.delete).grid(row=8, column=4, pady=5)


# win.mainloop()
