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
CREATE TABLE book_user(
    userid          TEXT PRIMARY KEY    NOT NULL,
    username        TEXT    NOT NULL,
    password        TEXT    NOT NULL,
    status          TEXT  ,
    lend_num        TEXT  ,  
    max_num         TEXT  );
''')
# 数据插入
cur.execute("INSERT INTO book_history (userid,username,password,status,lend_num,max_num) \
      VALUES ('2000300410', '王大锤','123', '1234567', '在借', '1'， '9')")

conn.commit()

# # 数据查询
# cur.execute("SELECT 学号,姓名,性别  from student")
# rows = cur.fetchall()
# for row in rows:
#    print("学号 = ", row[0])
#    print("姓名 = ", row[1])
#    print("性别 = ", row[2])
conn.close()
