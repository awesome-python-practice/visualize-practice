import pymysql

# 打开数据库连接
host = "ufoto-bi-group.cluster-czficfutfvot.us-east-1.rds.amazonaws.com"
username = "ufoto"
password = "ufoto$1234"
schema = "ufoto_bi"
db = pymysql.connect(host, username, password, schema)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = """
        SELECT * FROM ufoto_bi.ufoto_day_conn_and_login_analysis 
       """
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        login_total_count = row[1]
        login_success_count = row[2]
        login_fail_count = row[3]
        conn_total_count = row[4]
        # 打印结果
        print("id=%s,login_total_count=%s,login_success_count=%s,login_fail_count=%s,conn_total_count=%s" % \
              (id, login_total_count, login_success_count, login_fail_count, conn_total_count))

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
