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
CREATE TABLE book_history(
    book_id          TEXT     NOT NULL,
    name             TEXT    NOT NULL,
    userid           TEXT PRIMARY KEY   NOT NULL,
    username         TEXT    NOT NULL,
    begin_time       TEXT    NOT NULL,  
    end_time         TEXT    ,
    status           TEXT    NOT NULL);
''')
# 数据插入
cur.execute("INSERT INTO book_history (book_id,name,userid,username,begin_time,end_time,status) \
      VALUES ('1','python学习', '2000300410', '王大锤', '2000.01.01', '', '在借')")

cur.execute("INSERT INTO book_history (book_id,name,userid,username,begin_time,end_time,status) \
      VALUES ('1','Java学习', '2000300420', '刘半仙', '2010.12.12', '', '在借')")

cur.execute("INSERT INTO book_history (book_id,name,userid,username,begin_time,end_time,status) \
      VALUES ('1','语文魅力','2000300430', '乔峰', '2011.09.09', '2012.09.09', '已还')")
conn.commit()

# # 数据查询
# cur.execute("SELECT 学号,姓名,性别  from student")
# rows = cur.fetchall()
# for row in rows:
#    print("学号 = ", row[0])
#    print("姓名 = ", row[1])
#    print("性别 = ", row[2])
conn.close()
