from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import index


class borrow_book_user:
    def __init__(self, root):
        self.root = root
        root.title("借书信息")
        root.geometry("620x490")

        # ttk中控件使用style对象设定
        self.root.Style01 = Style()
        self.root.Style01.configure("user.TLabel", font=("华文黑体", 20, "bold"), foreground="Black")
        self.root.Style01.configure("TEntry", font=("华文黑体", 20, "bold"))
        self.root.Style01.configure("TButton", font=("华文黑体", 20, "bold"), foreground="Black")

        Label(self.root, text='图书名：', style='user.TLabel').place(x=10, y=10)
        self.useridStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.useridStringvar, style='TEntry').place(x=130, y=15)

        Label(self.root, text='用户id：', style='user.TLabel').place(x=10, y=60)
        self.usernameStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.usernameStringvar, style='TEntry').place(x=130, y=65)

        Label(self.root, text='用户名：', style='user.TLabel').place(x=10, y=110)
        self.useridStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.useridStringvar, style='TEntry').place(x=130, y=115)

        Label(self.root, text='密码：', style='user.TLabel').place(x=10, y=160)
        self.passwordStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.passwordStringvar, style='TEntry').place(x=130, y=165)

        Label(self.root, text='电话：', style='user.TLabel').place(x=10, y=210)
        self.phoneStringvar = StringVar()
        Entry(self.root, width=20, textvariable=self.phoneStringvar, style='TEntry').place(x=130, y=215)

    def back(self):
        # index.page_3()

        self.super_Button_login = Button(self.root, text="返回", width=4, command=self.back)
        self.super_Button_login.pack(side=BOTTOM)


root1 = Tk()
borrow_book_user(root1)
root1.mainloop()
