import psycopg2
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


# win = tk.Tk()
# win.geometry('1000x800')

class book_information:
    def __init__(self, win):
        self.win = win
        tk.Label(win, text='书名：').grid(row=0, column=0)
        self.nameStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.nameStringvar).grid(row=0, column=1)

        tk.Label(win, text='作者：').grid(row=1, column=0)
        self.authorStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.authorStringvar).grid(row=1, column=1)

        tk.Label(win, text='数量：').grid(row=2, column=0)
        self.numStringvar = tk.StringVar()
        tk.Entry(win, width=20, textvariable=self.numStringvar).grid(row=2, column=1)

        # tk.Label(win, text='出版社：').grid(row=3, column=0)
        # pressStringvar = tk.StringVar()
        # tk.Entry(win, width=20, textvariable=pressStringvar).grid(row=3, column=1)
        tk.Label(win, text='出版社：').grid(row=3, column=0)
        self.pressStringvar = tk.StringVar()
        pressChosen = ttk.Combobox(win, width=17, textvariable=self.pressStringvar)
        pressChosen['values'] = ("清华出版社", "北大出版社", "桂电出版社")  # 设置下拉列表的值
        pressChosen.grid(row=3, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        pressChosen.current(2)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        # tk.Label(win, text='类别：').grid(row=4, column=0)
        # typeStringvar = tk.StringVar()
        # tk.Entry(win, width=20, textvariable=typeStringvar).grid(row=4, column=1)
        tk.Label(win, text='类别：').grid(row=4, column=0)
        self.typeStringvar = tk.StringVar()
        typeChosen = ttk.Combobox(win, width=17, textvariable=self.typeStringvar)
        typeChosen['values'] = ("计算机类", "编程类", "文学类")  # 设置下拉列表的值
        typeChosen.grid(row=4, column=1)  # 设置其在界面中出现的位置 column代表列 row 代表行
        typeChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen[‘values’] 的下标值

        self.get_root()

        self.tree = ttk.Treeview(win)
        self.tree['column'] = ('书名', '作者', '数量', '出版社', '类型')
        self.tree.column('书名', width=100)
        self.tree.column('作者', width=100)
        self.tree.column('数量', width=100)
        self.tree.column('出版社', width=100)
        self.tree.column('类型', width=100)
        self.tree.heading('书名', text='书名')
        self.tree.heading('作者', text='作者')
        self.tree.heading('数量', text='数量')
        self.tree.heading('出版社', text='出版社')
        self.tree.heading('类型', text='类型')
        self.tree.grid(row=10, column=0, columnspan=10)

    def select(self):
        xh = self.nameStringvar.get()
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
            c = cursor.execute('select * from book')
        else:
            print('select * from book where name like "%' + xh + '%"')
            c = cursor.execute("select * from book where name = '{}'".format(xh))

        list_re = cursor.fetchall()
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for i in range(len(list_re)):
            self.tree.insert('', i, text=i, values=(
                list_re[i][0], list_re[i][1], list_re[i][2], list_re[i][3], list_re[i][4]))
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
        cursor.execute("insert into book values ('{0}','{1}','{2}','{3}','{4}')".format(
            self.nameStringvar.get(), self.authorStringvar.get(), self.numStringvar.get(), self.pressStringvar.get(),
            self.typeStringvar.get()))
        conn.commit()
        self.tree.insert('', 'end',
                         value=[self.nameStringvar.get(), self.authorStringvar.get(), self.numStringvar.get(),
                                self.pressStringvar.get(),
                                self.typeStringvar.get()])
        tk.messagebox.showinfo('提示', self.nameStringvar.get() + '信息插入成功！')
        conn.close()

    def update(self):
        xh = [self.nameStringvar.get(), self.authorStringvar.get(), self.numStringvar.get(), self.pressStringvar.get(),
              self.typeStringvar.get()]
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
            "update book set name='{0}',author='{1}',num='{2}',press='{3}',type='{4}' where name = '{5}'".format(xh[0],
                                                                                                                 xh[1],
                                                                                                                 xh[2],
                                                                                                                 xh[3],
                                                                                                                 xh[4],
                                                                                                                 xh[0]))
        conn.commit()
        tk.messagebox.showinfo('提示', xh[0] + '信息更新成功！')
        conn.close()

    def delete(self):
        xh = self.nameStringvar.get()
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
        cursor.execute("delete from book where name = '{}'".format(xh))
        conn.commit()
        tk.messagebox.showinfo('提示', xh + '信息删除成功！')
        conn.close()

    def clear(self):
        self.nameStringvar.set('')
        self.authorStringvar.set('')
        self.numStringvar.set('')
        self.pressStringvar.set('')
        self.typeStringvar.set('')

    def borrow_book(self):
        # borrow_book_user.borrow_book_user(self.win)
        pass

    def return_book(self):
        pass

    def get_root(self):
        win = self.win
        tk.Button(win, text='清空', width=10, height=1, command=self.clear).grid(row=8, column=0, pady=5)
        tk.Button(win, text='查询', width=10, height=1, command=self.select).grid(row=8, column=1, pady=5)
        tk.Button(win, text='插入', width=10, height=1, command=self.insert).grid(row=8, column=2, pady=5)
        tk.Button(win, text='更新', width=10, height=1, command=self.update).grid(row=8, column=3, pady=5)
        tk.Button(win, text='删除', width=10, height=1, command=self.delete).grid(row=8, column=4, pady=5)
        tk.Button(win, text='借书', width=10, height=1, command=self.borrow_book).grid(row=8, column=5, pady=5)
        tk.Button(win, text='还书', width=10, height=1, command=self.return_book).grid(row=8, column=6, pady=5)

# win.mainloop()
