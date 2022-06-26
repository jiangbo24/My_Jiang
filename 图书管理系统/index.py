import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import psycopg2
from PIL import Image, ImageTk

# 导入消息对话框子模块
import tkinter.messagebox

import book_information
import book_user
import book_history


# 登录界面
class page_1:
    def __init__(self, root):
        self.root = root
        self.root.title("图书管理系统")
        self.root.geometry("620x490")

        # 创建一个Label标签展示图片
        self.img = Image.open('./img/login.png')
        self.photo = ImageTk.PhotoImage(self.img)
        self.image_Label = tkinter.Label(root, image=self.photo)
        self.image_Label.pack()

        # ttk中控件使用style对象设定
        self.root.Style01 = Style()
        self.root.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="Black")
        self.root.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.root.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="Black")
        # 创建一个Label标签 + Entry   --- 用户名
        self.Label_user = Label(self.root, text="用户名:", style="user.TLabel")
        self.Label_user.pack(side=LEFT, padx=10, pady=10)
        self.useridStringvar = StringVar()
        self.Entry_user = Entry(root, width=12, textvariable=self.useridStringvar)
        self.Entry_user.pack(side=LEFT, padx=10, pady=10)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self.root, text="密码:", style="user.TLabel")
        self.Label_password.pack(side=LEFT, padx=10, pady=10)
        self.passwordStringvar = StringVar()
        self.Entry_password = Entry(root, width=12, show="*", textvariable=self.passwordStringvar)
        self.Entry_password.pack(side=LEFT, padx=10, pady=10)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self.root, text="登录", width=4, command=self.change)
        self.Button_login.pack(side=LEFT, padx=20, pady=10)
        # 创建一个超级用户按钮    --- 登录
        self.super_Button_login = Button(self.root, text="管理", width=4, command=self.change1)
        self.super_Button_login.pack(side=LEFT)

        # 初始化超级用户
        self.super_userStringvar = None
        self.super_user_passwordStringvar = None
        self.super_user = None
        self.Entry_super_user = None
        self.Label_super_user_password = None
        self.super_user_Entry_password = None
        self.super_user_Button_login = None
        self.button = None
        self.super_image_Label = None

    # 从普通用户进入后台
    def change(self):
        self.image_Label.destroy()
        self.Label_user.destroy()
        self.Entry_user.destroy()
        self.Label_password.destroy()
        self.Entry_password.destroy()
        self.Button_login.destroy()
        self.super_Button_login.destroy()
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
        cursor.execute('select userid from book_user')
        userid = cursor.fetchall()
        found = 0
        for i in userid:
            for j in i:
                if self.useridStringvar.get() == j:
                    found = 1
                    page_3(root1)
        if found == 0:
            messagebox.showinfo('提示', self.useridStringvar.get() + '未找到用户信息，请注册！')
            page_2(root1)

    # 后台管理登录
    def change1(self):
        self.image_Label.destroy()
        self.Label_user.destroy()
        self.Entry_user.destroy()
        self.Label_password.destroy()
        self.Entry_password.destroy()
        self.Button_login.destroy()
        self.super_Button_login.destroy()

        # 创建一个Label标签展示图片
        self.img = Image.open('./img/super_login.png')
        self.photo = ImageTk.PhotoImage(self.img)
        self.super_image_Label = tkinter.Label(self.root, image=self.photo)
        self.super_image_Label.pack()

        self.super_user = Label(self.root, text="管理名:", style="user.TLabel")
        self.super_user.pack(side=LEFT, padx=1, pady=5)
        self.super_userStringvar = StringVar()
        self.Entry_super_user = Entry(self.root, width=12, textvariable=self.super_userStringvar)
        self.Entry_super_user.pack(side=LEFT, padx=5, pady=10)
        # 创建一个Label标签 + Entry   --- 密码
        self.Label_super_user_password = Label(self.root, text="管理密码:", style="user.TLabel")
        self.Label_super_user_password.pack(side=LEFT, padx=1, pady=5)
        self.super_user_passwordStringvar = StringVar()
        self.super_user_Entry_password = Entry(self.root, width=12, show="*",
                                               textvariable=self.super_user_passwordStringvar)
        self.super_user_Entry_password.pack(side=LEFT, padx=5, pady=10)
        # 创建一个按钮    --- 登录
        self.super_user_Button_login = Button(self.root, text="登录", width=4, command=self.change2)
        self.super_user_Button_login.pack(side=LEFT, padx=5, pady=10)

        self.button = Button(self.root, text="返回", command=self.back)
        self.button.pack(side=LEFT, padx=5, pady=10)

    # 从后台管理进入后台页面
    def change2(self):
        self.super_user.destroy()
        self.Entry_super_user.destroy()
        self.Label_super_user_password.destroy()
        self.super_user_Entry_password.destroy()
        self.super_user_Button_login.destroy()
        self.button.destroy()
        self.super_image_Label.destroy()
        found = 0
        if self.super_userStringvar.get() == '110' and self.super_user_passwordStringvar.get() == '110':
            found = 1
            page_3(root1)
        if found == 0:
            messagebox.showinfo('提示', self.useridStringvar.get() + '输入错误，请重新输入！')
            page_1(root1).change1()

    def back(self):
        self.super_user.destroy()
        self.Entry_super_user.destroy()
        self.Label_super_user_password.destroy()
        self.super_user_Entry_password.destroy()
        self.super_user_Button_login.destroy()
        self.button.destroy()
        self.super_image_Label.destroy()
        page_1(root1)


