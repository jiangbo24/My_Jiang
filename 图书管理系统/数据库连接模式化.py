import psycopg2

# 创建会话连接
conn = psycopg2.connect(dbname="postgres",
                        user="tom",
                        password="Huawei_123",
                        host="192.168.56.101",
                        port="26000")
# 编码
conn.set_client_encoding('utf8')
# 创建游标
cur = conn.cursor()


# 创建表
def create_db():
    cur.execute(
        '''
    CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);
    ''')


# 数据插入
def inset_db():
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
    conn.commit()


# 数据查询
def search_db():
    cur.execute("SELECT id, name, address, salary  from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3])
    conn.close()


# 关闭数据库
def close_db():
    conn.commit()
    conn.close()

