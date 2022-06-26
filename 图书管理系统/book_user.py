import psycopg2
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


# win = tk.Tk()
# win.geometry('1000x800')

class book_user:
    def __init__(self, win):
        self.win = win
        tk.Label(win, text='用户id：').grid(row=0, column=0)
        self.useridStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.useridStringvar).grid(row=0, column=1)

        tk.Label(win, text='用户：').grid(row=1, column=0)
        self.usernameStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.usernameStringvar).grid(row=1, column=1)

        tk.Label(win, text='密码：').grid(row=2, column=0)
        self.passwordStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.passwordStringvar).grid(row=2, column=1)

        tk.Label(win, text='电话：').grid(row=3, column=0)
        self.phoneStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.phoneStringvar).grid(row=3, column=1)
        # tk.Label(win, text='出版社：').grid(row=3, column=0)
        # self.pressStringvar = tk.StringVar()
        # pressChosen = ttk.Combobox(win, width=17, textvariable=self.pressStringvar)
        # pressChosen['values'] = ("清华出版社", "北大出版社", "桂电出版社")  # 设置下拉列表的值
        # pressChosen.grid(row=3, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        # pressChosen.current(2)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        tk.Label(win, text='状态：').grid(row=4, column=0)
        self.statusStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.statusStringvar).grid(row=4, column=1)
        # tk.Label(win, text='类别：').grid(row=4, column=0)
        # self.typeStringvar = tk.StringVar()
        # typeChosen = ttk.Combobox(win, width=17, textvariable=self.typeStringvar)
        # typeChosen['values'] = ("计算机类", "编程类", "文学类")  # 设置下拉列表的值
        # typeChosen.grid(row=4, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        # typeChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        tk.Label(win, text='已借图书：').grid(row=5, column=0)
        self.lend_numStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.lend_numStringvar).grid(row=5, column=1)

        tk.Label(win, text='现最多可借图书：').grid(row=6, column=0)
        self.max_numStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.max_numStringvar).grid(row=6, column=1)

        self.get_root()

        self.tree = ttk.Treeview(win)
        self.tree['column'] = ('用户id', '用户', '密码', '电话', '状态', '已借图书', '现最多可借图书')
        self.tree.column('用户id', width=100)
        self.tree.column('用户', width=100)
        self.tree.column('密码', width=100)
        self.tree.column('电话', width=100)
        self.tree.column('状态', width=100)
        self.tree.column('已借图书', width=100)
        self.tree.column('现最多可借图书', width=100)
        self.tree.heading('用户id', text='用户id')
        self.tree.heading('用户', text='用户')
        self.tree.heading('密码', text='密码')
        self.tree.heading('电话', text='电话')
        self.tree.heading('状态', text='状态')
        self.tree.heading('已借图书', text='已借图书')
        self.tree.heading('现最多可借图书', text='现最多可借图书')
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
            c = cursor.execute('select * from book_user')
        else:
            print('select * from book_user where userid like "%' + xh + '%"')
            c = cursor.execute("select * from book where name = '{}'".format(xh))

        list_re = cursor.fetchall()
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for i in range(len(list_re)):
            self.tree.insert('', i, text=i, values=(
                list_re[i][0], list_re[i][1], list_re[i][2], list_re[i][3], list_re[i][4], list_re[i][5],
                list_re[i][6]))
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
        cursor.execute("insert into book_user values ('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}')".format(
            self.useridStringvar.get(), self.usernameStringvar.get(), self.passwordStringvar.get(),
            self.phoneStringvar.get(),
            self.statusStringvar.get(), self.lend_numStringvar.get(), self.max_numStringvar.get()))
        conn.commit()
        self.tree.insert('', 'end',
                         value=[self.useridStringvar.get(), self.usernameStringvar.get(), self.passwordStringvar.get(),
                                self.phoneStringvar.get(),
                                self.statusStringvar.get(), self.lend_numStringvar.get(), self.max_numStringvar.get()])
        tk.messagebox.showinfo('提示', self.useridStringvar.get() + '信息插入成功！')
        conn.close()

    def update(self):
        xh = [self.useridStringvar.get(), self.usernameStringvar.get(), self.passwordStringvar.get(),
              self.phoneStringvar.get(),
              self.statusStringvar.get(), self.lend_numStringvar.get(), self.max_numStringvar.get()]
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
            "update book_user set userid='{0}',username='{1}',password='{2}',phone='{3}',status='{4}', lend_num='{5}', max_num='{6}' where userid = '{7}'".format(
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
        cursor.execute("delete from book_user where userid = '{}'".format(xh))
        conn.commit()
        tk.messagebox.showinfo('提示', xh + '信息删除成功！')
        conn.close()

    def clear(self):
        self.useridStringvar.set('')
        self.usernameStringvar.set('')
        self.passwordStringvar.set('')
        self.phoneStringvar.set('')
        self.statusStringvar.set('')
        self.lend_numStringvar.set('')
        self.max_numStringvar.set('')

    def get_root(self):
        win = self.win
        tk.Button(win, text='清空', width=10, height=1, command=self.clear).grid(row=8, column=0, pady=5)
        tk.Button(win, text='查询', width=10, height=1, command=self.select).grid(row=8, column=1, pady=5)
        tk.Button(win, text='插入', width=10, height=1, command=self.insert).grid(row=8, column=2, pady=5)
        tk.Button(win, text='更新', width=10, height=1, command=self.update).grid(row=8, column=3, pady=5)
        tk.Button(win, text='删除', width=10, height=1, command=self.delete).grid(row=8, column=4, pady=5)

# win.mainloop()