# 注册页面
class page_2:
    def __init__(self, root):
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
        self.root = root
        root.title("mytest")
        root.geometry("620x490")

        # ttk中控件使用style对象设定
        self.root.Style01 = Style()
        self.root.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="Black")
        self.root.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.root.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="Black")

        Label(self.root, text='用户id：', style='user.TLabel').place(x=10, y=10)
        self.useridStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.useridStringvar, style='TEntry').place(x=130, y=15)

        Label(self.root, text='用户：', style='user.TLabel').place(x=10, y=60)
        self.usernameStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.usernameStringvar, style='TEntry').place(x=130, y=65)

        Label(self.root, text='密码：', style='user.TLabel').place(x=10, y=110)
        self.passwordStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.passwordStringvar, style='TEntry').place(x=130, y=115)

        Label(self.root, text='电话：', style='user.TLabel').place(x=10, y=160)
        self.phoneStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.phoneStringvar, style='TEntry').place(x=130, y=165)

        self.register_button = None
        self.button = None
        self.get_button()

        self.max_numStringvar = 10
        self.lend_numStringvar = 0
        self.statusStringvar = '未借'

    def get_button(self):
        self.register_button = Button(self.root, text="注册", command=self.insert)
        self.register_button.pack(side=LEFT)
        self.button = Button(self.root, text="返回", command=self.back)
        self.button.pack(side=BOTTOM)

    def back(self):
        self.register_button.destroy()
        self.button.destroy()
        page_1(self.root)
        # pass

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
            self.statusStringvar, self.lend_numStringvar, self.max_numStringvar))
        conn.commit()
        messagebox.showinfo('提示', self.useridStringvar.get() + '信息注册成功！')
        conn.close()


# 数据库查询首页
class page_3:
    def __init__(self, root):
        self.root = root
        root.title("mytest")
        root.geometry("910x500")
        self.root.title('图书管理系统')
        # 设置窗口大小
        self.root.minsize(500, 500)

        self.tabControl = Notebook(self.root)

        # 图书信息
        self.tab1 = Frame(self.tabControl)  # Create a tab
        self.tabControl.add(self.tab1, text='图书信息')  # Add the tab
        book_information.book_information(self.tab1)

        # 图书借阅信息
        self.tab2 = Frame(self.tabControl)  # Add a second tab
        self.tabControl.add(self.tab2, text='图书借阅信息')  # Make second tab visible
        book_history.book_history(self.tab2)

        # 借阅者信息
        self.tab3 = Frame(self.tabControl)  # Add a third tab
        self.tabControl.add(self.tab3, text='借阅者信息')  # Make second tab visible
        book_user.book_user(self.tab3)

        self.tabControl.pack(expand=1, fill="both")

        self.button = Button(self.root, text="返回", command=self.back)
        self.button.pack()

    def back(self):
        self.tabControl.destroy()
        self.button.destroy()
        page_1(root1)


root1 = Tk()
p1 = page_1(root1)
root1.mainloop()
