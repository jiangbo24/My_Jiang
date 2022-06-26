import psycopg2

conn = psycopg2.connect(dbname="postgres",
                        user="tom",
                        password="Huawei_123",
                        host="192.168.56.101",
                        port="26000")
conn.set_client_encoding('utf8')
cur = conn.cursor()

# 创建表
cur.execute(
    '''
CREATE TABLE book(
    name        TEXT PRIMARY KEY   NOT NULL,
    author      TEXT     NOT NULL,
    num         TEXT    NOT NULL,
    press       TEXT    NOT NULL,  
    type        TEXT    NOT NULL,
    # FOREIGN KEY (name) REFERENCES book_user(name),
    
    );
''')
# 数据插入
cur.execute("INSERT INTO book_history (name,author,num,press,type) \
      VALUES ('python学习','王大锤', '2', '清华出版社', '计算机类')")

conn.commit()

# # 数据查询
# cur.execute("SELECT 学号,姓名,性别  from student")
# rows = cur.fetchall()
# for row in rows:
#    print("学号 = ", row[0])
#    print("姓名 = ", row[1])
#    print("性别 = ", row[2])
conn.close()
