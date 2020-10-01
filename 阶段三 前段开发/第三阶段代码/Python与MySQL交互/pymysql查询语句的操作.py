# 1. 导包
import pymysql


def run():
    # 2. 创建连接对象
    conn = pymysql.connect(host="localhost",
                           port="3306",
                           user="root",
                           password="mysql",
                           database="python41",
                           charset="utf8")
    # 3. 获取游标，目的就是要执行sql语句
    cursor = conn.cursor()
    # 准备sql，之前在MySQL客户端怎么写sql，在这里就怎么写
    sql = "select * from students;"
    # 4. 执行sql语句
    cursor.execute(sql)
    # 返回的数据类型是一个元组，其中元组里面的每天数据还是元组
    for i in cursor.fetchall():
        print(i)
    # 5. 关闭游标
    cursor.close()
    # 6. 关闭连接
    conn.close()


if __name__ == '__main__':
    run()


